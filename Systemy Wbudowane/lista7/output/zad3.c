#include <avr/io.h>
#include <util/delay.h>
#include <stdio.h>
#include <string.h>
#include "i2c.h"
#include "uart.h"

#define DS3231_ADDR 0x68 // Adres I2C modułu DS3231

#define REG_SECONDS 0x00
#define REG_MINUTES 0x01
#define REG_HOURS 0x02
#define REG_DAY 0x03
#define REG_DATE 0x04
#define REG_MONTH 0x05
#define REG_YEAR 0x06

uint8_t bcd_to_dec(uint8_t bcd)
{
    return ((bcd >> 4) * 10) + (bcd & 0x0F);
}

uint8_t dec_to_bcd(uint8_t dec)
{
    return ((dec / 10) << 4) | (dec % 10);
}

uint8_t read_register(uint8_t reg_addr)
{
    uint8_t data;

    i2cStart();
    i2cSend(DS3231_ADDR << 1);
    i2cSend(reg_addr);

    i2cStart();
    i2cSend((DS3231_ADDR << 1) | 0x01);
    data = i2cReadNoAck();
    i2cStop();

    return data;
}

void write_register(uint8_t reg_addr, uint8_t data)
{
    i2cStart();
    i2cSend(DS3231_ADDR << 1);
    i2cSend(reg_addr);
    i2cSend(data);
    i2cStop();
}

void get_date(uint8_t *day, uint8_t *month, uint16_t *year)
{
    *day = bcd_to_dec(read_register(REG_DATE));
    *month = bcd_to_dec(read_register(REG_MONTH) & 0x1F);
    *year = 2000 + bcd_to_dec(read_register(REG_YEAR));
}

void get_time(uint8_t *hours, uint8_t *minutes, uint8_t *seconds)
{
    uint8_t bcd_hours, bcd_minutes, bcd_seconds;

    bcd_seconds = read_register(REG_SECONDS);
    bcd_minutes = read_register(REG_MINUTES);
    bcd_hours = read_register(REG_HOURS);

    *seconds = bcd_to_dec(bcd_seconds & 0x7F);
    *minutes = bcd_to_dec(bcd_minutes & 0x7F);

    if (bcd_hours & 0x40)
    {
        *hours = bcd_to_dec(bcd_hours & 0x1F);
        if (bcd_hours & 0x20)
        {
            *hours += 12;
        }
    }
    else
    {
        *hours = bcd_to_dec(bcd_hours & 0x3F);
    }
}

void set_date(uint8_t day, uint8_t month, uint16_t year)
{
    write_register(REG_DATE, dec_to_bcd(day));
    write_register(REG_MONTH, dec_to_bcd(month));
    write_register(REG_YEAR, dec_to_bcd(year - 2000));
}

void set_time(uint8_t hours, uint8_t minutes, uint8_t seconds)
{
    write_register(REG_SECONDS, dec_to_bcd(seconds));
    write_register(REG_MINUTES, dec_to_bcd(minutes));
    write_register(REG_HOURS, dec_to_bcd(hours));
}

void flush_input_buffer(void)
{
    char c;
    while ((c = getchar()) != '\n' && c != '\r' && c != EOF)
        ;
}

int main(void)
{
    char cmd[10];
    char subcmd[10];
    uint8_t day, month, hours, minutes, seconds;
    uint16_t year;

    i2cInit();
    uart_init();
    uart_stdio_setup();
    stdin = stdout = &uart_file;

    printf("Commands:\n");
    printf("date              - read current date\n");
    printf("time              - read current time\n");
    printf("set date DD-MM-YYYY\n");
    printf("set time HH:MM:SS\n\n");

    while (1)
    {
        printf("> ");

        // Wyczyść poprzedni bufor przed odczytem nowego polecenia
        if (scanf("%s", cmd) != 1)
        {
            flush_input_buffer();
            continue;
        }

        if (strcmp(cmd, "date") == 0)
        {
            get_date(&day, &month, &year);
            printf("%02u-%02u-%04u\n", day, month, year);
            flush_input_buffer();
        }
        else if (strcmp(cmd, "time") == 0)
        {
            get_time(&hours, &minutes, &seconds);
            printf("%02u:%02u:%02u\n", hours, minutes, seconds);
            flush_input_buffer();
        }
        else if (strcmp(cmd, "set") == 0)
        {
            if (scanf("%s", subcmd) != 1)
            {
                printf("Error: Missing subcommand\n");
                flush_input_buffer();
                continue;
            }

            if (strcmp(subcmd, "date") == 0)
            {
                int result = scanf("%hhu-%hhu-%u", &day, &month, &year);

                if (result != 3)
                {
                    printf("Error: Invalid date format (expected DD-MM-YYYY)\n");
                    flush_input_buffer();
                    continue;
                }

                if (day < 1 || day > 31 || month < 1 || month > 12 ||
                    year < 2000 || year > 2099)
                {
                    printf("Error: Date out of range\n");
                    flush_input_buffer();
                    continue;
                }

                set_date(day, month, year);
                printf("Date set to: %02u-%02u-%04u\n", day, month, year);
                flush_input_buffer();
            }
            else if (strcmp(subcmd, "time") == 0)
            {
                int result = scanf("%hhu:%hhu:%hhu", &hours, &minutes, &seconds);

                if (result != 3)
                {
                    printf("Error: Invalid time format (expected HH:MM:SS)\n");
                    flush_input_buffer();
                    continue;
                }

                if (hours > 23 || minutes > 59 || seconds > 59)
                {
                    printf("Error: Time out of range\n");
                    flush_input_buffer();
                    continue;
                }

                set_time(hours, minutes, seconds);
                printf("Time set to: %02u:%02u:%02u\n", hours, minutes, seconds);
                flush_input_buffer();
            }
            else
            {
                printf("Error: Unknown subcommand (use 'date' or 'time')\n");
                flush_input_buffer();
            }
        }
        else
        {
            printf("Error: Invalid command\n");
            flush_input_buffer();
        }
    }

    return 0;
}
