#include <avr/io.h>
#include <util/delay.h>

#define MOTOR_PWM_PIN    PB1
#define MOTOR_PWM_PORT   PORTB
#define MOTOR_PWM_DDR    DDRB

#define MOTOR_DIR_A_PIN  PD2
#define MOTOR_DIR_B_PIN  PD3
#define MOTOR_DIR_PORT   PORTD
#define MOTOR_DIR_DDR    DDRD

#define POT_ADC_CHANNEL  0

#define ADC_CENTER       512
#define DEADBAND         20    // Margines błędu na środku potencjometru

void ADC_Init() {
    // Napięcie odniesienia AVCC, wyrównanie do prawej
    ADMUX = (1 << REFS0);
    // Włączenie ADC, Prescaler 128 (16MHz/128 = 125kHz)
    ADCSRA = (1 << ADEN) | (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);
}

uint16_t ADC_Read(uint8_t channel) {
    ADMUX = (ADMUX & 0xF0) | (channel & 0x0F);
    ADCSRA |= (1 << ADSC);
    while (ADCSRA & (1 << ADSC));
    return ADC;
}

void PWM_Init() {
    // Ustawienie pinu OC1A (PB1) jako wyjście
    MOTOR_PWM_DDR |= (1 << MOTOR_PWM_PIN);
    
    // Konfiguracja Timera1: Fast PWM 8-bit
    // WGM12 | WGM10 -> Tryb 5 (Fast PWM, 8-bit)
    // COM1A1 -> Clear OC1A on Compare Match (non-inverting mode)
    TCCR1A = (1 << COM1A1) | (1 << WGM10);
    
    // Prescaler 64
    // WGM12 jest w rejestrze TCCR1B
    TCCR1B = (1 << WGM12) | (1 << CS11) | (1 << CS10);
}

void Motor_SetSpeed(uint8_t speed) {
    // W trybie 8-bitowym Fast PWM, rejestr OCR1A przyjmuje wartości 0-255
    OCR1A = speed; 
}

void Motor_Stop() {
    MOTOR_DIR_PORT &= ~((1 << MOTOR_DIR_A_PIN) | (1 << MOTOR_DIR_B_PIN)); 
    Motor_SetSpeed(0);
}

void Motor_Forward(uint8_t speed) {
    MOTOR_DIR_PORT |= (1 << MOTOR_DIR_A_PIN);  // 1A High
    MOTOR_DIR_PORT &= ~(1 << MOTOR_DIR_B_PIN); // 2A Low
    Motor_SetSpeed(speed);
}

void Motor_Reverse(uint8_t speed) {
    MOTOR_DIR_PORT &= ~(1 << MOTOR_DIR_A_PIN); // 1A Low
    MOTOR_DIR_PORT |= (1 << MOTOR_DIR_B_PIN);  // 2A High
    Motor_SetSpeed(speed);
}

int main(void) {
    MOTOR_DIR_DDR |= (1 << MOTOR_DIR_A_PIN) | (1 << MOTOR_DIR_B_PIN);
    
    ADC_Init();
    PWM_Init();

    while (1) {
        uint16_t adc_val = ADC_Read(POT_ADC_CHANNEL);
        uint16_t speed_calc = 0;

        if (adc_val > (ADC_CENTER + DEADBAND)) {
            // Ruch w jedną stronę
            speed_calc = (adc_val - (ADC_CENTER + DEADBAND)) * 255UL / (512 - DEADBAND);
            if (speed_calc > 255) speed_calc = 255;
            Motor_Forward((uint8_t)speed_calc);
        } 
        else if (adc_val < (ADC_CENTER - DEADBAND)) {
            // Ruch w drugą stronę
            speed_calc = ((ADC_CENTER - DEADBAND) - adc_val) * 255UL / (ADC_CENTER - DEADBAND);
            if (speed_calc > 255) speed_calc = 255;
            Motor_Reverse((uint8_t)speed_calc);
        } 
        else {
            // Stop (środek)
            Motor_Stop();
        }
        
        _delay_ms(10);
    }
}
