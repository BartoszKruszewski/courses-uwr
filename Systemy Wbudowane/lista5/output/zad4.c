#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/sleep.h>
#include "utils.h"

volatile uint16_t last_capture = 0;
volatile uint16_t diff = 0;
volatile uint8_t new_capture = 0;

ISR(TIMER1_CAPT_vect) {
    uint16_t current = ICR1;
    diff = current - last_capture;
    last_capture = current;
}

void timer1_init(void) {
    TCCR1B = (1 << ICES1) | (1 << CS11); // Wzrostowe zbocze, prescaler 8
    TIMSK1 = (1 << ICIE1); // Włącz przerwanie Input Capture
}

int main(void) {
    uart_init();
    timer1_init();
    sei();
    set_sleep_mode(SLEEP_MODE_IDLE);
    while (1) {
        sleep_mode();
        if (new_capture) {
            float freq = 1.0 / ((diff * 0.0000005)); // dla preskalera 8, zegar 16 MHz
            printf("%f\r\n", freq);
            new_capture = 0;
        }
    }
}
