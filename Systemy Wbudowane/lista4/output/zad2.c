#include <avr/io.h>
#include <avr/pgmspace.h>
#include <util/delay.h>

#define MIN_LIGHT 40
#define MAX_LIGHT 200

const uint8_t gamma_table[256] PROGMEM = {
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,
    1,   1,   1,   1,   1,   1,   1,   1,   2,   2,   2,   2,   2,   2,   2,   3,
    3,   3,   3,   3,   4,   4,   4,   4,   5,   5,   5,   5,   6,   6,   6,   7,
    7,   7,   8,   8,   8,   9,   9,   9,  10,  10,  11,  11,  11,  12,  12,  13,
   13,  14,  14,  15,  15,  16,  16,  17,  17,  18,  18,  19,  19,  20,  20,  21,
   22,  22,  23,  23,  24,  25,  25,  26,  26,  27,  28,  28,  29,  30,  30,  31,
   32,  33,  33,  34,  35,  35,  36,  37,  38,  38,  39,  40,  41,  42,  42,  43,
   44,  45,  46,  47,  47,  48,  49,  50,  51,  52,  53,  54,  55,  56,  56,  57,
   58,  59,  60,  61,  62,  63,  64,  65,  66,  67,  68,  69,  70,  71,  73,  74,
   75,  76,  77,  78,  79,  80,  81,  82,  84,  85,  86,  87,  88,  89,  91,  92,
   93,  94,  95,  97,  98,  99, 100, 102, 103, 104, 105, 107, 108, 109, 111, 112,
  113, 115, 116, 117, 119, 120, 121, 123, 124, 126, 127, 128, 130, 131, 133, 134,
  136, 137, 139, 140, 142, 143, 145, 146, 148, 149, 151, 152, 154, 155, 157, 159,
  160, 162, 163, 165, 167, 168, 170, 172, 173, 175, 177, 178, 180, 182, 184, 185,
  187, 189, 191, 192, 194, 196, 198, 200, 201, 203, 205, 207, 209, 211, 213, 214,
  216, 218, 220, 222, 224, 226, 228, 230, 232, 234, 236, 238, 240, 242, 244, 246,
};

void adc_init() {
    // AVCC jako referencja, ADC0 jako wejście
    ADMUX = (1<<REFS0);
    
    // Włącz ADC, prescaler 128 (16MHz/128 = 125kHz)
    ADCSRA = (1<<ADEN) | (1<<ADPS2) | (1<<ADPS1) | (1<<ADPS0);
}

uint16_t adc_read() {
    // Rozpocznij konwersję
    ADCSRA |= (1<<ADSC);
    
    // Czekaj na zakończenie
    while(ADCSRA & (1<<ADSC));
    
    return ADC;
}

void pwm_init() {
    // Ustaw pin PB1 (D9) jako wyjście
    DDRB |= (1<<PB1);
    
    // Fast PWM, 8-bit, non-inverted mode na OC1A
    // WGM13:0 = 5 (Fast PWM, 8-bit, TOP=0x00FF)
    // COM1A1:0 = 2 (non-inverted)
    TCCR1A = (1<<COM1A1) | (1<<WGM10);
    TCCR1B = (1<<WGM12) | (1<<CS11);  // Prescaler 8
    
    // Początkowa wartość duty cycle
    OCR1A = 0;
}


int main(void) {
    adc_init();
    pwm_init();
    
    uint16_t adc_value;
    uint8_t normalized;
    
    while(1) {
        adc_value = adc_read();
        normalized = 255 -(adc_value - MIN_LIGHT) * 255 / MAX_LIGHT;
        OCR1A = pgm_read_byte(&gamma_table[normalized]);
        _delay_ms(50);
    }
    
    return 0;
}
