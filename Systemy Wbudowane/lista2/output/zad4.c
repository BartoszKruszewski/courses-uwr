#include <avr/io.h>
#include <util/delay.h>

const uint8_t digits[10] = {
    0b11000000, // 0: A,B,C,D,E,F
    0b11111001, // 1: B,C
    0b10100100, // 2: A,B,D,E,G
    0b10110000, // 3: A,B,C,D,G
    0b10011001, // 4: B,C,F,G
    0b10010010, // 5: A,C,D,F,G
    0b10000010, // 6: A,C,D,E,F,G
    0b11111000, // 7: A,B,C
    0b10000000, // 8: A,B,C,D,E,F,G
    0b10010000  // 9: A,B,C,D,F,G
};

void display_number(uint8_t num)
{
    uint8_t tens = num / 10;
    uint8_t ones = num % 10;

    PORTC |= (1 << PC1);
    PORTD = digits[tens];
    PORTC &= ~(1 << PC0);
    _delay_ms(5);

    PORTC |= (1 << PC0);
    PORTD = digits[ones];
    PORTC &= ~(1 << PC1);
    _delay_ms(5);
}

int main(void)
{
    DDRD = 0xFF;                      // PD0-PD7 jako wyjscia
    DDRC |= (1 << PC0) | (1 << PC1);  // PC0, PC1 jako wyjscia
    PORTC |= (1 << PC0) | (1 << PC1); // Oba wyświetlacze wylaczone

    uint8_t counter = 0;
    uint8_t refresh_count = 0;

    while (1)
    {
        display_number(counter);    // 10ms
        if (refresh_count++ >= 100) // 100 * 10ms = 1s
        {
            if (counter++ > 59)
                counter = 0;
            refresh_count = 0;
        }
    }
}
