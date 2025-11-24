#include <avr/io.h>
#include <util/delay.h>
#include <stdio.h>
#include <string.h>
#include "i2c.h"
#include "uart.h"

#define EEPROM_ADDR 0x50 // (1010 000x)

uint8_t eeprom_read(uint16_t addr)
{
    uint8_t data;

    // Wyodrębnij bit A8 (wybór bloku pamięci 0 lub 1)
    // 24C04 ma 512 bajtów = 2 bloki po 256 bajtów
    // addr >> 8 przesunięcie o 8 bitów w prawo wydobywa bit 8
    // & 0x01 maskuje wszystkie bity oprócz najmłodszego
    uint8_t block = (addr >> 8) & 0x01;

    // Utworz adres urządzenia I2C z bitem bloku
    // Format: 1010 A2 A1 A8 (bez bitu R/W)
    // EEPROM_ADDR = 0x50 = 0b01010000 (1010 00x0)
    // block << 1 przesuwa bit bloku na pozycję A8
    uint8_t device_addr = EEPROM_ADDR | (block << 1);

    // START
    // DEVICE_ADDR(W)
    // WORD_ADDR
    // START
    // DEVICE_ADDR(R)
    // DATA
    // STOP

    // === FAZA 1: Dummy Write - ustawienie wskaźnika adresu w EEPROM ===

    i2cStart();

    // Wyślij adres urządzenia z bitem W=0 (zapis)
    // device_addr << 1 tworzy 8-bitowy bajt z bitem R/W=0 na końcu
    // Przykład: 0x50 << 1 = 0xA0 = 0b10100000
    i2cSend(device_addr << 1);

    // Wyślij adres bajtu w wybranym bloku (młodsze 8 bitów adresu A7-A0)
    // addr & 0xFF maskuje bity 8-15, pozostawiając tylko A7-A0
    i2cSend((uint8_t)(addr & 0xFF));

    // === FAZA 2: Właściwy odczyt danych ===

    i2cStart();

    // Wyślij adres urządzenia z bitem R=1 (odczyt)
    // | 0x01 ustawia najmłodszy bit (R/W) na 1
    // Przykład: (0x50 << 1) | 0x01 = 0xA1 = 0b10100001
    i2cSend((device_addr << 1) | 0x01);

    // Odczytaj bajt danych z EEPROM
    data = i2cReadNoAck();
    i2cStop();
    return data;
}

void eeprom_write(uint16_t addr, uint8_t data)
{
    // Wyodrębnij bit A8 (wybór bloku pamięci)
    uint8_t block = (addr >> 8) & 0x01;

    // Utworz adres urządzenia I2C z bitem bloku
    uint8_t device_addr = EEPROM_ADDR | (block << 1);

    // START
    // DEVICE_ADDR(W)
    // WORD_ADDR
    // DATA
    // STOP
    // [czekaj tWR=10ms]

    i2cStart();

    // Wyślij adres urządzenia z bitem W=0 (zapis)
    i2cSend(device_addr << 1);

    // Wyślij adres bajtu w bloku (A7-A0)
    i2cSend((uint8_t)(addr & 0xFF));

    // Wyślij bajt danych do zapisania
    i2cSend(data);

    i2cStop();

    // Czekaj na zakończenie wewnętrznego cyklu zapisu (tWR)
    // Zgodnie z dokumentacją: tWR max = 5ms, używamy 10ms dla pewności
    _delay_ms(10);
}

int main(void)
{
    char cmd[5];
    uint16_t addr;
    uint16_t value;

    i2cInit();
    uart_init();
    uart_stdio_setup();
    stdin = stdout = &uart_file;

    printf("Commands:\n");
    printf("read <addr>\n");
    printf("write <addr> <value>\n");
    printf("Address range: 0-511\n\n");

    while (1)
    {
        printf("> ");
        scanf("%s", cmd);

        if (strcmp(cmd, "read") == 0)
        {
            scanf("%u", &addr);
            if (addr > 0x1FF)
            {
                printf("Error: Address out of range (0-511)\n");
                continue;
            }
            printf("Read addr %u: %u\n", addr, eeprom_read(addr));
        }
        else if (strcmp(cmd, "write") == 0)
        {
            scanf("%u %u", &addr, &value);
            if (addr > 0x1FF)
            {
                printf("Error: Address out of range (0-511)\n");
                continue;
            }
            if (value > 0xFF)
            {
                printf("Error: Value out of range (0-255)\n");
                continue;
            }

            eeprom_write(addr, (uint8_t)value);
            printf("Wrote value %u to addr %u\n", value, addr);
        }
        else
        {
            printf("Invalid command\n");
        }
    }
    return 0;
}
