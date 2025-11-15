#include <avr/io.h>
#include <util/delay.h>

#define TLC_LE PB1
#define TLC_OE PB2

#define SET(port, bit) ((port) |= (1 << (bit)))
#define CLR(port, bit) ((port) &= ~(1 << (bit)))

const uint8_t digits[10] = {
    0b00111111, // 0
    0b00000110, // 1
    0b01011011, // 2
    0b01001111, // 3
    0b01100110, // 4
    0b01101101, // 5
    0b01111101, // 6
    0b00000111, // 7
    0b01111111, // 8
    0b01101111  // 9
};

static void spi_init(void)
{
    // MOSI (PB3), SCK (PB5), LE, OE jako wyjścia
    DDRB |= (1 << PB3) | (1 << PB5) | (1 << TLC_LE) | (1 << TLC_OE);

    // włącz SPI, tryb master, mode 0 (CPOL=0, CPHA=0), zegar F_CPU/128
    SPCR = (1 << SPE) | (1 << MSTR) | (1 << SPR1) | (1 << SPR0);

    CLR(PORTB, TLC_OE); // domyślnie wszystkie LED zapalone (OE=1)
    CLR(PORTB, TLC_LE); // LE w stanie niskim
}

static void spi_send(uint8_t data)
{
    SPDR = data; // start transmisji
    while (!(SPSR & (1 << SPIF))) {} // czekaj na koniec
}

static void tlc_write(uint8_t pattern)
{
    spi_send(pattern);

    // krótki impuls na LE – przerzutnik wyjściowy aktualizuje się na opadającym zboczu
    SET(PORTB, TLC_LE);
    _delay_us(1);
    CLR(PORTB, TLC_LE);
}

int main(void)
{
    spi_init();
    uint8_t i = 0;

    while(1)
    {
        tlc_write(digits[i]);
        _delay_ms(1000);
        if (i++ >= 10) i = 0;
    }
}
