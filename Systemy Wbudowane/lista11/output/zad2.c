#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include "uart.h"

#define F_PWM 1000UL // Częstotliwość PWM: 1 kHz
#define PRESCALER 8

// W trybie Phase/Freq Correct: F_PWM = F_CPU / (2 * N * TOP)
// Zatem: TOP = F_CPU / (2 * N * F_PWM)
#define PWM_TOP (F_CPU / (2 * PRESCALER * F_PWM))

volatile uint16_t adc_sem_raw = 0;     // Pomiar przy wyłączonym (OFF)
volatile uint16_t adc_current_raw = 0; // Pomiar przy włączonym (ON)
volatile uint8_t data_ready = 0;       // Flaga gotowości danych

void timer1_init() {
    // Ustawienie pinu OC1A (PB1) jako wyjście
    DDRB |= _BV(PB1);

    // TCCR1A:
    // COM1A1=1, COM1A0=0 -> Clear OC1A on Compare Match (up-counting), Set on down-counting
    // WGM11=0, WGM10=0 -> Część konfiguracji trybu 8 (Phase and Freq Correct)
    TCCR1A = _BV(COM1A1);

    // TCCR1B:
    // WGM13=1, WGM12=0 -> Dokończenie konfiguracji trybu 8 (TOP = ICR1)
    // CS11=1 -> Prescaler 8
    TCCR1B = _BV(WGM13) | _BV(CS11);

    // Ustalenie częstotliwości (TOP)
    ICR1 = PWM_TOP;

    // Włączenie przerwań:
    // TOIE1 -> Overflow Interrupt (Wywołanie przy liczniku = 0, BOTTOM)
    // ICIE1 -> Input Capture Interrupt (Wywołanie przy liczniku = ICR1, TOP)
    TIMSK1 = _BV(TOIE1) | _BV(ICIE1);
}

void adc_init() {
    // AVCC jako referencja, Pin PC0 (ADC0) jako wejście pomiarowe
    ADMUX = _BV(REFS0); 
    // Włączenie ADC, Prescaler 128 (16MHz/128 = 125kHz zegar ADC)
    ADCSRA = _BV(ADEN) | _BV(ADPS2) | _BV(ADPS1) | _BV(ADPS0);
}

uint16_t adc_read_blocking() {
    ADCSRA |= _BV(ADSC);       // Start konwersji
    while (ADCSRA & _BV(ADSC)); // Czekaj na koniec
    return ADC;
}

/* Przerwanie przy BOTTOM (0) - Środek impulsu HIGH */
/* Tranzystor jest WŁĄCZONY -> Mierzymy Prąd (niskie napięcie) */
ISR(TIMER1_OVF_vect) {
    adc_current_raw = adc_read_blocking(); // Tu mierzymy prąd (ON)
}

/* Przerwanie przy TOP (ICR1) - Środek przerwy LOW */
/* Tranzystor jest WYŁĄCZONY -> Mierzymy SEM (wysokie napięcie) */
ISR(TIMER1_CAPT_vect) {
    adc_sem_raw = adc_read_blocking();     // Tu mierzymy SEM (OFF)
    data_ready = 1;
}


int main(void) {
    uart_init();
    uart_stdio_setup();
    stdin = stdout = &uart_file;

    timer1_init();
    adc_init();

    // Ustawienie stałego wypełnienia na start (np. 50%)
    OCR1A = PWM_TOP / 2; 

    sei();

    printf("Start systemu pomiarowego silnika DC...\n");

    while (1) {
        if (data_ready) {
            data_ready = 0; // Kasowanie flagi

            // Przeliczenie na miliwolty (zakładając Vref=5V)
            uint16_t mv_off = (uint16_t)((adc_sem_raw * 5000UL) / 1024);
            uint16_t mv_on  = (uint16_t)((adc_current_raw * 5000UL) / 1024);

            // Wyświetlenie wyników
            // OFF - SEM (napięcie wysokie, bo tranzystor rozwarty)
            // ON - Prąd (napięcie niskie, spadek na R_DS_on)
            printf("PWM OFF (SEM): %d mV | PWM ON (I): %d mV\n", mv_off, mv_on);

            _delay_ms(200);
        }
    }
}
