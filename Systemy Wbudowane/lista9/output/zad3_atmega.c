#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/twi.h>
#include <stdio.h>
#include "uart.h"

volatile uint8_t received_data;
volatile uint8_t new_data_flag = 0;

ISR(TWI_vect)
{
    // Odczytaj status (maskuj bity prescalera)
    uint8_t status = TWSR & 0xF8;

    switch (status)
    {
    // 0x60: Odebrano własny adres SLA+W, odesłano ACK
    case TW_SR_SLA_ACK:
        // Czekaj na dane, wyślij ACK po odebraniu
        TWCR |= (1 << TWINT) | (1 << TWEA);
        break;

    // 0x80: Odebrano dane, odesłano ACK
    case TW_SR_DATA_ACK:
        received_data = TWDR; // Pobierz dane
        new_data_flag = 1;    // Poinformuj pętlę główną
        // Czekaj na kolejne dane lub STOP
        TWCR |= (1 << TWINT) | (1 << TWEA);
        break;

    // 0xA0: Odebrano STOP lub Repeated START
    case TW_SR_STOP:
        // Zresetuj interfejs do nasłuchu
        TWCR |= (1 << TWINT) | (1 << TWEA);
        break;

    // Inne przypadki (np. błędy)
    default:
        TWCR |= (1 << TWINT) | (1 << TWEA);
        break;
    }
}

int main(void)
{
    uart_init();
    uart_stdio_setup();
    stdout = stdin = &uart_file;

    // Ustawienie adresu (7-bit przesunięte o 1)
    TWAR = (0x7F << 1);
    // Włącz TWI, Przerwania (TWIE), ACK (TWEA) i wyczyść flagę TWINT
    TWCR = (1 << TWEN) | (1 << TWIE) | (1 << TWEA) | (1 << TWINT);

    sei();

    while (1)
    {
        if (new_data_flag)
        {
            printf("%d\r\n", received_data);
            new_data_flag = 0;
        }
    }
}
