#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include "utils.h"

#define R_SERIES 10000 // 10kOhm

volatile uint16_t last_adc_value = 0;

ISR(ADC_vect)
{
    last_adc_value = ADC;
}

// Przy ADC Auto Trigger nie musimy tu nic robić
ISR(INT0_vect)
{
    // Przerwanie INT0 automatycznie wyzwala ADC
}

uint32_t calculate_resistance(uint16_t adc_value)
{
    // R_photo = R_series * adc_value / (1023 - adc_value)

    if (adc_value >= 1023)
    {
        return 0xFFFFFFFF; // Nieskończona rezystancja
    }

    if (adc_value == 0)
    {
        return 0; // Zwarcie
    }

    uint32_t resistance = ((uint32_t)R_SERIES * adc_value) / (1023 - adc_value);
    return resistance;
}

int main(void)
{
    uart_init();
    adc_init();
    pin_mode(PIN_D2, INPUT_PULLUP);

    // Konfiguracja przerwania zewnętrznego INT0
    // Wyzwalanie na zbocze opadające
    EICRA = (1 << ISC01); // ISC01=1, ISC00=0 - falling edge (high->low)
    EIMSK = (1 << INT0);  // Włącz przerwanie INT0

    adc_auto_trigger_init();

    sei();

    while (1)
    {
        printf("ADC: %u | Rezystancja: %lu Ohm\n", last_adc_value, calculate_resistance(last_adc_value));
        _delay_ms(1000);
    }

    return 0;
}
