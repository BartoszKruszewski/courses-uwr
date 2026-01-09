#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/pgmspace.h>
#include <avr/sleep.h>
#include "dzwiek.c" // trzeba dodac PROGMEM

#define CS_PIN PB2
#define CS_PORT PORTB
#define CS_DDR DDRB

#define SAMPLE_RATE 8000
const uint16_t num_samples = sizeof(dzwiek_raw) / sizeof(dzwiek_raw[0]);

volatile uint16_t sample_index = 0;
volatile uint8_t playback_active = 1;

void spi_init(void) {
    DDRB |= (1 << DDB3) | (1 << DDB5) | (1 << DDB2); // PB2 jako wyjscie
    PORTB |= (1 << CS_PIN); // CS stan wysoki (nieaktywny)
    SPCR = (1 << SPE) | (1 << MSTR) | (1 << SPR0); // Włącz SPI, tryb master, CPOL=0, CPHA=0
}

// Wysłanie jednego bajtu przez SPI
uint8_t spi_transfer(uint8_t data) {
    SPDR = data;
    while (!(SPSR & (1 << SPIF)));
    return SPDR;
}

void dac_write(uint8_t value) {
    uint16_t command;
    
    // Budowa 16-bitowego rejestru komend dla MCP4901:
    // Bit 15: 0 - Write to DAC register
    // Bit 14: 0 - Vref unbuffered
    // Bit 13 (GA): 1 - Output gain = 1x (VOUT = VREF * D/256)
    // Bit 12 (SHDN): 1 - Output active (not shutdown)
    // Bits 11-4: 8-bit data (dla MCP4901)
    // Bits 3-0: Don't care (0)
    
    // Format: 0011 DDDD DDDD 0000
    // gdzie DDDD DDDD to 8-bitowa wartość DAC
    command = 0x7000 | ((uint16_t)value << 4);
    
    
    CS_PORT &= ~(1 << CS_PIN); // CS low - rozpoczęcie transmisji
    spi_transfer((command >> 8) & 0xFF); // Wyślij starszy bajt
    spi_transfer(command & 0xFF); // Wyślij młodszy bajt
    CS_PORT |= (1 << CS_PIN); // CS high - zakończenie transmisji
}

// Inicjalizacja Timer1 dla generowania przerwań co 1/8000 sekundy
void timer_init(void) {
    // Tryb CTC (Clear Timer on Compare Match)
    TCCR1B |= (1 << WGM12);
    
    // Wartość porównania dla 8 kHz przy 16 MHz i prescaler 8
    // OCR1A = (F_CPU / (prescaler * sample_rate)) - 1
    // OCR1A = (16000000 / (8 * 8000)) - 1 = 249
    OCR1A = 249;
    
    // Prescaler = 8
    TCCR1B |= (1 << CS11);
    
    // Włącz przerwanie porównania
    TIMSK1 |= (1 << OCIE1A);
}

// Przerwanie timera - odtwarzanie próbek
ISR(TIMER1_COMPA_vect) {
    if (playback_active && sample_index < num_samples) {
        dac_write(pgm_read_byte(&dzwiek_raw[sample_index]));
        sample_index++;
    } else {
        playback_active = 0;
    }
}

int main(void) {
    spi_init();
    timer_init();
    sei();
    set_sleep_mode(SLEEP_MODE_IDLE);
    while (1) sleep_mode();
    return 0;
}
