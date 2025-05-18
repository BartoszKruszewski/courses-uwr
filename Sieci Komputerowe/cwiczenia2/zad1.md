Aby możliwe było wykrycie kolizji, ramka musi być nadawana przez czas równy co najmniej **dwukrotnemu czasowi propagacji**  między najdalszymi komputerami.

Prędkość sygnału: $10^8\ m/s$

Odległość: $2,5\  km = 2500\ m$

Czas propagacji w jedną stronę: $t_{p} = \frac{2500}{10^8} = 25 \cdot 10^{-6}\ s$

Czas rundy (RTT): $RTT = 2 \cdot 25 \cdot 10^{-6}\ s = 50 \cdot 10^{-6}\ s$

Minimalna liczba bitów: $10^7\ b/s \cdot 50 \cdot 10^{-6}\ s = 500\ \text{b} = 62.5\ \text{B}$

Aby zapewnić wykrywanie kolizji, ramka musi mieć **min. 500 bitów**.

Standard Ethernet zaokrągla to do **64 bajtów (512 bitów)**.
