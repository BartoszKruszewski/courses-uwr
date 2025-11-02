#ifndef UART_H
#define UART_H

#include <stdio.h>

void uart_init(void);
int uart_transmit(char c, FILE *stream);
int uart_receive(FILE *stream);

extern FILE uart_file;

void uart_stdio_setup(void);

#endif
