/**
 * @file utils.h
 * @brief Driver library for ATmega328P microcontroller
 *
 * This library provides easy-to-use functions for:
 * - GPIO control (digital read/write with debouncing)
 * - ADC (analog-to-digital conversion)
 * - PWM (pulse-width modulation with configurable modes)
 * - Gamma 2.2 correction (compact 16-entry lookup table with interpolation)
 * - UART (serial communication at 9600 baud)
 *
 * @author Bartosz Kruszewski
 * @version 1.0
 */

#ifndef UTILS_H
#define UTILS_H

#include <avr/io.h>
#include <util/delay.h>
#include <avr/pgmspace.h>
#include <stdio.h>

/* ==================== PIN DEFINITIONS ==================== */

#define PIN_B0 0 /**< Port B Pin 0 */
#define PIN_B1 1 /**< Port B Pin 1 - OC1A PWM */
#define PIN_B2 2 /**< Port B Pin 2 - OC1B PWM */
#define PIN_B3 3 /**< Port B Pin 3 - OC2A PWM */
#define PIN_B4 4 /**< Port B Pin 4 */
#define PIN_B5 5 /**< Port B Pin 5 - LED on Arduino Nano */

#define PIN_C0 6  /**< Port C Pin 0 - ADC0 */
#define PIN_C1 7  /**< Port C Pin 1 - ADC1 */
#define PIN_C2 8  /**< Port C Pin 2 - ADC2 */
#define PIN_C3 9  /**< Port C Pin 3 - ADC3 */
#define PIN_C4 10 /**< Port C Pin 4 - ADC4 */
#define PIN_C5 11 /**< Port C Pin 5 - ADC5 */

#define PIN_D0 12 /**< Port D Pin 0 */
#define PIN_D1 13 /**< Port D Pin 1 */
#define PIN_D2 14 /**< Port D Pin 2 */
#define PIN_D3 15 /**< Port D Pin 3 - OC2B PWM */
#define PIN_D4 16 /**< Port D Pin 4 */
#define PIN_D5 17 /**< Port D Pin 5 - OC0B PWM */
#define PIN_D6 18 /**< Port D Pin 6 - OC0A PWM */
#define PIN_D7 19 /**< Port D Pin 7 */

/* ==================== PIN MODES ==================== */

#define OUTPUT 1       /**< Pin configured as output */
#define INPUT 0        /**< Pin configured as input (high impedance) */
#define INPUT_PULLUP 2 /**< Pin configured as input with internal pull-up */

/* ==================== PIN STATES ==================== */

#define HIGH 1 /**< Logic HIGH state (Vcc) */
#define LOW 0  /**< Logic LOW state (GND) */

/* ==================== ADC CHANNELS ==================== */

#define ADC0 0 /**< ADC Channel 0 (Port C Pin 0) */
#define ADC1 1 /**< ADC Channel 1 (Port C Pin 1) */
#define ADC2 2 /**< ADC Channel 2 (Port C Pin 2) */
#define ADC3 3 /**< ADC Channel 3 (Port C Pin 3) */
#define ADC4 4 /**< ADC Channel 4 (Port C Pin 4 - SDA) */
#define ADC5 5 /**< ADC Channel 5 (Port C Pin 5 - SCL) */
#define ADC6 6 /**< ADC Channel 6 (internal) */
#define ADC7 7 /**< ADC Channel 7 (internal) */

/* ==================== PWM PINS ==================== */

#define PWM_PIN_D3 0 /**< PWM on Port D Pin 3 (Timer2 OC2B) */
#define PWM_PIN_D5 1 /**< PWM on Port D Pin 5 (Timer0 OC0B) */
#define PWM_PIN_D6 2 /**< PWM on Port D Pin 6 (Timer0 OC0A) */
#define PWM_PIN_B1 3 /**< PWM on Port B Pin 1 (Timer1 OC1A) */
#define PWM_PIN_B2 4 /**< PWM on Port B Pin 2 (Timer1 OC1B) */
#define PWM_PIN_B3 5 /**< PWM on Port B Pin 3 (Timer2 OC2A) */

/* ==================== PWM MODES ==================== */

#define PWM_MODE_FAST 0 /**< Fast PWM: high frequency (~62kHz for Timer0/2, ~31kHz for Timer1) */
#define PWM_MODE_CTC 2  /**< CTC mode: Clear Timer on Compare (frequency output, 50% duty cycle) */

/* ==================== GPIO FUNCTIONS ==================== */

/**
 * @brief Configure pin mode
 *
 * @param pin Pin number (0-19, see PIN_* definitions)
 * @param mode Pin mode: OUTPUT, INPUT, or INPUT_PULLUP
 */
void pin_mode(uint8_t pin, uint8_t mode);

/**
 * @brief Write digital value to pin
 *
 * @param pin Pin number (0-19)
 * @param state Desired state: HIGH or LOW
 */
void digital_write(uint8_t pin, uint8_t state);

/**
 * @brief Read digital value from pin
 *
 * @param pin Pin number (0-19)
 * @return Current state: HIGH or LOW
 */
uint8_t digital_read(uint8_t pin);

/**
 * @brief Read digital value from pin with debouncing
 *
 * Performs two consecutive reads separated by a 40ms delay to filter out noise
 * and contact bouncing from mechanical switches.
 *
 * @param pin Pin number (0-19)
 * @return Stable state: HIGH or LOW
 */
uint8_t digital_read_debounced(uint8_t pin);

/* ==================== ADC FUNCTIONS ==================== */

/**
 * @brief Initialize analog-to-digital converter
 *
 * Configures ADC with AVCC as voltage reference and prescaler 128.
 * - ADC clock frequency: 16MHz / 128 = 125kHz
 */
void adc_init(void);

/**
 * @brief Initialize ADC with auto-trigger on External Interrupt 0
 * 
 * Configures ADC with automatic triggering from INT0 (External Interrupt 0).
 * 
 * Configures ADC with AVCC as voltage reference and prescaler 128.
 * - ADC clock frequency: 16MHz / 128 = 125kHz
 */
void adc_auto_trigger_init(void);

/**
 * @brief Read raw 10-bit value from ADC channel
 *
 * Performs single blocking conversion on specified channel.
 *
 * @param channel ADC channel number (0-7, see ADC_* definitions)
 * @return Raw ADC value (0-1023)
 */
uint16_t adc_read(uint8_t channel);

/* ==================== PWM FUNCTIONS ==================== */

/**
 * @brief Initialize PWM on specified pin with selected mode
 *
 * Configures timer and sets up PWM output.
 *
 * Available modes:
 * - PWM_MODE_FAST: High frequency (~62kHz Timer0/2, ~31kHz Timer1)
 * - PWM_MODE_CTC: Clear Timer on Compare (frequency output only)
 *
 * @param pwm_pin PWM pin number (0-5, see PWM_PIN_* definitions)
 * @param mode PWM mode: PWM_MODE_FAST, or PWM_MODE_CTC
 */
void pwm_init(uint8_t pwm_pin, uint8_t mode);

/**
 * @brief Set PWM duty cycle or CTC frequency
 *
 * For Fast PWM mode: Sets duty cycle (0-255, where 0=0% and 255=100%)
 * For CTC mode: Sets frequency divider (frequency = F_CPU / (2 * Prescaler * (value+1)))
 *
 * @param pwm_pin PWM pin number (0-5)
 * @param value Duty cycle (0-255) or frequency divider (CTC mode)
 */
void pwm_set(uint8_t pwm_pin, uint8_t value);

/* ==================== GAMMA CORRECTION FUNCTION ==================== */

/**
 * @brief Apply gamma 2.2 correction to 8-bit value
 *
 * Uses compact 16-entry lookup table with linear interpolation.
 * Corrects for human perception of LED brightness (non-linear).
 *
 * @param value Input value (0-255)
 * @return Gamma-corrected output value (0-255)
 */
uint8_t gamma_correct(uint8_t value);

/* ==================== UART FUNCTIONS ==================== */

void uart_init(void);
int uart_transmit(char c, FILE *stream);
int uart_receive(FILE *stream);

extern FILE uart_file;

#endif // UTILS_H
