#include <avr/io.h>
#include <util/delay.h>

#define BURST_US 600
#define GAP_US 600
#define BURST_COUNT 6
#define FRAME_GAP_MS 100
#define DETECT_HOLD_MS 250

void ir_on(void)
{
    TCCR1A |= (1 << COM1A0); // toggle OC1A
}

void ir_off(void)
{
    TCCR1A &= ~(1 << COM1A0);
    PORTB &= ~(1 << PB1);
}

uint16_t send_and_detect(void)
{
    uint16_t hits = 0;

    for (uint8_t i = 0; i < BURST_COUNT; i++)
    {
        ir_on();
        _delay_us(100);

        // 9 próbek co ~50 us
        for (uint8_t s = 0; s < 9; s++)
        {
            if (!(PINB & (1 << PB0)))
                hits++;
            _delay_us(50);
        }

        ir_off();
        _delay_us(GAP_US);
    }
    return hits;
}

int main(void)
{
    DDRB |= (1 << DDB1) | (1 << DDB2); // PB1 (IR LED), PB2 (wskaźnik)
    DDRB &= ~(1 << DDB0);              // PB0 wejście
    PORTB |= (1 << PB0);               // pull-up
    
    TCCR1B = (1 << WGM12) | (1 << CS10); // CTC, preskaler 1
    OCR1A = 210;                         // ~37.9 kHz
    TCNT1 = 0;

    while (1)
    {
        if (send_and_detect() >= 8)
        {
            PORTB |= (1 << PB2);
            _delay_ms(DETECT_HOLD_MS);
            PORTB &= ~(1 << PB2);
        }
        _delay_ms(FRAME_GAP_MS);
    }
}
