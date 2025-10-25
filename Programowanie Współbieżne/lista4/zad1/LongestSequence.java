
public class LongestSequence {

    private int[] array; // Tablica do przeszukania (współdzielona między wątkami)
    private int maxLength = 0; // Długość najdłuższego znalezionego ciągu
    private int maxStart = 0; // Pozycja początkowa najdłuższego ciągu w tablicy

    // Wewnętrzna klasa reprezentująca wątek roboczy
    class Worker extends Thread {

        int start, end; // Zakres tablicy do przeszukania przez ten wątek

        // Konstruktor - przypisuje zakres do przeszukania
        Worker(int start, int end) {
            this.start = start;
            this.end = end;
        }

        // Główna metoda wątku - wykonuje się po wywołaniu start()
        @Override
        public void run() {
            int len = 1;    // Długość aktualnego ciągu
            int pos = start; // Pozycja początkowa aktualnego ciągu

            // Przeszukuj swój fragment tablicy
            for (int i = start + 1; i < end; i++) {
                // Jeśli kolejny element jest taki sam jak poprzedni
                if (array[i] == array[i - 1]) {
                    len++; // Zwiększ długość ciągu
                } else {
                    // Koniec ciągu - sprawdź czy to najdłuższy dotychczas
                    update(pos, len);
                    len = 1;    // Rozpocznij nowy ciąg
                    pos = i;    // Nowa pozycja początkowa
                }
            }
            // Sprawdź ostatni ciąg w tym fragmencie
            update(pos, len);
        }
    }

    // Synchronizowana metoda do aktualizacji wyniku globalnego
    // synchronized zapobiega konfliktom gdy kilka wątków jednocześnie próbuje aktualizować wynik
    synchronized void update(int start, int length) {
        // Jeśli znaleziono dłuższy ciąg, zaktualizuj wynik globalny
        if (length > maxLength) {
            maxLength = length;
            maxStart = start;
        }
    }

    // Główna metoda wyszukiwania najdłuższego ciągu
    public int[] find(int[] arr, int threads) throws InterruptedException {
        // Sprawdź przypadki brzegowe
        if (arr == null || arr.length == 0) {
            return new int[0];
        }

        // Zainicjalizuj pola klasy
        array = arr;
        maxLength = 0;

        // Oblicz rozmiar segmentu dla każdego wątku
        int size = arr.length / threads;
        // Tablica do przechowywania referencji do wątków
        Thread[] t = new Thread[threads];

        // Utwórz i uruchom wątki
        for (int i = 0; i < threads; i++) {
            int start = i * size; // Początek segmentu
            // Koniec segmentu (ostatni wątek bierze resztę tablicy)
            int end = (i == threads - 1) ? arr.length : (i + 1) * size;

            t[i] = new Worker(start, end); // Utwórz wątek
            t[i].start(); // Uruchom wątek (wywołuje metodę run())
        }

        // Poczekaj na zakończenie wszystkich wątków
        for (Thread thread : t) {
            thread.join(); // Blokuje główny wątek do momentu zakończenia wątku roboczego
        }

        // WAŻNE: Sprawdź połączenia między segmentami
        // Ciąg mógł zostać podzielony między różne segmenty
        for (int i = 1; i < threads; i++) {
            int boundary = i * size; // Granica między segmentami

            // Jeśli elementy na granicy są takie same
            if (array[boundary] == array[boundary - 1]) {
                int left = 1, right = 1; // Liczniki elementów w lewo i prawo

                // Zlicz identyczne elementy w lewo od granicy
                while (boundary - left - 1 >= 0
                        && array[boundary - left - 1] == array[boundary]) {
                    left++;
                }

                // Zlicz identyczne elementy w prawo od granicy
                while (boundary + right < arr.length
                        && array[boundary + right] == array[boundary]) {
                    right++;
                }

                // Sprawdź czy połączony ciąg jest najdłuższy
                if (left + right > maxLength) {
                    maxLength = left + right;
                    maxStart = boundary - left;
                }
            }
        }

        // Utwórz i zwróć wynikową tablicę z najdłuższym ciągiem
        int[] result = new int[maxLength];
        for (int i = 0; i < maxLength; i++) {
            result[i] = array[maxStart + i]; // Skopiuj elementy najdłuższego ciągu
        }

        return result;
    }
}
