#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>
#include <stdio.h>
#include <stdlib.h>
#include "uart.h" 

#define HEATER_PIN  PB5
#define HEATER_PORT PORTB
#define HEATER_DDR  DDRB

#define HYSTERESIS  1.0    // Th = 1 stopień Celsjusza

float target_temp = 30.0;
char rx_buffer[10];        // Bufor na dane z UART
uint8_t rx_index = 0;

// Inicjalizacja ADC dla MCP9700 z referencją 1.1V
void adc_init(void) {
    // REFS1:0 = 11 -> Wewnętrzne napięcie referencyjne 1.1V
    // MUX3:0 = 0000 -> Kanał ADC0
    ADMUX = _BV(REFS1) | _BV(REFS0); 
    
    // ADEN = 1 -> Włącz ADC
    // ADPS2:0 = 111 -> Prescaler 128 (16MHz/128 = 125kHz, idealnie dla ADC)
    ADCSRA = _BV(ADEN) | _BV(ADPS2) | _BV(ADPS1) | _BV(ADPS0);
}

// Odczyt temperatury z uśrednianiem
float read_temperature(void) {
    uint32_t adc_sum = 0;
    const uint8_t samples = 20;

    for (uint8_t i = 0; i < samples; i++) {
        ADCSRA |= _BV(ADSC);          // Start konwersji
        while (ADCSRA & _BV(ADSC));   // Czekaj na koniec
        adc_sum += ADC;
        _delay_ms(1);
    }
    
    float adc_avg = (float)adc_sum / samples;
    
    // Obliczenia dla MCP9700 przy Vref = 1.1V
    // Wzór: Vout = Tc * Ta + V0  => Ta = (Vout - V0) / Tc
    // Vout = ADC * (1.1 / 1024.0)
    // Tc = 0.01 V/C, V0 = 0.5 V
    // Temp = (ADC * (1.1/1024) - 0.5) / 0.01
    // Temp = ADC * 0.10742 - 50.0
    
    float voltage = adc_avg * (1.1 / 1024.0);
    float temperature = (voltage - 0.5) * 100.0;
    
    return temperature;
}

// Obsługa wejścia UART bez blokowania
void check_uart_input(void) {
    // Sprawdź, czy coś przyszło (bit RXC0 w rejestrze UCSR0A)
    if (UCSR0A & _BV(RXC0)) {
        char c = UDR0; // Odczytaj znak
        
        // Echo (opcjonalnie, żeby widzieć co się wpisuje)
        uart_transmit(c, &uart_file); 

        // Jeśli koniec linii (Enter), parsuj liczbę
        if (c == '\n' || c == '\r') {
            rx_buffer[rx_index] = '\0'; // Null-terminate
            if (rx_index > 0) {
                float new_val = atof(rx_buffer);
                if (new_val > 5.0 && new_val < 100.0) { // Proste zabezpieczenie zakresu
                    target_temp = new_val;
                    printf("\r\nZmieniono cel na: %.1f C\r\n", target_temp);
                } else {
                     printf("\r\nBledna wartosc!\r\n");
                }
            }
            rx_index = 0; // Reset bufora
        } 
        // Zbieranie cyfr i kropki
        else if (rx_index < sizeof(rx_buffer) - 1) {
            rx_buffer[rx_index++] = c;
        }
    }
}

int main(void) {
    uart_init();
    uart_stdio_setup();
    stdin = stdout = &uart_file;
    adc_init();

    HEATER_DDR |= _BV(HEATER_PIN);
    HEATER_PORT &= ~_BV(HEATER_PIN);

    printf("Wpisz nowa temperature i nacisnij Enter.\r\n");

    uint8_t heater_state = 0; // 0 - wyłączona, 1 - włączona

    while (1) {
        check_uart_input();
        float current_temp = read_temperature();

        // Logika histerezy
        // Jeśli włączona i przekroczyła T -> Wyłącz
        if (heater_state && current_temp > target_temp) {
            HEATER_PORT &= ~_BV(HEATER_PIN); // Wyłącz (Low)
            heater_state = 0;
        }
        // Jeśli wyłączona i spadła poniżej T - Th -> Włącz
        else if (!heater_state && current_temp < (target_temp - HYSTERESIS)) {
            HEATER_PORT |= _BV(HEATER_PIN);  // Włącz (High)
            heater_state = 1;
        }

        static uint16_t print_counter = 0;
        if (++print_counter > 10) { // Co ok. 1s przy delay(100ms)
            printf("Temp: %.1f C | Cel: %.1f C | Grzalka: %s\r", 
                   current_temp, target_temp, heater_state ? "ON " : "OFF");
            print_counter = 0;
        }

        _delay_ms(100);
    }
}
