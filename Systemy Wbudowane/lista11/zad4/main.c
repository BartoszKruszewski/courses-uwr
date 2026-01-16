#include <avr/io.h>
#include <util/delay.h>

/* Stałe dla PWM (Timer1) przy F_CPU=16MHz i Prescaler=64 */
/* Częstotliwość 50Hz -> Okres 20ms -> 20ms / (1/(16MHz/64)) = 5000 taktów */
#define PWM_TOP 4999  // (16000000 / 64 / 50) - 1

/* Bezpieczne zakresy impulsów dla serwa (w taktach timera) */
/* 1.0ms = 250 taktów, 1.5ms = 375 taktów, 2.0ms = 500 taktów */
#define SERVO_MIN 275  // ~1.1ms
#define SERVO_MAX 475  // ~1.9ms

void init_pwm_timer1(void) {
    /* Ustawienie pinu PB1 (OC1A) jako wyjście */
    DDRB |= (1 << PB1);

    /* Timer1 w trybie Fast PWM z TOP w rejestrze ICR1 (Mode 14) */
    /* WGM13:0 = 1110, COM1A1:0 = 10 (Clear OC1A on Compare Match) */
    TCCR1A = (1 << COM1A1) | (1 << WGM11);
    TCCR1B = (1 << WGM13) | (1 << WGM12) | (1 << CS11) | (1 << CS10); // Prescaler 64

    /* Ustawienie częstotliwości 50Hz */
    ICR1 = PWM_TOP;
}

void init_adc(void) {
    /* Napięcie odniesienia AVcc, wejście ADC0 (PC0) */
    ADMUX = (1 << REFS0);
    
    /* Włączenie ADC i prescaler 128 (dla F_CPU 16MHz -> 125kHz ADC clock) */
    ADCSRA = (1 << ADEN) | (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);
}

uint16_t read_adc(void) {
    /* Start konwersji */
    ADCSRA |= (1 << ADSC);
    
    /* Oczekiwanie na zakończenie */
    while (ADCSRA & (1 << ADSC));
    
    return ADC;
}

/* Funkcja mapująca zakresy */
long map_value(long x, long in_min, long in_max, long out_min, long out_max) {
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}

int main(void) {
    init_pwm_timer1();
    init_adc();

    while (1) {
        /* Odczyt z potencjometru (0-1023) */
        uint16_t adc_val = read_adc();

        /* Skalowanie odczytu na bezpieczny zakres wychylenia serwa */
        uint16_t pwm_val = map_value(adc_val, 0, 1023, SERVO_MIN, SERVO_MAX);

        /* Ustawienie wypełnienia */
        OCR1A = pwm_val;

        _delay_ms(10);
    }
}
