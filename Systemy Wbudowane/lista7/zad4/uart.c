#include <avr/io.h>
#include <stdio.h>
#include "uart.h"

#define BAUD 9600
#define UBRR_VALUE ((F_CPU) / 16 / (BAUD) - 1)

FILE uart_file;

void uart_init(void)
{
  UBRR0 = UBRR_VALUE;
  UCSR0A = 0;
  UCSR0B = _BV(RXEN0) | _BV(TXEN0);
  UCSR0C = _BV(UCSZ00) | _BV(UCSZ01);
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

void uart_stdio_setup(void)
{
  fdev_setup_stream(&uart_file, uart_transmit, uart_receive, _FDEV_SETUP_RW);
}
