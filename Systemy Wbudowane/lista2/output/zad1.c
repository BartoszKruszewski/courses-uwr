#include <avr/io.h>
#include <util/delay.h>
#include <stdio.h>

#define LED PB5
#define LED_DDR DDRB
#define LED_PORT PORTB

#define BTN PD2
#define BTN_PIN PIND
#define BTN_PORT PORTD

#define DELAY 100 // time units
#define TIME_UNIT 10 // ms
#define HOLD_TIME 2

#define BUFFER_SIZE (DELAY / HOLD_TIME) * 2 // ile max razy przycisk moze zostac nacisniety (*2 dla bezpieczenstwa)

static int8_t buffer[BUFFER_SIZE] = {0}; // event timestamp (in time units)
static int8_t bufferWriteCounter = 0;
static int8_t bufferReadCounter = 0;
static int8_t timer = 0; // time units
static int8_t hold = 0;  // time units

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

int main(void)
{
    BTN_PORT |= _BV(BTN);
    LED_DDR |= _BV(LED);

    while (1)
    {
        if (button_pressed())
        {
            if (hold++ == HOLD_TIME)
                buffer[bufferWriteCounter++] = timer + DELAY;
        }
        else
        {
            hold = 0;
        }

        if (bufferReadCounter != bufferWriteCounter && buffer[bufferReadCounter] == timer)
        {
            buffer[bufferReadCounter] = 0;
            bufferReadCounter++;
            led_on();
        }
        else
        {
            led_off();
        }

        _delay_ms(TIME_UNIT);
        timer++;

        if (bufferReadCounter == BUFFER_SIZE - 1) bufferReadCounter = 0;
        if (bufferWriteCounter == BUFFER_SIZE - 1) bufferWriteCounter = 0;
    }
}