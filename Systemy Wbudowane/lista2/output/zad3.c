#include <avr/io.h>
#include <util/delay.h>

#define BTN_RESET PC0
#define BTN_NEXT PC1
#define BTN_PREV PC2

#define DEBOUNCE 30

uint8_t binary_to_gray(uint8_t n)
{
    return n ^ (n >> 1);
}

uint8_t debounce(uint8_t pin)
{
    if (!(PINC & (1 << pin)))
    {                             // Przycisk wciśnięty
        _delay_ms(DEBOUNCE);            // Odczekaj na ustabilizowanie
        if (!(PINC & (1 << pin))) // Ponowne sprawdzenie
        {
            while (!(PINC & (1 << pin))); // Czekaj na puszczenie
            _delay_ms(DEBOUNCE); // Debounce na puszczenie
            return 1;
        }
    }
    return 0;
}

int main(void)
{
    DDRD = 0xFF;  // PORTD jako wyjście
    DDRC = 0x00;  // PORTB jako wejście
    PORTC = 0x07; // pull-up na PC0-PC2

    uint8_t counter = 0;

    while (1)
    {
        if (debounce(BTN_RESET))
            counter = 0;
        if (debounce(BTN_NEXT))
            counter++;
        if (debounce(BTN_PREV))
            counter--;

        PORTD = binary_to_gray(counter);
    }

    return 0;
}
