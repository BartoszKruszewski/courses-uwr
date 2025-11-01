#include "adc.h"
#include <util/delay.h>

void adc_init(uint8_t reference, uint8_t prescaler)
{
    // Ustawienie napięcia referencyjnego
    // REFS1:0 - bity wyboru napięcia referencyjnego
    ADMUX = 0; // Wyzeruj rejestr

    switch (reference)
    {
    case ADC_REF_AREF:
        // AREF, Internal Vref turned off
        ADMUX &= ~((1 << REFS1) | (1 << REFS0));
        break;
    case ADC_REF_AVCC:
        // AVCC with external capacitor at AREF pin
        ADMUX |= (1 << REFS0);
        ADMUX &= ~(1 << REFS1);
        break;
    case ADC_REF_INTERNAL:
        // Internal 1.1V Voltage Reference
        ADMUX |= (1 << REFS1) | (1 << REFS0);
        break;
    default:
        // Domyślnie AVCC
        ADMUX |= (1 << REFS0);
        break;
    }

    // Wyrównanie wyniku w prawo (domyślne)
    ADMUX &= ~(1 << ADLAR);

    // Ustawienie preskalera i włączenie ADC
    ADCSRA = (1 << ADEN); // Włącz ADC

    // Ustaw prescaler
    ADCSRA |= (prescaler & 0x07);

    // Wykonaj dummy read dla stabilizacji
    adc_read(0);
}

uint16_t adc_read(uint8_t channel)
{
    // Wybierz kanał (0-7)
    // Maskowanie aby upewnić się że wartość jest 0-7
    channel &= 0x07;

    // Wyczyść dolne 3 bity ADMUX i ustaw wybrany kanał
    ADMUX = (ADMUX & 0xF8) | channel;

    // Rozpocznij konwersję
    ADCSRA |= (1 << ADSC);

    // Czekaj na zakończenie konwersji
    // ADSC zostanie wyczyszczony automatycznie po zakończeniu
    while (ADCSRA & (1 << ADSC))
        ;

    // Odczytaj i zwróć wartość ADC
    // ADC to 16-bitowy rejestr zawierający wynik
    return ADC;
}

uint16_t adc_read_average(uint8_t channel, uint8_t samples)
{
    uint32_t sum = 0;

    // Wykonaj określoną liczbę pomiarów
    for (uint8_t i = 0; i < samples; i++)
    {
        sum += adc_read(channel);
    }

    // Zwróć średnią wartość
    return (uint16_t)(sum / samples);
}

float adc_to_voltage(uint16_t adc_value, float vref)
{
    // Przelicz wartość ADC (0-1023) na napięcie
    // V = (ADC_value * Vref) / 1024
    return (adc_value * vref) / 1024.0;
}

uint16_t adc_read_bandgap(void)
{
    // Zapisz poprzednią konfigurację ADMUX (tylko referencję)
    uint8_t old_refs = ADMUX & 0xC0;

    // Ustaw AVCC jako referencję i bandgap jako wejście
    // REFS0 = 1 (AVCC), MUX3:0 = 1110 (bandgap)
    ADMUX = (1 << REFS0) | (1 << MUX3) | (1 << MUX2) | (1 << MUX1);

    // Poczekaj na ustabilizowanie się napięcia referencyjnego
    // (bardzo ważne dla pierwszego odczytu bandgap!)
    _delay_ms(2);

    // Wykonaj dummy read (bandgap potrzebuje czasu na stabilizację)
    ADCSRA |= (1 << ADSC);
    while (ADCSRA & (1 << ADSC))
        ;

    // Właściwy pomiar
    ADCSRA |= (1 << ADSC);
    while (ADCSRA & (1 << ADSC))
        ;

    // Odczytaj wynik
    uint16_t result = ADCL;
    result |= ADCH << 8;

    // Przywróć poprzednią konfigurację referencji
    ADMUX = old_refs;

    return result;
}
