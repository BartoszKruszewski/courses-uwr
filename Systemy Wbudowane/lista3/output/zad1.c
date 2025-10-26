#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/pgmspace.h>
#include <util/delay.h>

#define NOTE_AS2 117
#define NOTE_B2 123
#define NOTE_C3 131
#define NOTE_D3 147
#define NOTE_F3 175
#define NOTE_G3 196
#define NOTE_GS3 208
#define NOTE_A3 220
#define NOTE_AS3 233
#define NOTE_B3 247
#define NOTE_C4 262
#define NOTE_D4 294
#define NOTE_DS4 311
#define NOTE_E4 330
#define NOTE_F4 349
#define NOTE_G4 392
#define NOTE_GS4 415
#define NOTE_A4 440
#define NOTE_AS4 466
#define NOTE_B4 494
#define NOTE_C5 523
#define NOTE_D5 587
#define NOTE_E5 659
#define NOTE_F5 698
#define NOTE_G5 784
#define NOTE_A5 880
#define NOTE_B5 988

#define END 0
#define PAUSE 1

#define NOTE_LEN 60000UL * 4 // Długość całej nuty

// Format: częstotliwość, długość (4=ćwierćnuta, 8=ósemka, 2=półnuta)
const uint16_t melody[] PROGMEM = {
    NOTE_D3, 16, NOTE_D3, 16, NOTE_D4, 8, NOTE_A3, 6,
    PAUSE, 32, NOTE_GS3, 8, NOTE_G3, 8, NOTE_F3, 8,
    NOTE_D3, 16, NOTE_F3, 16, NOTE_G3, 16,

    NOTE_C3, 16, NOTE_C3, 16, NOTE_D4, 8, NOTE_A3, 6,
    PAUSE, 32, NOTE_GS3, 8, NOTE_G3, 8, NOTE_F3, 8,
    NOTE_D3, 16, NOTE_F3, 16, NOTE_G3, 16,

    NOTE_B2, 16, NOTE_B2, 16, NOTE_D4, 8, NOTE_A3, 6,
    PAUSE, 32, NOTE_GS3, 8, NOTE_G3, 8, NOTE_F3, 8,
    NOTE_D3, 16, NOTE_F3, 16, NOTE_G3, 16,

    NOTE_AS2, 16, NOTE_AS2, 16, NOTE_D4, 8, NOTE_A3, 6,
    PAUSE, 32, NOTE_GS3, 8, NOTE_G3, 8, NOTE_F3, 8,
    NOTE_D3, 16, NOTE_F3, 16, NOTE_G3, 16,

    NOTE_D4, 8, NOTE_D4, 8, NOTE_D4, 8, NOTE_A4, 4,
    NOTE_GS4, 8, NOTE_G4, 8, NOTE_F4, 8,
    NOTE_D4, 16, NOTE_F4, 16, NOTE_G4, 16,

    NOTE_C4, 8, NOTE_C4, 8, NOTE_D4, 8, NOTE_A4, 4,
    NOTE_GS4, 8, NOTE_G4, 8, NOTE_F4, 8,
    NOTE_D4, 16, NOTE_F4, 16, NOTE_G4, 16,

    NOTE_B3, 8, NOTE_B3, 8, NOTE_D4, 8, NOTE_A4, 4,
    NOTE_GS4, 8, NOTE_G4, 8, NOTE_F4, 8,
    NOTE_D4, 16, NOTE_F4, 16, NOTE_G4, 16,

    NOTE_AS3, 8, NOTE_AS3, 8, NOTE_D4, 8, NOTE_A4, 4,
    NOTE_GS4, 8, NOTE_G4, 8, NOTE_F4, 8,
    NOTE_D4, 16, NOTE_F4, 16, NOTE_G4, 16,

    NOTE_D3, 16, NOTE_D3, 16, NOTE_D4, 8, NOTE_A3, 6,
    PAUSE, 32, NOTE_GS3, 8, NOTE_G3, 8, NOTE_F3, 8,
    NOTE_D3, 16, NOTE_F3, 16, NOTE_G3, 16,

    NOTE_C3, 16, NOTE_C3, 16, NOTE_D4, 8, NOTE_A3, 6,
    PAUSE, 32, NOTE_GS3, 8, NOTE_G3, 8, NOTE_F3, 8,
    NOTE_D3, 16, NOTE_F3, 16, NOTE_G3, 16,

    END};

volatile uint32_t tone_counter = 0;

void timer1_init_pwm(uint16_t frequency)
{
    if (frequency == 0)
    {
        // Pauza - wyłącz PWM
        TCCR1A = 0;
        TCCR1B = 0;
        return;
    }

    // Tryb CTC z przełączaniem OC1A, prescaler=64
    TCCR1A = (1 << COM1A0);
    TCCR1B = (1 << WGM12) | (1 << CS11); // prescaler = 8

    // OCR1A = F_CPU / (2 * 64 * frequency) - 1
    OCR1A = (F_CPU / (16UL * frequency)) - 1;
}

void delay_ms(uint16_t ms)
{
    while (ms-- > 0)
        _delay_ms(1);
}

void play_tone(uint16_t frequency, uint16_t duration_ms)
{
    timer1_init_pwm(frequency);
    delay_ms(duration_ms);
    timer1_init_pwm(0); // Wyłącz dźwięk
}

void play_melody(const uint16_t *melody_data, uint16_t tempo)
{
    uint16_t note, duration;
    uint16_t index = 0;
    uint16_t whole_note = NOTE_LEN / tempo; // Długość całej nuty w ms

    while (1)
    {
        note = pgm_read_word(&melody_data[index++]);
        if (note == END)
            break; // Koniec melodii

        duration = pgm_read_word(&melody_data[index++]);

        uint16_t note_duration = whole_note / duration;
        uint16_t pause_duration = note_duration / 10; // 10% pauza
        uint16_t tone_duration = note_duration - pause_duration;

        if (note == PAUSE)
            delay_ms(tone_duration);
        else
            play_tone(note, tone_duration);

        delay_ms(pause_duration);
    }
}

int main(void)
{
    // Skonfiguruj PB1 jako wyjście
    DDRB |= (1 << PB1);

    play_melody(melody, 120);

    // Wyłącz timer po zakończeniu
    TCCR1A = 0;
    TCCR1B = 0;

    return 0;
}
