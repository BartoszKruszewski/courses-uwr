#include <avr/io.h>
#include <avr/interrupt.h>
#include <stdio.h>

#include "FreeRTOS.h"
#include "task.h"
#include "semphr.h"
#include "uart.h"

void initADC(void);
uint16_t readADC(uint8_t mux);
void uart_print(const char *str, uint16_t val);
void vSensorTask(void *pvParameters);
void vApplicationIdleHook(void);

SemaphoreHandle_t xADCMutex;    // Chroni dostęp do sprzętu ADC
SemaphoreHandle_t xADCComplete; // Sygnalizuje zakończenie konwersji (ISR -> Task)

typedef struct
{
    uint8_t muxChannel;
    TickType_t delayMs;
    const char *sensorName;
} SensorTaskParams_t;

void initADC(void)
{
    // Konfiguracja: Napięcie odniesienia AVCC, prescaler 128 (dla 16MHz -> 125kHz)
    ADMUX = (1 << REFS0);
    ADCSRA = (1 << ADEN) | (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);
}

uint16_t readADC(uint8_t mux)
{
    uint16_t result = 0;

    xSemaphoreTake(xADCMutex, portMAX_DELAY); // Uzyskaj wyłączny dostęp do ADC.
    xSemaphoreTake(xADCComplete, 0); // Upewnij się, że semafor zakończenia jest pusty przed startem

    ADMUX = (ADMUX & 0xF0) | (mux & 0x0F); // Maska 0x0F zakłada kanały 0-7. Dla pewności czyścimy dolne 4 bity ADMUX.
    ADCSRA |= (1 << ADIE); // Włącz przerwanie ADC (Interrupt Enable)
    ADCSRA |= (1 << ADSC); // Start Conversion

    xSemaphoreTake(xADCComplete, portMAX_DELAY); // Zablokuj zadanie w oczekiwaniu na wynik.

    result = ADC; // Odczyt wyniku
    ADCSRA &= ~(1 << ADIE); // Wyłącz przerwania ADC 

    xSemaphoreGive(xADCMutex); // Zwolnij Muteks

    return result;
}

ISR(ADC_vect)
{
    BaseType_t xHigherPriorityTaskWoken = pdFALSE;
    xSemaphoreGiveFromISR(xADCComplete, &xHigherPriorityTaskWoken);
    if (xHigherPriorityTaskWoken != pdFALSE) taskYIELD();
}

void vSensorTask(void *pvParameters)
{
    SensorTaskParams_t *params = (SensorTaskParams_t *)pvParameters;
    while (1)
    {
        uint16_t val = readADC(params->muxChannel);
        printf("%s: %u\r\n", params->sensorName, val);
        vTaskDelay(params->delayMs / portTICK_PERIOD_MS);
    }
}

void vApplicationIdleHook(void) {}

int main(void)
{
    initADC();
    uart_init();
    stdout = stdin = &uart_file;

    xADCMutex = xSemaphoreCreateMutex();
    xADCComplete = xSemaphoreCreateBinary();

    static SensorTaskParams_t p1 = {0, 500, "Potencjometr (CH0)"};
    static SensorTaskParams_t p2 = {1, 1000, "Termistor (CH1)"};
    static SensorTaskParams_t p3 = {2, 2000, "Fotorezystor (CH2)"};

    xTaskCreate(vSensorTask, "Task1", 200, &p1, 2, NULL);
    xTaskCreate(vSensorTask, "Task2", 200, &p2, 2, NULL);
    xTaskCreate(vSensorTask, "Task3", 200, &p3, 2, NULL);
    vTaskStartScheduler();
    return 0;
}
