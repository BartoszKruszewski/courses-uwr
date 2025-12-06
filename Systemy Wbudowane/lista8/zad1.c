#include <avr/io.h>
#include "FreeRTOS.h"
#include "task.h"

#define BUTTON_PIN PB0
#define REPLAY_LED_PIN PB1
#define BUTTON_PORT PINB
#define LED_PORT PORTB
#define LED_DDR DDRB

#define DELAY_TIME_MS 1000
#define SAMPLE_RATE_MS 10
#define BUFFER_SIZE (DELAY_TIME_MS / SAMPLE_RATE_MS)

void vTaskKnightRider(void *pvParameters);
void vTaskButtonDelay(void *pvParameters);
void vApplicationIdleHook(void);

void vTaskKnightRider(void *pvParameters)
{
    (void)pvParameters;

    uint8_t position = 0;
    int8_t direction = 1;

    DDRD = 0xFF;

    while (1)
    {
        PORTD = (1 << position);
        position += direction;

        if (position == 7)
        {
            direction = -1;
        }
        else if (position == 0)
        {
            direction = 1;
        }

        vTaskDelay(pdMS_TO_TICKS(100));
    }
}

void vTaskButtonDelay(void *pvParameters)
{
    (void)pvParameters;

    LED_DDR |= (1 << REPLAY_LED_PIN);
    PORTB |= (1 << BUTTON_PIN); // Pull-up

    uint8_t historyBuffer[BUFFER_SIZE] = {0};
    uint16_t headIndex = 0;

    while (1)
    {
        uint8_t pastState = historyBuffer[headIndex];

        if (pastState)
        {
            LED_PORT |= (1 << REPLAY_LED_PIN);
        }
        else
        {
            LED_PORT &= ~(1 << REPLAY_LED_PIN);
        }

        if (!(BUTTON_PORT & (1 << BUTTON_PIN)))
        {
            historyBuffer[headIndex] = 1;
        }
        else
        {
            historyBuffer[headIndex] = 0;
        }

        headIndex++;
        if (headIndex >= BUFFER_SIZE)
        {
            headIndex = 0;
        }

        vTaskDelay(pdMS_TO_TICKS(SAMPLE_RATE_MS));
    }
}

void vApplicationIdleHook(void) {}

int main(void)
{
    xTaskCreate(vTaskKnightRider, "KnightRider", configMINIMAL_STACK_SIZE, NULL, 1, NULL);
    xTaskCreate(vTaskButtonDelay, "ButtonDelay", configMINIMAL_STACK_SIZE + 50, NULL, 2, NULL);

    vTaskStartScheduler();
    return 0;
}
