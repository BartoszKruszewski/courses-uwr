#include <avr/io.h>
#include <stdio.h>
#include <stdint.h>
#include "uart.h"

int main(void)
{
    // inicjalizacja UART wraz z przekierowaniami ze wyjsc standardowych
    uart_init();
    uart_stdio_setup();
    stdin = stdout = stderr = &uart_file;

    // int8_t
    {
        int8_t a, b;
        if (scanf("%hhd %hhd", &a, &b) == 2)
        {
            printf(
                "i8 add=%hhd mul=%hhd div=%hhd\n",
                (int8_t)(a + b),
                (int8_t)(a * b),
                (b != 0) ? (int8_t)(a / b) : 0
            );
        }
    }

    // int16_t
    {
        int16_t a, b;
        if (scanf("%hd %hd", &a, &b) == 2)
        {
            printf(
                "i16 add=%hd mul=%hd div=%hd\n",
                (int16_t)(a + b),
                (int16_t)(a * b),
                (b != 0) ? (int16_t)(a / b) : 0
            );
        }
    }

    // int32_t
    {
        int32_t a, b;
        if (scanf("%ld %ld", &a, &b) == 2)
        {
            printf(
                "i32 add=%ld mul=%ld div=%ld\n",
                (a + b),
                (a * b),
                (b != 0) ? (a / b) : 0
            );
        }
    }

    // int64_t: wczytanie jako 32-bit, obliczenia w 64-bit, wypis jako hi:lo
    {
        int32_t a32, b32;
        if (scanf("%ld %ld", &a32, &b32) == 2)
        {
            int64_t a = (int64_t)a32, b = (int64_t)b32;
            int64_t s = a + b;
            int64_t m = a * b;
            int64_t d = (b != 0) ? (a / b) : 0;
            unsigned long s_hi = (unsigned long)((unsigned long long)s >> 32);
            unsigned long s_lo = (unsigned long)((unsigned long long)s & 0xFFFFFFFFu);
            unsigned long m_hi = (unsigned long)((unsigned long long)m >> 32);
            unsigned long m_lo = (unsigned long)((unsigned long long)m & 0xFFFFFFFFu);
            unsigned long d_hi = (unsigned long)((unsigned long long)d >> 32);
            unsigned long d_lo = (unsigned long)((unsigned long long)d & 0xFFFFFFFFu);
            printf(
                "i64 add=0x%08lx:%08lx mul=0x%08lx:%08lx div=0x%08lx:%08lx\n",
                s_hi,
                s_lo,
                m_hi,
                m_lo,
                d_hi,
                d_lo
            );
        }
    }

    // float (wymaga dodatkowych bibliotek do %f)
    {
        float a, b;
        if (scanf("%f %f", &a, &b) == 2)
        {
            printf(
                "f add=%f mul=%f div=%f\n",
                a + b,
                a * b,
                (b != 0.0f) ? (a / b) : 0.0f
            );
        }
    }
}
