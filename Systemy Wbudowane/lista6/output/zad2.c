#include <avr/io.h>
#include <stdio.h>
#include <inttypes.h>
#include <avr/interrupt.h>

#define BAUD 9600
#define UBRR_VALUE ((F_CPU)/16/(BAUD)-1) // 103
// UBRR to rejestr, który ustawia prędkość transmisji UART przez określenie dzielnika zegara mikrokontrolera.
// Dzięki niemu UART działa z odpowiednią szybkością (baud rate).

#define BUFFER_SIZE 64

volatile uint8_t tx_buffer[BUFFER_SIZE];
volatile uint8_t tx_head = 0;
volatile uint8_t tx_tail = 0;

volatile uint8_t rx_buffer[BUFFER_SIZE];
volatile uint8_t rx_head = 0;
volatile uint8_t rx_tail = 0;

void uart_init(void) {
    UBRR0 = UBRR_VALUE; // Ustawienie baud rate (str. 198)
    UCSR0B = _BV(RXEN0) | _BV(TXEN0) | _BV(RXCIE0) | _BV(UDRIE0); // Włączenie odbiornika i nadajnika i przerwania odbioru znaku i przerwania UDRE (str. 184 oraz 206)
    UCSR0C = _BV(UCSZ00) | _BV(UCSZ01); // Ustawienie formatu ramki 8 bitów danych, 1 stop-bit (str. 197)
}

// Przerwanie UART - znak odebrany
ISR(USART_RX_vect)
{
  uint8_t data = UDR0;
  uint8_t new_head = (rx_head + 1) % BUFFER_SIZE;
  if (new_head != rx_tail) {  // jeśli bufor nie jest pełny
    rx_buffer[rx_head] = data;
    rx_head = new_head;
  }
  // Jeśli bufor pełny, odebrane dane są ignorowane (można dodać obsługę błędu)
}

// ISR przerwania gotowości do nadawania (UDRE)
ISR(USART_UDRE_vect)
{
  if (tx_head == tx_tail) {
    // Bufor pusty - wyłącz przerwanie UDRE
    UCSR0B &= ~_BV(UDRIE0);
  } else {
    UDR0 = tx_buffer[tx_tail];
    tx_tail = (tx_tail + 1) % BUFFER_SIZE;
  }
}

int uart_transmit(char data, FILE *stream)
{
  uint8_t tmp_head = (tx_head + 1) % BUFFER_SIZE;
  while (tmp_head == tx_tail) {
    // busy wait, program czeka tylko jeśli bufor pełny
  }
  tx_buffer[tx_head] = data;
  tx_head = tmp_head;
  // Włącz przerwanie UDRE, by rozpocząć nadawanie
  UCSR0B |= _BV(UDRIE0);
  return 0;
}

int uart_receive(FILE *stream)
{
  // Czekaj, jeśli bufor pusty
  while (rx_head == rx_tail) { }
  uint8_t data = rx_buffer[rx_tail];
  rx_tail = (rx_tail + 1) % BUFFER_SIZE;
  return data;
}

FILE uart_file;

int main()
{
  uart_init();
  sei(); // globalne zezwolenie na przerwania
  fdev_setup_stream(&uart_file, uart_transmit, uart_receive, _FDEV_SETUP_RW);
  stdin = stdout = stderr = &uart_file;

  int16_t a = 1;
  
  printf("Hello world!\r\n");
  while(1) {
    
    scanf("%" SCNd16, &a);
    printf("Odczytano: %" PRId16 "\r\n", a);
  }
}
