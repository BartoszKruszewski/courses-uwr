#include <avr/io.h>
#include <util/delay.h>
#include "USI_TWI_Master.h"

#define SLAVE_ADDR 0x7F

int main(void)
{
    USI_TWI_Master_Initialise();

    uint8_t counter = 0;
    unsigned char msg_buffer[2];

    while (1)
    {
        // Przygotowanie adresu: (Adres << 1) | Bit R/W (0 = Zapis)
        msg_buffer[0] = (SLAVE_ADDR << 1);
        msg_buffer[1] = counter++;
        USI_TWI_Start_Transceiver_With_Data(msg_buffer, 2);

        _delay_ms(1000);
    }
}
