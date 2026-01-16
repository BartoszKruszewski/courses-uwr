#include <avr/io.h>
#include <util/delay.h>

#define F_PWM 1000UL // Docelowa częstotliwość PWM: 1 kHz
#define PRESCALER 8
// Obliczenie wartości TOP dla Timera1 (ICR1)
#define PWM_TOP ((F_CPU / (PRESCALER * F_PWM)) - 1)

void PWM_Init() {
    // Ustawienie pinu OC1A (PB1) jako wyjście
    DDRB |= (1 << PB1);

    // Konfiguracja Timer1: Fast PWM, Mode 14 (TOP = ICR1)
    // Clear OC1A on Compare Match (non-inverting mode)
    TCCR1A |= (1 << COM1A1) | (1 << WGM11);
    TCCR1B |= (1 << WGM13) | (1 << WGM12);

    // Ustawienie częstotliwości PWM (TOP)
    ICR1 = PWM_TOP; // Dla 1kHz i preskalera 8 -> 1999

    // Ustawienie preskalera na 8 i start timera
    TCCR1B |= (1 << CS11);
}

void ADC_Init() {
    // Napięcie odniesienia AVCC, wejście ADC0 (PC0)
    ADMUX |= (1 << REFS0);
    
    // Włączenie ADC, Prescaler 128 (16MHz/128 = 125kHz)
    ADCSRA |= (1 << ADEN) | (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);
}

uint16_t ADC_Read() {
    // Start konwersji
    ADCSRA |= (1 << ADSC);
    // Czekaj na zakończenie (flaga ADSC zmieni się na 0)
    while (ADCSRA & (1 << ADSC));
    return ADC;
}

int main(void) {
    PWM_Init();
    ADC_Init();

    while (1) {
        uint16_t potValue = ADC_Read();
        // ADC (0-1023) musimy przeskalować na zakres licznika (0-ICR1, czyli 0-1999)
        uint32_t pwmValue = ((uint32_t)potValue * PWM_TOP) / 1023;
        // Aktualizacja wypełnienia
        OCR1A = (uint16_t)pwmValue;
        _delay_ms(10);
    }
}
