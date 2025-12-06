#include <avr/io.h>
#include <stdio.h>
#include <stdlib.h>
#include "FreeRTOS.h"
#include "task.h"
#include "queue.h"
#include "uart.h"

#define LED_PIN PB1
#define LED_PORT PORTB
#define LED_DDR DDRB

#define QUEUE_LENGTH 5
#define QUEUE_ITEM_SIZE sizeof(uint16_t)

void vTaskSerialRead(void *pvParameters);
void vTaskBlink(void *pvParameters);
void vApplicationIdleHook(void);

QueueHandle_t xBlinkQueue;

void vTaskSerialRead(void *pvParameters)
{
    (void)pvParameters;
    uint16_t inputVal;

    vTaskDelay(pdMS_TO_TICKS(100));
    printf("Wpisz czas w ms i wcisnij ENTER:\r\n");

    while (1)
    {
        if (scanf("%u", &inputVal) == 1)
        {
            printf("Odebrano: %u ms\r\n", inputVal);
            xQueueSend(xBlinkQueue, &inputVal, portMAX_DELAY);
        }
        else
        {
            scanf("%*s");
            printf("To nie liczba!\r\n");
        }
    }
}

void vTaskBlink(void *pvParameters)
{
    (void)pvParameters;
    uint16_t blinkDuration;

    LED_DDR |= (1 << LED_PIN);

    while (1)
    {
        if (xQueueReceive(xBlinkQueue, &blinkDuration, portMAX_DELAY) == pdPASS)
        {

            if (blinkDuration < 10)
                blinkDuration = 10;

            // Przeliczenie na uint32_t aby uniknąć przepełnienia
            uint32_t durationTicks = ((uint32_t)blinkDuration * configTICK_RATE_HZ) / 1000;
            uint32_t gapTicks = (200UL * configTICK_RATE_HZ) / 1000;

            LED_PORT |= (1 << LED_PIN);
            vTaskDelay((TickType_t)durationTicks);
            LED_PORT &= ~(1 << LED_PIN);
            vTaskDelay((TickType_t)gapTicks);
        }
    }
}

void vApplicationIdleHook(void) {}

int main(void)
{
    uart_init();
    stdout = stdin = &uart_file;

    xBlinkQueue = xQueueCreate(QUEUE_LENGTH, QUEUE_ITEM_SIZE);

    // Stos dla scanf musi być większy (~256 bajtów)
    xTaskCreate(vTaskSerialRead, "Serial", 256, NULL, 1, NULL);
    xTaskCreate(vTaskBlink, "Blink", 128, NULL, 2, NULL);
    vTaskStartScheduler();

    while (1)
        ;
    return 0;
}
