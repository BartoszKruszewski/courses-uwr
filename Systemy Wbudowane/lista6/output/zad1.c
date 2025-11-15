#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/sleep.h>

#define BAUD 9600
#define UBRR_VALUE ((F_CPU)/16/(BAUD)-1) // 103
// UBRR to rejestr, który ustawia prędkość transmisji UART przez określenie dzielnika zegara mikrokontrolera.
// Dzięki niemu UART działa z odpowiednią szybkością (baud rate).

void uart_init(void) {
    UBRR0 = UBRR_VALUE; // Ustawienie baud rate (str. 198)
    UCSR0B = _BV(RXEN0) | _BV(TXEN0) | _BV(RXCIE0); // Włączenie odbiornika i nadajnika i przerwania odbioru znaku (str. 184 oraz 206)
    UCSR0C = _BV(UCSZ00) | _BV(UCSZ01); // Ustawienie formatu ramki 8 bitów danych, 1 stop-bit (str. 197)
}

// Przerwanie UART - znak odebrany
ISR(USART_RX_vect) {
    uint8_t data = UDR0; // Odczyt buforu UART (str. 172)
    while (!(UCSR0A & (1 << UDRE0))); // Czekanie aż nadajnik będzie gotowy na nowy znak (str. 179)
    UDR0 = data; // Wysłanie tego samego znaku (str. 179)
}

int main(void) {
    uart_init();
    sei(); // Globalne włączenie przerwań
    set_sleep_mode(SLEEP_MODE_IDLE); // Ustawienie trybu uśpienia IDLE (str. 38-39)
    while (1) sleep_mode();
}
