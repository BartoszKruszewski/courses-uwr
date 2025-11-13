#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/sleep.h>
#include "utils.h"

typedef struct
{
    uint8_t state;      // 0/1
    uint16_t timestamp; // ms
} ButtonEvent;

#define BUFFER_SIZE 32
volatile ButtonEvent event_buffer[BUFFER_SIZE];
volatile uint8_t buffer_head = 0;
volatile uint8_t buffer_tail = 0;

volatile uint16_t current_time = 0;
volatile uint16_t playback_time = 0;
volatile uint16_t first_event_time = 0;
volatile uint8_t playback_active = 0;

static inline uint8_t buffer_is_full(void)
{
    return ((buffer_head + 1) % BUFFER_SIZE) == buffer_tail;
}

static inline uint8_t buffer_is_empty(void)
{
    return buffer_head == buffer_tail;
}

static inline void buffer_put(uint8_t state, uint16_t timestamp)
{
    if (!buffer_is_full())
    {
        event_buffer[buffer_head].state = state;
        event_buffer[buffer_head].timestamp = timestamp;
        buffer_head = (buffer_head + 1) % BUFFER_SIZE;
    }
}

static inline ButtonEvent buffer_peek(void)
{
    return event_buffer[buffer_tail];
}

static inline void buffer_remove(void)
{
    buffer_tail = (buffer_tail + 1) % BUFFER_SIZE;
}

// ISR - Timer1 Compare Match A (co 1ms)
ISR(TIMER1_COMPA_vect)
{
    static uint8_t last_button_state = 1;
    static uint8_t debounce_counter = 0;

    current_time++;

    uint8_t button_state = digital_read(PIN_D2);

    if (button_state != last_button_state)
    {
        debounce_counter++;
        if (debounce_counter >= 10)
        {
            buffer_put(button_state, current_time);

            if (!playback_active && !buffer_is_empty())
            {
                playback_active = 1;
                first_event_time = current_time;
                playback_time = 0;
            }

            last_button_state = button_state;
            debounce_counter = 0;
        }
    }
    else
    {
        debounce_counter = 0;
    }

    if (playback_active && !buffer_is_empty())
    {
        playback_time++;

        ButtonEvent next_event = buffer_peek();

        uint16_t event_relative_time = next_event.timestamp - first_event_time;
        uint16_t event_playback_time = event_relative_time + 1000;

        if (playback_time >= event_playback_time)
        {
            digital_write(PIN_B5, !next_event.state);
            buffer_remove();

            if (buffer_is_empty())
            {
                playback_active = 0;
                playback_time = 0;
            }
        }
    }
}

void timer1_init(void)
{
    // CTC mode, TOP = OCR1A
    TCCR1A = 0;
    TCCR1B = (1 << WGM12) | (1 << CS11) | (1 << CS10); // CTC, prescaler 64

    // OCR1A dla 1ms przy 16MHz i prescaler 64
    OCR1A = 249;

    // Włączenie przerwania Compare Match A
    TIMSK1 = (1 << OCIE1A);
}

int main(void)
{
    pin_mode(PIN_B5, OUTPUT);
    digital_write(PIN_B5, HIGH);

    pin_mode(PIN_D2, INPUT_PULLUP);

    timer1_init();

    set_sleep_mode(SLEEP_MODE_IDLE);
    sleep_enable();

    sei();

    while (1)
    {
        sleep_mode();
    }

    return 0;
}
