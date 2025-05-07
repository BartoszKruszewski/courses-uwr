1. Jakie są pola nadawcy i odbiorcy ramki Ethernet podczas pinga V1 → V2?
    - Nadawca: MAC V1
	- Odbiorca: MAC V2
	- IP nadawcy: 192.168.0.1
	- IP odbiorcy: 192.168.0.2

2. Jakie są pola nadawcy i odbiorcy przy pingu na 192.168.0.255?
	- Nadawca ramki: MAC V1
	- Odbiorca ramki: (broadcast)
	- IP nadawcy: 192.168.0.1
	- IP odbiorcy: 192.168.0.255

3. Jak zmienił się stan tablicy ARP po pingu V1 → V2 po flushu?
	- Do tablicy ARP dodano wpis zawierający adres IP i MAC drugiej maszyny.

4. Co jest danymi ramki w zapytaniu ARP?
	- Zapytanie ARP (zawierające IP docelowe i MAC nadawcy).

5. Czy zapytania ARP są wysyłane do konkretnego komputera czy na broadcast?
	- Na adres rozgłoszeniowy (broadcast).

6. Czy odpowiedzi ARP są wysyłane do konkretnego komputera czy na broadcast?
	- Do konkretnego komputera (MAC nadawcy zapytania).

Warstawa transportowa wysyła wszystko na broadcasty i dopiero w nastepnej warstwie jest podział na adresy IP

Tablica ARP kojarzy adresy MAC (sprzetowe) z adresami IP