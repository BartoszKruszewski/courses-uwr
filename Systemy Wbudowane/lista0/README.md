`make all`  # kompilacja
`ls /dev/tty.*`  # wykrycie portu Arduino
`PORT = /dev/tty.usbserial-120`  # ustawienie wykrytego PORTu w Makefile
`make install`  # wgranie pliku .hex na Arduino

screen -X -S