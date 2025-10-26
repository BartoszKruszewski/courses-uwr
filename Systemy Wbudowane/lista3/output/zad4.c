#include <avr/io.h>
#include <util/delay.h>
#include <stdio.h>
#include <math.h>
#include "uart.h"
#include "adc.h"

// Parametry termistora
#define R1 4700.0      // Rezystancja dzielnika w omach
#define R0 4700.0      // Rezystancja termistora w 25°C
#define T0 298.15      // Temperatura odniesienia w K (25°C)
#define B_CONST 4000.0 // Stała B termistora (do kalibracji)

float calculate_temperature(uint16_t adc_value)
{
    // Oblicz rezystancję termistora
    float r_ntc = R1 * ((1023.0 / (float)adc_value) - 1.0);

    // Oblicz temperaturę według wzoru Beta
    float inv_t = (1.0 / T0) + (1.0 / B_CONST) * log(r_ntc / R0);
    float temp_k = 1.0 / inv_t;
    float temp_c = temp_k - 273.15;

    return temp_c;
}

int main(void)
{
    uart_init();
    uart_stdio_setup();
    stdout = stdin = &uart_file;

    adc_init(ADC_REF_AVCC, ADC_PRESCALER_128);

    while (1)
    {
        printf("Temp: %.2f C\r\n", calculate_temperature(adc_read(ADC_CHANNEL_0)));
        _delay_ms(1000);
    }

    return 0;
}
