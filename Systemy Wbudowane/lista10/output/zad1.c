#include <avr/io.h>
#include <util/delay.h>
#include "hd44780.h"
#include "uart.h"

#define LCD_COLS 16
#define LCD_ROWS 2

volatile uint8_t cursor_x = 0;
volatile uint8_t cursor_y = 0;

char lcd_buffer[LCD_ROWS][LCD_COLS];

void buffer_init(void)
{
    for (uint8_t y = 0; y < LCD_ROWS; y++)
    {
        for (uint8_t x = 0; x < LCD_COLS; x++)
        {
            lcd_buffer[y][x] = ' ';
        }
    }
}

void lcd_scroll(void)
{
    // Kopiuj wiersz 2 do wiersza 1
    for (uint8_t x = 0; x < LCD_COLS; x++)
    {
        lcd_buffer[0][x] = lcd_buffer[1][x];
        lcd_buffer[1][x] = ' ';
    }
    
    // Odśwież wyświetlacz
    LCD_GoTo(0, 0);
    for (uint8_t x = 0; x < LCD_COLS; x++)
    {
        LCD_WriteData(lcd_buffer[0][x]);
    }
    
    LCD_GoTo(0, 1);
    for (uint8_t x = 0; x < LCD_COLS; x++)
    {
        LCD_WriteData(lcd_buffer[1][x]);
    }
    
    // Ustaw kursor na początku drugiego wiersza
    cursor_x = 0;
    cursor_y = 1;
    LCD_GoTo(cursor_x, cursor_y);
}

void lcd_put_char(char c)
{
    if (c == '\n' || c == '\r')
    {
        // Znak nowego wiersza - przewiń wyświetlacz
        lcd_scroll();
    }
    else
    {
        // Zapisz znak do bufora i wyświetl
        lcd_buffer[cursor_y][cursor_x] = c;
        LCD_WriteData(c);
        
        cursor_x++;
        
        // Obsługa przepełnienia wiersza
        if (cursor_x >= LCD_COLS)
        {
            // Przewinięcie jak przy znaku nowego wiersza
            lcd_scroll();
        }
    }
}

void lcd_cursor_on(void)
{
    LCD_WriteCommand(HD44780_DISPLAY_ONOFF | HD44780_DISPLAY_ON | 
                     HD44780_CURSOR_ON | HD44780_CURSOR_BLINK);
}

int main(void)
{
    uart_init();
    LCD_Initialize();
    buffer_init();
    lcd_cursor_on();
    
    // Ustaw pozycję początkową
    LCD_GoTo(0, 0);
    
    char received_char;
    
    while (1)
    {
        // Oczekiwanie na dane z UART
        if (UCSR0A & _BV(RXC0))
        {
            received_char = UDR0;
            lcd_put_char(received_char);
        }
    }
    
    return 0;
}
