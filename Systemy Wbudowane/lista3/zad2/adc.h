#ifndef ADC_H
#define ADC_H

#include <avr/io.h>
#include <stdint.h>

#define ADC_CHANNEL_0   0
#define ADC_CHANNEL_1   1
#define ADC_CHANNEL_2   2
#define ADC_CHANNEL_3   3
#define ADC_CHANNEL_4   4
#define ADC_CHANNEL_5   5
#define ADC_CHANNEL_6   6
#define ADC_CHANNEL_7   7

// Napięcie referencyjne
#define ADC_REF_AREF    0
#define ADC_REF_AVCC    1
#define ADC_REF_INTERNAL 3

// Prescaler ADC
#define ADC_PRESCALER_2     1
#define ADC_PRESCALER_4     2
#define ADC_PRESCALER_8     3
#define ADC_PRESCALER_16    4
#define ADC_PRESCALER_32    5
#define ADC_PRESCALER_64    6
#define ADC_PRESCALER_128   7

/**
 * @brief Inicjalizacja ADC
 * @param reference Źródło napięcia referencyjnego (ADC_REF_AREF, ADC_REF_AVCC, ADC_REF_INTERNAL)
 * @param prescaler Prescaler zegara ADC (ADC_PRESCALER_2 do ADC_PRESCALER_128)
 */
void adc_init(uint8_t reference, uint8_t prescaler);

/**
 * @brief Odczyt wartości z wybranego kanału ADC
 * @param channel Numer kanału ADC (0-7)
 * @return Wartość ADC (0-1023)
 */
uint16_t adc_read(uint8_t channel);

/**
 * @brief Odczyt wartości z wybranego kanału ADC z uśrednianiem
 * @param channel Numer kanału ADC (0-7)
 * @param samples Liczba próbek do uśrednienia
 * @return Uśredniona wartość ADC (0-1023)
 */
uint16_t adc_read_average(uint8_t channel, uint8_t samples);

/**
 * @brief Konwersja wartości ADC na napięcie
 * @param adc_value Wartość ADC (0-1023)
 * @param vref Napięcie referencyjne w woltach (np. 5.0)
 * @return Napięcie w woltach
 */
float adc_to_voltage(uint16_t adc_value, float vref);

/**
 * @brief Odczyt surowej wartości ADC z kanału bandgap
 * @return Wartość ADC bandgap (0-1023)
 */
uint16_t adc_read_bandgap(void);

#endif // ADC_H
