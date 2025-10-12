#### Wzajemne wykluczanie

Każdy węzeł to 2‑wątkowy zamek Petersona.

Więc przez dany węzeł może przejść jednocześnie co najwyżej jeden wątek.

Indukcyjnie ogranicza to liczbę „zwycięzców” na każdym poziomie do jednego przy korzeniu.

Dostęp do sekcji krytycznej jest równoważny wygraniu rywalizacji w korzeniu.

Więc globalne wzajemne wykluczenie jest zapewnione.

#### Niezagłodzenie

Każdy zamek Petersona jest wolny od zagłodzenia.

Więc wątek próbujący wejść nie jest omijany w nieskończoność.

Każdy "niepominięcie" to awans w drzewie.

Indukcyjnie doprowadza to do dostania się do korzenia, a następnie wejście do sekcji krytycznej.

#### Brak zakleszczeń

Zakleszczenie nie występuje na poziomie pojedyńczego zamka.

Natomiast po wyjściu z sekcji krytycznej `unlock()` zwalnia wszystkie zamki na drodze od liścia do korzenia.

Stąd wszystkie przegrane wątki idą o jeden poziom wyżej i tak indukcyjnie aż do korzenia.
