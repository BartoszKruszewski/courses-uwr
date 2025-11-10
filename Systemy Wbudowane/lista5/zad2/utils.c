#include "utils.h"

static const uint8_t PROGMEM gamma22_table[16] = {
    0, 72, 99, 119, 136, 151, 164, 175,
    186, 197, 206, 215, 224, 232, 240, 248};

/* ==================== GPIO IMPLEMENTATION ==================== */

void pin_mode(uint8_t pin, uint8_t mode)
{
    volatile uint8_t *ddr, *port;
    uint8_t bit;

    // Map pin to port and bit
    if (pin <= 5)
    {
        ddr = &DDRB;
        port = &PORTB;
        bit = pin;
    }
    else if (pin <= 11)
    {
        ddr = &DDRC;
        port = &PORTC;
        bit = pin - 6;
    }
    else
    {
        ddr = &DDRD;
        port = &PORTD;
        bit = pin - 12;
    }

    if (mode == OUTPUT)
    {
        // DDxn = 1 (Datasheet 14.2.1, page 77)
        *ddr |= (1 << bit);
    }
    else if (mode == INPUT)
    {
        // DDxn = 0, PORTxn = 0 (Datasheet 14.2.1, page 77)
        *ddr &= ~(1 << bit);
        *port &= ~(1 << bit);
    }
    else if (mode == INPUT_PULLUP)
    {
        // DDxn = 0, PORTxn = 1 (Datasheet 14.2.1, page 77)
        *ddr &= ~(1 << bit);
        *port |= (1 << bit);
    }
}

void digital_write(uint8_t pin, uint8_t state)
{
    volatile uint8_t *port;
    uint8_t bit;

    if (pin <= 5)
    {
        port = &PORTB;
        bit = pin;
    }
    else if (pin <= 11)
    {
        port = &PORTC;
        bit = pin - 6;
    }
    else
    {
        port = &PORTD;
        bit = pin - 12;
    }

    if (state == HIGH)
    {
        *port |= (1 << bit);
    }
    else
    {
        *port &= ~(1 << bit);
    }
}

uint8_t digital_read(uint8_t pin)
{
    volatile uint8_t *pinreg;
    uint8_t bit;

    if (pin <= 5)
    {
        pinreg = &PINB;
        bit = pin;
    }
    else if (pin <= 11)
    {
        pinreg = &PINC;
        bit = pin - 6;
    }
    else
    {
        pinreg = &PIND;
        bit = pin - 12;
    }

    return (*pinreg & (1 << bit)) ? HIGH : LOW;
}

uint8_t digital_read_debounced(uint8_t pin)
{
    uint8_t state1 = digital_read(pin);
    _delay_ms(40);
    uint8_t state2 = digital_read(pin);

    if (state1 == state2)
    {
        return state1;
    }

    _delay_ms(40);
    return digital_read(pin);
}

/* ==================== ADC IMPLEMENTATION ==================== */

void adc_init(void)
{
    // ADMUX: REFS0=1 (AVCC ref), ADLAR=0 (right-adj), MUX=0 (ADC0) - Datasheet 23.9.1-2, pages 218-219
    ADMUX = (1 << REFS0);

    // ADCSRA: ADEN=1 (enable), ADPS=7 (prescaler 128) - Datasheet 23.8, page 217
    ADCSRA = (1 << ADEN) | (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);
}

void adc_auto_trigger_init(void) {
    // ADMUX: REFS0=1 (AVCC ref), ADLAR=0 (right-adj), MUX=0 (ADC0) - Datasheet 24.9.1, page 254
    ADMUX = (1 << REFS0);
    
    // ADCSRA: ADEN=1 (enable), ADIE=1 (interrupt enable), ADATE=1 (auto-trigger), ADPS=7 (prescaler 128) - Datasheet 24.9.2, page 255
    ADCSRA = (1 << ADEN) | (1 << ADIE) | (1 << ADATE) |
             (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);
    
    // ADCSRB: ADTS=2 (trigger source INT0) - Datasheet 24.9.4, page 257, Table 24-6
    ADCSRB = (1 << ADTS1);
}

uint16_t adc_read(uint8_t channel)
{
    // Set channel in ADMUX bits 3:0 - Datasheet 23.9.1, page 218
    ADMUX = (ADMUX & 0xF0) | (channel & 0x0F);

    // Set ADSC bit to start conversion - Datasheet 23.8, page 217
    ADCSRA |= (1 << ADSC);

    // Poll ADSC bit, returns 0 when conversion complete - Datasheet 23.8, page 217
    while (ADCSRA & (1 << ADSC))
        ;

    return ADC;
}

/* ==================== PWM IMPLEMENTATION ==================== */

void pwm_init(uint8_t pwm_pin, uint8_t mode)
{
    switch (pwm_pin)
    {
    case PWM_PIN_D6: // Timer0 OC0A (PD6)
        DDRD |= (1 << PD6);
        // COM0A1:0 = 10 (clear on match) - Datasheet 15.9.1, page 105
        TCCR0A |= (1 << COM0A1);

        if (mode == PWM_MODE_FAST)
        {
            // WGM0 = 3 (fast PWM) - Datasheet 15.9.2, page 106
            TCCR0A |= (1 << WGM01) | (1 << WGM00);
            // CS0 = 2 (prescaler 8) - Datasheet 15.9.3, page 110
            TCCR0B = (1 << CS01);
        }
        else if (mode == PWM_MODE_CTC)
        {
            // WGM0 = 2 (CTC mode) - Datasheet 15.9.2, page 106
            TCCR0A |= (1 << WGM01);
            // COM0A1:0 = 01 (toggle on match) - Datasheet 15.9.1, page 105
            TCCR0A &= ~(1 << COM0A1);
            TCCR0A |= (1 << COM0A0);
            TCCR0B = (1 << CS01);
        }
        break;

    case PWM_PIN_D5: // Timer0 OC0B (PD5)
        DDRD |= (1 << PD5);
        // COM0B1:0 = 10 (clear on match) - Datasheet 15.9.1, page 105
        TCCR0A |= (1 << COM0B1);

        if (mode == PWM_MODE_FAST)
        {
            TCCR0A |= (1 << WGM01) | (1 << WGM00);
            TCCR0B = (1 << CS01);
        }
        else if (mode == PWM_MODE_CTC)
        {
            TCCR0A |= (1 << WGM01);
            TCCR0A &= ~(1 << COM0B1);
            TCCR0A |= (1 << COM0B0);
            TCCR0B = (1 << CS01);
        }
        break;

    case PWM_PIN_D3: // Timer2 OC2B (PD3)
        DDRD |= (1 << PD3);
        // COM2B1:0 = 10 (clear on match) - Datasheet 18.9.1, page 156
        TCCR2A |= (1 << COM2B1);

        if (mode == PWM_MODE_FAST)
        {
            // WGM2 = 3 (fast PWM) - Datasheet 18.9.2, page 157
            TCCR2A |= (1 << WGM21) | (1 << WGM20);
            // CS2 = 2 (prescaler 8) - Datasheet 18.9.3, page 161
            TCCR2B = (1 << CS21);
        }
        else if (mode == PWM_MODE_CTC)
        {
            // WGM2 = 2 (CTC mode) - Datasheet 18.9.2, page 157
            TCCR2A |= (1 << WGM21);
            // COM2B1:0 = 01 (toggle on match) - Datasheet 18.9.1, page 156
            TCCR2A &= ~(1 << COM2B1);
            TCCR2A |= (1 << COM2B0);
            TCCR2B = (1 << CS21);
        }
        break;

    case PWM_PIN_B1: // Timer1 OC1A (PB1)
        DDRB |= (1 << PB1);
        // COM1A1:0 = 10 (clear on match) - Datasheet 16.11.1, page 132
        TCCR1A |= (1 << COM1A1);

        if (mode == PWM_MODE_FAST)
        {
            // WGM1 = 14 (fast PWM, 8-bit) - Datasheet 16.11.2, page 134
            TCCR1A |= (1 << WGM10);
            // CS1 = 2 (prescaler 8) - Datasheet 16.11.3, page 139
            TCCR1B = (1 << WGM12) | (1 << CS11);
        }
        else if (mode == PWM_MODE_CTC)
        {
            // WGM1 = 4 (CTC mode) - Datasheet 16.11.2, page 134
            TCCR1B = (1 << WGM12) | (1 << CS11);
            // COM1A1:0 = 01 (toggle on match) - Datasheet 16.11.1, page 132
            TCCR1A &= ~(1 << COM1A1);
            TCCR1A |= (1 << COM1A0);
        }
        break;

    case PWM_PIN_B2: // Timer1 OC1B (PB2)
        DDRB |= (1 << PB2);
        // COM1B1:0 = 10 (clear on match) - Datasheet 16.11.1, page 132
        TCCR1A |= (1 << COM1B1);

        if (mode == PWM_MODE_FAST)
        {
            TCCR1A |= (1 << WGM10);
            TCCR1B = (1 << WGM12) | (1 << CS11);
        }
        else if (mode == PWM_MODE_CTC)
        {
            TCCR1B = (1 << WGM12) | (1 << CS11);
            TCCR1A &= ~(1 << COM1B1);
            TCCR1A |= (1 << COM1B0);
        }
        break;

    case PWM_PIN_B3: // Timer2 OC2A (PB3)
        DDRB |= (1 << PB3);
        // COM2A1:0 = 10 (clear on match) - Datasheet 18.9.1, page 156
        TCCR2A |= (1 << COM2A1);

        if (mode == PWM_MODE_FAST)
        {
            TCCR2A |= (1 << WGM21) | (1 << WGM20);
            TCCR2B = (1 << CS21);
        }
        else if (mode == PWM_MODE_CTC)
        {
            TCCR2A |= (1 << WGM21);
            TCCR2A &= ~(1 << COM2A1);
            TCCR2A |= (1 << COM2A0);
            TCCR2B = (1 << CS21);
        }
        break;
    }
}

void pwm_set(uint8_t pwm_pin, uint8_t value)
{
    switch (pwm_pin)
    {
    case PWM_PIN_D6:
        OCR0A = value; // Datasheet 15.10.3, page 110
        break;
    case PWM_PIN_D5:
        OCR0B = value; // Datasheet 15.10.4, page 110
        break;
    case PWM_PIN_B1:
        OCR1AL = value; // Datasheet 16.12.5, page 140
        break;
    case PWM_PIN_B2:
        OCR1BL = value; // Datasheet 16.12.7, page 140
        break;
    case PWM_PIN_B3:
        OCR2A = value; // Datasheet 18.10.3, page 162
        break;
    case PWM_PIN_D3:
        OCR2B = value; // Datasheet 18.10.4, page 162
        break;
    }
}

/* ==================== GAMMA CORRECTION IMPLEMENTATION ==================== */

uint8_t gamma_correct(uint8_t value)
{
    uint8_t idx = value >> 4;
    uint8_t frac = value & 0x0F;

    uint8_t low = pgm_read_byte(&gamma22_table[idx]);
    uint8_t high = (idx < 15) ? pgm_read_byte(&gamma22_table[idx + 1]) : 255;

    uint8_t result = low + (((high - low) * frac) >> 4);

    return result;
}

/* ==================== UART IMPLEMENTATION ==================== */

#define BAUD 9600
#define UBRR_VALUE ((F_CPU) / 16 / (BAUD) - 1)

FILE uart_file;

void uart_init(void)
{
    UBRR0 = UBRR_VALUE;
    UCSR0A = 0;
    UCSR0B = _BV(RXEN0) | _BV(TXEN0);
    UCSR0C = _BV(UCSZ00) | _BV(UCSZ01);
    fdev_setup_stream(&uart_file, uart_transmit, uart_receive, _FDEV_SETUP_RW);
    stdout = stdin = &uart_file;
}

int uart_transmit(char c, FILE *stream)
{
    if (c == '\n')
    {
        uart_transmit('\r', stream);
    }
    while (!(UCSR0A & _BV(UDRE0)))
        ;
    UDR0 = c;
    return 0;
}

int uart_receive(FILE *stream)
{
    while (!(UCSR0A & _BV(RXC0)))
        ;
    return UDR0;
}
