#include <avr/io.h>
#include <util/delay.h>

#define LED_PIN PB2  // Pin 5
#define BTN_PIN PA7  // Pin 6
#define SPI_MOSI PA6 // Pin 7
#define SPI_MISO PA5 // Pin 8
#define SPI_SCK PA4  // Pin 9

void spi_init(void)
{
    DDRA |= (1 << SPI_MOSI) | (1 << SPI_SCK); // Wyjścia
    DDRA &= ~(1 << SPI_MISO);                 // Wejście
    PORTA |= (1 << SPI_MISO);                 // PULL-UP NA MISO

    PORTA &= ~(1 << SPI_SCK);  // SCK Low
    PORTA &= ~(1 << SPI_MOSI); // MOSI Low
}

uint8_t spi_transfer(uint8_t data_out)
{
    uint8_t data_in = 0;

    for (uint8_t i = 0; i < 8; i++)
    {
        // 1. SETUP: Ustaw MOSI
        if (data_out & 0x80)
            PORTA |= (1 << SPI_MOSI);
        else
            PORTA &= ~(1 << SPI_MOSI);

        data_out <<= 1;
        _delay_ms(2); // Czekaj aż sygnał się ustabilizuje

        // 2. CLOCK HIGH (Slave czyta MOSI)
        PORTA |= (1 << SPI_SCK);
        _delay_ms(2); // Trzymaj zegar wysoko

        // 3. READ MISO (Master czyta co Slave wystawił)
        data_in <<= 1;
        if (PINA & (1 << SPI_MISO))
            data_in |= 1;

        // 4. CLOCK LOW (Slave wystawia nowy bit na MISO)
        PORTA &= ~(1 << SPI_SCK);
        _delay_ms(2);
    }

    // Po transmisji wyzeruj MOSI
    PORTA &= ~(1 << SPI_MOSI);
    return data_in;
}

int main(void)
{
    DDRB |= (1 << LED_PIN);
    DDRA &= ~(1 << BTN_PIN);
    PORTA |= (1 << BTN_PIN);

    spi_init();

    // Mignij na start
    PORTB |= (1 << LED_PIN);
    _delay_ms(200);
    PORTB &= ~(1 << LED_PIN);
    _delay_ms(200);

    while (1)
    {
        uint8_t val = (PINA & (1 << BTN_PIN)) ? 0 : 1;
        uint8_t rec = spi_transfer(val);

        if (rec == 1)
        {
            PORTB |= (1 << LED_PIN);
        }
        else
        {
            PORTB &= ~(1 << LED_PIN);
        }
    }
}
