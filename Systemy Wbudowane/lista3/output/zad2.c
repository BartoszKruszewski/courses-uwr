#include <avr/io.h>
#include <util/delay.h>
#include <stdio.h>
#include "uart.h"
#include "adc.h"

#define LED_DDR DDRD
#define LED_PORT PORTD
#define LED_PIN PD6

float calculate_vcc(uint16_t adc_value)
{
    // VCC = 1.1V * 1023 / ADC_value
    // Używamy 1126400 = 1100mV * 1023 dla obliczeń w miliwoltach
    uint32_t vcc_mv = 1126400UL / adc_value;
    return vcc_mv / 1000.0;
}

int main(void)
{
    uart_init();
    uart_stdio_setup();
    stdout = stdin = &uart_file;

    // Konfiguracja pinu LED jako wyjście
    LED_DDR |= _BV(LED_PIN);

    adc_init(ADC_REF_AVCC, ADC_PRESCALER_128);

    while (1)
    {
        // Pomiar z LED zgaszonym
        LED_PORT &= ~_BV(LED_PIN);
        _delay_ms(500);

        uint16_t adc_off = adc_read_bandgap();
        float vcc_off = calculate_vcc(adc_off);

        printf("LED OFF: ADC=%4u, VCC=%.3f V\n", adc_off, vcc_off);

        // Zapalenie LED
        LED_PORT |= _BV(LED_PIN);
        _delay_ms(500);

        // Pomiar z LED zapalonym
        uint16_t adc_on = adc_read_bandgap();
        float vcc_on = calculate_vcc(adc_on);

        printf("LED ON:  ADC=%4u, VCC=%.3f V", adc_on, vcc_on);

        // Obliczenie i wyświetlenie różnicy
        printf(" (roznica: %.3f V)\n\n", vcc_off - vcc_on);
    }

    return 0;
}
