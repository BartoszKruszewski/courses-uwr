#include <avr/io.h>
#include <util/delay.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <inttypes.h>
#include "uart.h"

#define LED PB5
#define LED_DDR DDRB
#define LED_PORT PORTB

#define UNIT_MS 120u

static inline void led_on(void) { LED_PORT |= _BV(LED); }
static inline void led_off(void) { LED_PORT &= ~_BV(LED); }

static const char *encode_char(char c)
{
  switch (toupper(c))
  {
  case 'A':
    return ".-";
  case 'B':
    return "-...";
  case 'C':
    return "-.-.";
  case 'D':
    return "-..";
  case 'E':
    return ".";
  case 'F':
    return "..-.";
  case 'G':
    return "--.";
  case 'H':
    return "....";
  case 'I':
    return "..";
  case 'J':
    return ".---";
  case 'K':
    return "-.-";
  case 'L':
    return ".-..";
  case 'M':
    return "--";
  case 'N':
    return "-.";
  case 'O':
    return "---";
  case 'P':
    return ".--.";
  case 'Q':
    return "--.-";
  case 'R':
    return ".-.";
  case 'S':
    return "...";
  case 'T':
    return "-";
  case 'U':
    return "..-";
  case 'V':
    return "...-";
  case 'W':
    return ".--";
  case 'X':
    return "-..-";
  case 'Y':
    return "-.--";
  case 'Z':
    return "--..";
  case '0':
    return "-----";
  case '1':
    return ".----";
  case '2':
    return "..---";
  case '3':
    return "...--";
  case '4':
    return "....-";
  case '5':
    return ".....";
  case '6':
    return "-....";
  case '7':
    return "--...";
  case '8':
    return "---..";
  case '9':
    return "----.";
  default:
    return NULL;
  }
}

static void blink_symbol(char s)
{
  led_on();
  if (s == '.')
  {
    _delay_ms(UNIT_MS);
  }
  else
  {
    _delay_ms(3 * UNIT_MS);
  }
  led_off();
}

static void blink_char(char c)
{
  const char *code = encode_char(c);
  size_t n = strlen(code);
  for (size_t i = 0; i < n; ++i)
  {
    blink_symbol(code[i]);
    _delay_ms(UNIT_MS);
  }
  // przerwa pomiedzy znakami
  _delay_ms(3 * UNIT_MS);
}

int main(void)
{
  // ustawienie pinu z wbudowanym LED jako output
  LED_DDR |= _BV(LED);

  // inicjalizacja UART wraz z przekierowaniami ze wyjsc standardowych
  uart_init();
  uart_stdio_setup();
  stdin = stdout = stderr = &uart_file;

  while (1)
  {
    blink_char(getchar());
  }
}
