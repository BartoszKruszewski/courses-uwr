#include <avr/io.h>
#include <util/delay.h>
#include <stdint.h>

#define SEG_A (1u << 0)
#define SEG_B (1u << 1)
#define SEG_C (1u << 2)
#define SEG_D (1u << 3)
#define SEG_E (1u << 4)
#define SEG_F (1u << 5)
#define SEG_G (1u << 6)
#define SEG_DP (1u << 7)

#define PATTERN(mask_on) ((uint8_t)(~(mask_on) & 0xFF))

static const uint8_t digits_ca[10] = {
    // 0: A B C D E F
    PATTERN(SEG_A | SEG_B | SEG_C | SEG_D | SEG_E | SEG_F),
    // 1: B C
    PATTERN(SEG_B | SEG_C),
    // 2: A B D E G
    PATTERN(SEG_A | SEG_B | SEG_D | SEG_E | SEG_G),
    // 3: A B C D G
    PATTERN(SEG_A | SEG_B | SEG_C | SEG_D | SEG_G),
    // 4: B C F G
    PATTERN(SEG_B | SEG_C | SEG_F | SEG_G),
    // 5: A C D F G
    PATTERN(SEG_A | SEG_C | SEG_D | SEG_F | SEG_G),
    // 6: A C D E F G
    PATTERN(SEG_A | SEG_C | SEG_D | SEG_E | SEG_F | SEG_G),
    // 7: A B C
    PATTERN(SEG_A | SEG_B | SEG_C),
    // 8: A B C D E F G
    PATTERN(SEG_A | SEG_B | SEG_C | SEG_D | SEG_E | SEG_F | SEG_G),
    // 9: A B C D F G
    PATTERN(SEG_A | SEG_B | SEG_C | SEG_D | SEG_F | SEG_G),
};

int main(void) {
    // PORTD jako wyjścia, wszystko zgaszone
    DDRD  = 0xFF;
    PORTD = 0xFF;

    for (;;) {
        for (uint8_t i = 0; i < 10; ++i) {
            PORTD = digits_ca[i];  // pojedynczy zapis do rejestru portu
            _delay_ms(1000);
        }
    }
}
