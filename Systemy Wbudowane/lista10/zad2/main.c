#include <avr/io.h>
#include <util/delay.h>
#include "hd44780.h"

#define HD44780_CGRAM_SET 0x40
#define PROGRESS_MAX 80

// Tablica definicji własnych znaków (5 znaków po 8 bajtów każdy)
// Każdy znak to kolejny stopień wypełnienia od lewej do prawej
const uint8_t ProgressBarChars[5][8] = {
    {0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10}, // 1 linia (0b10000)
    {0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18}, // 2 linie (0b11000)
    {0x1C, 0x1C, 0x1C, 0x1C, 0x1C, 0x1C, 0x1C, 0x1C}, // 3 linie (0b11100)
    {0x1E, 0x1E, 0x1E, 0x1E, 0x1E, 0x1E, 0x1E, 0x1E}, // 4 linie (0b11110)
    {0x1F, 0x1F, 0x1F, 0x1F, 0x1F, 0x1F, 0x1F, 0x1F}  // 5 linii (0b11111)
};

void LCD_LoadProgressBarPatterns(void) {
    uint8_t i, j;
    
    // Ustawiamy adres na początek pamięci CGRAM (znak o kodzie 0)
    LCD_WriteCommand(HD44780_CGRAM_SET); 
    
    for (i = 0; i < 5; i++) {
        for (j = 0; j < 8; j++) {
            LCD_WriteData(ProgressBarChars[i][j]);
        }
    }
}

void LCD_ShowProgressBar(uint8_t value) {
    if (value > PROGRESS_MAX) value = PROGRESS_MAX;

    uint8_t full_blocks = value / 5;
    uint8_t partial_block = value % 5;

    // Ustawienie kursora na początek drugiego wiersza
    LCD_GoTo(0, 1);

    for (uint8_t i = 0; i < 16; i++) {
        if (i < full_blocks) {
            // Rysuj pełny blok (nasz znak nr 4)
            LCD_WriteData(4); 
        } 
        else if (i == full_blocks) {
            // Rysuj blok częściowy
            if (partial_block > 0) {
                // partial_block wynosi 1..4. 
                // Nasze znaki są indeksowane 0..3 (dla 1..4 linii)
                // Więc wysyłamy kod: partial_block - 1
                LCD_WriteData(partial_block - 1);
            } else {
                // Jeśli reszta to 0, wyświetl spację
                LCD_WriteData(' ');
            }
        } 
        else {
            // Rysuj puste miejsce (spacja)
            LCD_WriteData(' ');
        }
    }
}

int main(void) {
    LCD_Initialize();
    LCD_LoadProgressBarPatterns();
    
    LCD_Clear();
    LCD_GoTo(0, 0);
    LCD_WriteText("Loading...");

    uint8_t progress = 0;

    while (1) {
        LCD_ShowProgressBar(progress);

        if (progress++ > PROGRESS_MAX) {
            progress = 0;
        }

        _delay_ms(50);
    }
    
    return 0;
}
