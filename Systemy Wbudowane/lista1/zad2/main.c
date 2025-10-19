#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
    DDRD = 0xFF; // Ustawienie całego portu D jako wyjścia

    while (1)
    {
        // Zapalaj piny PD0–PD7 po kolei
        for (uint8_t i = 0; i <= 7; i++)
        {
            PORTD |= (1 << i); // Włącz i-ty pin
            _delay_ms(100);
            PORTD &= ~(1 << i); // Wyłącz i-ty pin
        }
        _delay_ms(100); // Krótka przerwa po zakończeniu sekwencji
    }
}
