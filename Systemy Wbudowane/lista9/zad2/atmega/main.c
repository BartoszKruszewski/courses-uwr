#include <avr/io.h>
#include <avr/interrupt.h>

#define LED_PIN PD5
#define BTN_PIN PD2
#define SPI_MOSI PB3
#define SPI_MISO PB4
#define SPI_SCK PB5

int main(void)
{
    DDRD |= (1 << LED_PIN);
    DDRD &= ~(1 << BTN_PIN);
    PORTD |= (1 << BTN_PIN); // Pull-up

    DDRB &= ~((1 << SPI_MOSI) | (1 << SPI_SCK));
    DDRB |= (1 << SPI_MISO);
    PORTB |= (1 << SPI_MOSI) | (1 << SPI_SCK); // Pull-up

    uint8_t data_out = 0;
    uint8_t data_in = 0;

    while (1)
    {
        uint8_t my_btn = (!(PIND & (1 << BTN_PIN))) ? 1 : 0;
        data_out = my_btn;

        // Czekamy, aż zegar będzie NISKI (Master gotowy)
        while (PINB & (1 << SPI_SCK))
            ;

        if (data_out & 0x80)
            PORTB |= (1 << SPI_MISO);
        else
            PORTB &= ~(1 << SPI_MISO);
        data_out <<= 1;

        // Pętla 8 bitów
        uint8_t current_byte_in = 0;

        for (int i = 0; i < 8; i++)
        {
            // 1. Czekaj na Zegar HIGH (Rising Edge) - Master czyta nasz bit
            while (!(PINB & (1 << SPI_SCK)))
                ;

            // My czytamy bit Mastera z MOSI
            current_byte_in <<= 1;
            if (PINB & (1 << SPI_MOSI))
                current_byte_in |= 1;

            // 2. Czekaj na Zegar LOW (Falling Edge)
            while (PINB & (1 << SPI_SCK))
                ;

            // 3. Wystaw KOLEJNY bit na MISO (jeśli to nie był ostatni cykl)
            if (i < 7)
            {
                if (data_out & 0x80)
                    PORTB |= (1 << SPI_MISO);
                else
                    PORTB &= ~(1 << SPI_MISO);
                data_out <<= 1;
            }
        }

        data_in = current_byte_in;

        // Dioda
        if (data_in == 1)
            PORTD |= (1 << LED_PIN);
        else
            PORTD &= ~(1 << LED_PIN);
    }
}
