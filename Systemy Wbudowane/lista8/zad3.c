#include <avr/io.h>
#include <avr/interrupt.h>
#include <stdio.h>
#include <stdlib.h>

#include "FreeRTOS.h"
#include "task.h"
#include "queue.h"

#define BAUD 9600
#define UBRR_VAL ((F_CPU / 16 / BAUD) - 1)
#define LED_PIN PB1

void vTaskTerminal(void *pvParameters);
void vTaskLed(void *pvParameters);
void vApplicationIdleHook(void);

QueueHandle_t xRxQueue;
QueueHandle_t xTxQueue;

int uart_putchar(char c, FILE *stream);
int uart_getchar(FILE *stream);
void uart_init(void);

FILE uart_str = FDEV_SETUP_STREAM(uart_putchar, uart_getchar, _FDEV_SETUP_RW);

ISR(USART_RX_vect)
{
    uint8_t data = UDR0;
    BaseType_t xHigherPriorityTaskWoken = pdFALSE;

    xQueueSendFromISR(xRxQueue, &data, &xHigherPriorityTaskWoken);
    if (xHigherPriorityTaskWoken)
        taskYIELD();
}

ISR(USART_UDRE_vect)
{
    uint8_t data;
    BaseType_t xHigherPriorityTaskWoken = pdFALSE;

    if (xQueueReceiveFromISR(xTxQueue, &data, &xHigherPriorityTaskWoken) == pdTRUE)
        UDR0 = data;
    else
        UCSR0B &= ~(1 << UDRIE0);

    if (xHigherPriorityTaskWoken)
        taskYIELD();
}

void uart_init(void)
{
    // Ustawienie prędkości transmisji
    UBRR0H = (uint8_t)(UBRR_VAL >> 8);
    UBRR0L = (uint8_t)(UBRR_VAL);

    // Włączenie odbiornika i nadajnika, włączenie przerwania od odbioru (RXCIE)
    // Przerwanie od pustego rejestru (UDRIE) włączamy tylko gdy mamy dane do wysłania
    UCSR0B = (1 << RXEN0) | (1 << TXEN0) | (1 << RXCIE0);

    // Format ramki: 8 bitów danych, 1 bit stopu
    UCSR0C = (1 << UCSZ01) | (1 << UCSZ00);

    // Tworzenie kolejek
    xRxQueue = xQueueCreate(32, sizeof(char)); // Bufor odbiorczy
    xTxQueue = xQueueCreate(32, sizeof(char)); // Bufor nadawczy

    // Podpięcie pod stdio
    stdout = stdin = &uart_str;
}

int uart_putchar(char c, FILE *stream)
{
    if (c == '\n') uart_putchar('\r', stream);

    // Wstawiamy znak do kolejki.
    // Jeśli kolejka pełna, zadanie zostanie ZABLOKOWANE (portMAX_DELAY).
    xQueueSend(xTxQueue, &c, portMAX_DELAY);
    UCSR0B |= (1 << UDRIE0);

    return 0;
}

int uart_getchar(FILE *stream)
{
    (void)stream;
    uint8_t data;

    // Czekamy na dane z kolejki RX.
    // Zadanie przechodzi w stan BLOCKED do momentu otrzymania przerwania RX.
    xQueueReceive(xRxQueue, &data, portMAX_DELAY);

    return data;
}

void vTaskTerminal(void *pvParameters)
{
    (void)pvParameters;
    char buffer[64];

    while(1)
    {
        printf("Wpisz tekst: ");
        if (scanf("%63s", buffer) == 1)
            printf("\nOdebrano: %s\n", buffer);
        vTaskDelay(100 / portTICK_PERIOD_MS);
    }
}

void vTaskLed(void *pvParameters)
{
    (void)pvParameters;
    DDRB |= (1 << LED_PIN);

    while(1)
    {
        PORTB ^= (1 << LED_PIN);
        vTaskDelay(500 / portTICK_PERIOD_MS);
    }
}

void vApplicationIdleHook(void) {}

int main(void)
{
    uart_init();
    xTaskCreate(vTaskTerminal, "Terminal", 256, NULL, 2, NULL);
    xTaskCreate(vTaskLed, "LED", 128, NULL, 1, NULL);
    vTaskStartScheduler();
    return 0;
}
