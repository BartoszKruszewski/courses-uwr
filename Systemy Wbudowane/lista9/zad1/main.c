#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/sleep.h>

#define LED_PIN PB2
#define PORT_LED PORTB
#define DDR_LED DDRB

#define BUTTON_PIN PA7
#define PIN_BUTTON PINA
#define PORT_BUTTON PORTA
#define PULLUP_BTN PORTA

#define SAMPLING_INTERVAL_MS 10
#define DELAY_SECONDS 1
#define BUFFER_SIZE (DELAY_SECONDS * 1000 / SAMPLING_INTERVAL_MS)

volatile uint8_t button_buffer[BUFFER_SIZE];
volatile uint8_t buffer_index = 0;

ISR(TIM1_COMPA_vect)
{
  button_buffer[buffer_index] = (PIN_BUTTON & (1 << BUTTON_PIN)) ? 1 : 0;

  if (button_buffer[(buffer_index + 1) % BUFFER_SIZE] == 0)
    PORT_LED |= (1 << LED_PIN);
  else
    PORT_LED &= ~(1 << LED_PIN);

  if (buffer_index++ >= BUFFER_SIZE)
    buffer_index = 0;
}

int main(void)
{
  DDR_LED |= (1 << LED_PIN);
  DDR_LED &= ~(1 << BUTTON_PIN);
  PULLUP_BTN |= (1 << BUTTON_PIN);

  // Chcemy przerwanie co 10ms.
  // Zegar fabryczny ATtiny84 to 1MHz (8MHz / 8).
  // Wzór: F_CPU / Preskaler / Częstotliwość_przerwań - 1
  // 1,000,000 / 64 / 100Hz (czyli 10ms) - 1 = 155.25 -> ~155

  TCCR1B |= (1 << WGM12);              // Tryb CTC
  TCCR1B |= (1 << CS11) | (1 << CS10); // Preskaler 64
  OCR1A = 155;                         // Wartość porównania dla 10ms przy zegarze 1MHz
  TIMSK1 |= (1 << OCIE1A);             // Włącz przerwanie od porównania kanału A

  set_sleep_mode(SLEEP_MODE_IDLE); // Tryb IDLE pozwala działać timerom i przerwaniom

  for (int i = 0; i < BUFFER_SIZE; i++)
    button_buffer[i] = 1;

  sei();

  while (1)
    sleep_mode();
}
