#include <avr/io.h>
#include <util/delay.h>
#include <stdio.h>
#include <inttypes.h>
#include "uart.h"
#include "operations.h"

void timer1_init()
{
    // ustaw tryb licznika
    // WGM1  = 0000 -- normal
    // CS1   = 001  -- prescaler 1, więc licznik inkrementuje się z kazdym cyklem procesora
    TCCR1B = _BV(CS10);
}

// Makro do pomiaru czasu
#define MEASURE_TIME(operation, type) \
    do { \
        volatile type val_a = (type)17; \
        volatile type val_b = (type)3; \
        uint16_t start = TCNT1; \
        operation(val_a, val_b); \
        uint16_t end = TCNT1; \
        printf("%s: %u cykli\r\n", #operation, end - start); \
    } while(0) // while jest po to żeby makro działało jak zwykła instrukcja

int main()
{
    uart_init();
    uart_stdio_setup();
    stdin = stdout = stderr = &uart_file;
    timer1_init();
    
    MEASURE_TIME(add_int8, int8_t);
    MEASURE_TIME(mul_int8, int8_t);
    MEASURE_TIME(div_int8, int8_t);
    
    MEASURE_TIME(add_int16, int16_t);
    MEASURE_TIME(mul_int16, int16_t);
    MEASURE_TIME(div_int16, int16_t);
    
    MEASURE_TIME(add_int32, int32_t);
    MEASURE_TIME(mul_int32, int32_t);
    MEASURE_TIME(div_int32, int32_t);
    
    MEASURE_TIME(add_int64, int64_t);
    MEASURE_TIME(mul_int64, int64_t);
    MEASURE_TIME(div_int64, int64_t);
    
    MEASURE_TIME(add_float, float);
    MEASURE_TIME(mul_float, float);
    MEASURE_TIME(div_float, float);
}
