#ifndef OPERATIONS_H
#define OPERATIONS_H

#include <stdint.h>

int8_t add_int8(volatile int8_t a, volatile int8_t b);
int8_t mul_int8(volatile int8_t a, volatile int8_t b);
int8_t div_int8(volatile int8_t a, volatile int8_t b);

int16_t add_int16(volatile int16_t a, volatile int16_t b);
int16_t mul_int16(volatile int16_t a, volatile int16_t b);
int16_t div_int16(volatile int16_t a, volatile int16_t b);

int32_t add_int32(volatile int32_t a, volatile int32_t b);
int32_t mul_int32(volatile int32_t a, volatile int32_t b);
int32_t div_int32(volatile int32_t a, volatile int32_t b);

int64_t add_int64(volatile int64_t a, volatile int64_t b);
int64_t mul_int64(volatile int64_t a, volatile int64_t b);
int64_t div_int64(volatile int64_t a, volatile int64_t b);

float add_float(volatile float a, volatile float b);
float mul_float(volatile float a, volatile float b);
float div_float(volatile float a, volatile float b);

#endif
