#include "utils.h"
#include <avr/interrupt.h>
#include <avr/sleep.h>
#include <string.h>

#define SAMPLES 64

volatile uint16_t adc_result = 0;
volatile uint8_t adc_done = 0;

uint16_t adc_read_noise_reduction(uint8_t channel) {
    adc_done = 0;

    // Ustaw kanał na 1.1V wbudowane (0b1110), referencja AVCC (ADMUX już ustawiony przez adc_init)
    ADMUX = (ADMUX & 0xF0) | (channel & 0x0F);
    ADCSRA |= (1 << ADIE); // ADC Interrupt Enable
    ADCSRA |= (1 << ADSC); // Start conversion

    set_sleep_mode(SLEEP_MODE_ADC);
    sleep_enable();
    sei();
    sleep_cpu();
    sleep_disable();
    cli();
    ADCSRA &= ~(1 << ADIE);

    return adc_result;
}

// ISR ADC_vect: zapis wyniku, oznacz zakończenie
ISR(ADC_vect) {
    adc_result = ADC;
    adc_done = 1;
}

float calc_variance(const uint16_t *buf, uint8_t n) {
    float mean = 0.0f, sum2 = 0.0f;
    for(uint8_t i = 0; i < n; ++i) {
        mean += buf[i];
    }
    mean /= n;
    for(uint8_t i = 0; i < n; ++i) {
        float d = buf[i] - mean;
        sum2 += d * d;
    }
    return sum2 / n;
}

int main(void) {
    uart_init();
    adc_init();

    uint16_t poll_samples[SAMPLES];
    uint16_t nr_samples[SAMPLES];

    printf("Polling:\n");
    // dummy read
    adc_read(0b1110); 
    _delay_ms(10);

    for(uint8_t i=0; i < SAMPLES; ++i) {
        // Pomiar kanału 0b1110 – wbudowane 1.1V Referencja
        poll_samples[i] = adc_read(0b1110);
        printf("%u ", poll_samples[i]);
        _delay_ms(10);
    }
    printf("\n");

    printf("Noise Reduction:\n");

    adc_read_noise_reduction(0b1110);
    _delay_ms(10);

    for(uint8_t i=0; i < SAMPLES; ++i) {
        nr_samples[i] = adc_read_noise_reduction(0b1110);
        printf("%u ", nr_samples[i]);
        _delay_ms(10);
    }
    printf("\n");

    printf("Variance polling: %f\n", calc_variance(poll_samples, SAMPLES));
    printf("Variance noise reduction: %f\n", calc_variance(nr_samples, SAMPLES));

    while(1) {}
}
