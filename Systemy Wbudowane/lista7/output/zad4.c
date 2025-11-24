#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include <stdio.h>
#include "uart.h"

// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
// Trzeba czasami zresetować program jeżeli nie działa za pierwszym razem
// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

// --- Konfiguracja pinów Software SPI (Master) ---
// Używamy portu D
#define SW_SPI_PORT PORTD
#define SW_SPI_DDR  DDRD
#define SW_SPI_PIN  PIND

#define SW_SS   PD4
#define SW_MOSI PD5
#define SW_MISO PD6
#define SW_SCK  PD7

// --- Konfiguracja pinów Hardware SPI (Slave) ---
// Używamy portu B
#define HW_SS   PB2
#define HW_MOSI PB3
#define HW_MISO PB4
#define HW_SCK  PB5

volatile uint8_t slave_received_data = 0;
volatile uint8_t slave_new_data_flag = 0;

void spi_init(void) {
    // Konfiguracja kierunków: SS, MOSI, SCK jako wyjścia
    SW_SPI_DDR |= (1 << SW_SS) | (1 << SW_MOSI) | (1 << SW_SCK);
    // MISO jako wejście
    SW_SPI_DDR &= ~(1 << SW_MISO);
    // Włącz pull-up na MISO
    SW_SPI_PORT |= (1 << SW_MISO);
    
    // Stan początkowy: SS wysoki (nieaktywny), SCK niski (Mode 0)
    SW_SPI_PORT |= (1 << SW_SS);
    SW_SPI_PORT &= ~(1 << SW_SCK);
}

uint8_t spi_transfer(uint8_t data) {
    uint8_t received = 0;
    
    // Aktywuj Slave (SS Low)
    SW_SPI_PORT &= ~(1 << SW_SS);
    _delay_us(1); // Krótkie opóźnienie na stabilizację
    
    // Pętla dla 8 bitów (MSB first)
    for (uint8_t i = 0; i < 8; i++) {
        // 1. Ustaw MOSI zgodnie z bitem danych (MSB)
        if (data & 0x80) {
            SW_SPI_PORT |= (1 << SW_MOSI);
        } else {
            SW_SPI_PORT &= ~(1 << SW_MOSI);
        }
        
        // Przesuń dane do następnego bitu
        data <<= 1;
        
        // 2. Zbocze narastające SCK (Clock High) - Slave czyta MOSI
        _delay_us(5); // Opóźnienie dla "półokresu" zegara
        SW_SPI_PORT |= (1 << SW_SCK);
        
        // 3. Odczytaj MISO (MSB)
        received <<= 1;
        if (SW_SPI_PIN & (1 << SW_MISO)) {
            received |= 1;
        }
        
        // 4. Zbocze opadające SCK (Clock Low) - Slave wystawia MISO
        _delay_us(5);
        SW_SPI_PORT &= ~(1 << SW_SCK);
    }
    
    // Dezaktywuj Slave (SS High)
    SW_SPI_PORT |= (1 << SW_SS);
    
    return received;
}

void spi_slave_init(void) {
    // Konfiguracja kierunków dla Slave: MISO wyjście, reszta wejścia
    DDRB |= (1 << HW_MISO);  // MISO Output
    DDRB &= ~((1 << HW_MOSI) | (1 << HW_SCK) | (1 << HW_SS)); // MOSI, SCK, SS Input
    
    // Włącz pull-up na SS
    PORTB |= (1 << HW_SS);
    
    // Konfiguracja rejestru SPCR:
    // SPE (SPI Enable) - włącz SPI
    // SPIE (SPI Interrupt Enable) - włącz przerwania
    // Bit MSTR = 0 (tryb Slave)
    SPCR = (1 << SPE) | (1 << SPIE);
}

// Obsługa przerwania Hardware SPI Slave
// Wywoływane gdy Slave odbierze pełny bajt
ISR(SPI_STC_vect) {
    slave_received_data = SPDR; // Odczytaj odebrane dane
    slave_new_data_flag = 1;    // Ustaw flagę
    // Załaduj dane do wysłania w następnej transakcji
    SPDR = slave_received_data + 1; 
}

int main(void) {
    uart_init();
    uart_stdio_setup();
    stdin = stdout = &uart_file;

    spi_slave_init(); // Najpierw Slave
    spi_init();       // Potem Master
    
    sei();
    
    uint8_t counter = 1;
    
    while (1) {
        printf("Master sending: %u\n", counter);
        
        // Master wysyła dane i odbiera odpowiedź (z poprzedniej transakcji)
        uint8_t master_received = spi_transfer(counter);
        
        // Sprawdź czy Slave odebrał dane (przerwanie powinno zadziałać)
        if (slave_new_data_flag) {
            slave_new_data_flag = 0;
            printf("Slave received: %u\n", slave_received_data);
            printf("Master received back: %u\n", master_received);
            printf("---\n");
        } else {
            printf("Error: Slave did not respond!\n");
        }
        
        counter++;
        _delay_ms(1000); // Czekaj 1s
    }
    
    return 0;
}
