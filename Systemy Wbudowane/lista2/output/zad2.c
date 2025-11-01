#include <avr/io.h>
#include <util/delay.h>
#include <stdio.h>
#include "uart.h"

#define LED PB5
#define LED_DDR DDRB
#define LED_PORT PORTB

#define BTN PD2
#define BTN_PIN PIND
#define BTN_PORT PORTD

#define TIME_UNIT 10
#define DIT_MAX 20  // time units
#define CHAR_GAP 30 // time units
#define WORD_GAP 70 // time units

// Kodowanie: 3 bity długości + 5 bitów kodu
typedef struct
{
    uint8_t pattern;
    char letter;
} MorseCode;

const MorseCode morse_table[] = {
    {0b00100000, 'E'}, // .
    {0b00110000, 'T'}, // -
    {0b01000000, 'I'}, // ..
    {0b01001000, 'A'}, // .-
    {0b01010000, 'N'}, // -.
    {0b01011000, 'M'}, // --
    {0b01100000, 'S'}, // ...
    {0b01100100, 'U'}, // ..-
    {0b01101000, 'R'}, // .-.
    {0b01101100, 'W'}, // .--
    {0b01110000, 'D'}, // -..
    {0b01110100, 'K'}, // -.-
    {0b01111000, 'G'}, // --.
    {0b01111100, 'O'}, // ---
    {0b10000000, 'H'}, // ....
    {0b10000010, 'V'}, // ...-
    {0b10000100, 'F'}, // ..-.
    {0b10001000, 'L'}, // .-..
    {0b10001100, 'P'}, // .--.
    {0b10001110, 'J'}, // .---
    {0b10010000, 'B'}, // -...
    {0b10010010, 'X'}, // -..-
    {0b10010100, 'C'}, // -.-.
    {0b10010110, 'Y'}, // -.--
    {0b10011000, 'Z'}, // --..
    {0b10011010, 'Q'}, // --.-
    {0b10100000, '5'}, // .....
    {0b10100001, '4'}, // ....-
    {0b10100011, '3'}, // ...--
    {0b10100111, '2'}, // ..---
    {0b10101111, '1'}, // .----
    {0b10110000, '6'}, // -....
    {0b10111000, '7'}, // --...
    {0b10111100, '8'}, // ---..
    {0b10111110, '9'}, // ----.
    {0b10111111, '0'}, // -----
    {0, '\0'}};

uint8_t morse_buffer = 0;
uint8_t morse_bit_count = 0;

void led_on(void)
{
    LED_PORT |= _BV(LED);
}

static inline void led_off(void)
{
    LED_PORT &= ~_BV(LED);
}

uint8_t button_pressed(void)
{
    return !(BTN_PIN & _BV(BTN));
}

char decode_morse(uint8_t pattern)
{
    for (uint8_t i = 0; morse_table[i].letter != '\0'; i++)
    {
        if (morse_table[i].pattern == pattern)
        {
            return morse_table[i].letter;
        }
    }
    return '?';
}

void add_dit(void)
{
    morse_bit_count++;
    morse_buffer = (morse_buffer & 0b00011111) | (morse_bit_count << 5);
}

void add_dah(void)
{
    morse_buffer |= (1 << (4 - morse_bit_count));
    morse_bit_count++;
    morse_buffer = (morse_buffer & 0b00011111) | (morse_bit_count << 5);
}

void clear_buffer(void)
{
    morse_buffer = 0;
    morse_bit_count = 0;
}

uint16_t wait_for_release(void)
{
    uint16_t counter = 0;
    uint8_t dash_signaled = 0;

    while (button_pressed())
    {
        _delay_ms(TIME_UNIT);
        counter++;

        // LED sygnalizuje kreskę
        if (counter >= DIT_MAX && !dash_signaled)
        {
            led_on();
            dash_signaled = 1;
        }
    }

    led_off();
    return counter;
}

uint16_t wait_silence(void)
{
    uint16_t counter = 0;

    while (!button_pressed() && counter < WORD_GAP + 10)
    {
        _delay_ms(TIME_UNIT);
        counter++;
    }

    return counter;
}

int main(void)
{
    BTN_PORT |= _BV(BTN);
    LED_DDR |= _BV(LED);

    uart_init();
    uart_stdio_setup();
    stdout = &uart_file;

    clear_buffer();
    led_off();

    while (1)
    {
        if (button_pressed())
        {
            uint16_t press_duration = wait_for_release();

            if (morse_bit_count < 5)
            {
                if (press_duration > 3 && press_duration < DIT_MAX)
                    add_dit();
                else if (press_duration >= DIT_MAX)
                    add_dah();
            }

            uint16_t silence = wait_silence();

            // Dekoduj znak po przerwie między znakami
            if (silence >= CHAR_GAP && morse_bit_count > 0)
            {
                char decoded = decode_morse(morse_buffer);
                printf("%c", decoded);
                fflush(stdout); // natychmiastowe wypisane
                clear_buffer();
            }

            // Spacja między słowami
            if (silence >= WORD_GAP)
            {
                printf(" ");
                fflush(stdout); // natychmiastowe wypisane
            }
        }

        _delay_ms(TIME_UNIT);
    }

    return 0;
}
