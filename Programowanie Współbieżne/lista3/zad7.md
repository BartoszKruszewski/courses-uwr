```java
class MergeSort implements Runnable {
    private final int[] array;
    private final int leftIdx;
    private final int rightIdx;
    private final int[] auxArray;
    
    // minimalny rozmiar dla wielowątkowego sortowania
    // dla tablic mniejszych niż THRESHOLD używamy sekwencyjnego sortowania (efektywniejsze)
    private static final int THRESHOLD = 1000;

    MergeSort(int arr[], int l, int r) {
        this(arr, l, r, new int[arr.length]);
    }

    private MergeSort(int[] array, int leftIdx, int rightIdx, int[] auxArray) {
        this.array = array;
        this.leftIdx = leftIdx;
        this.rightIdx = rightIdx;
        this.auxArray = auxArray;
    }

    private void merge(int leftIdx, int midIdx, int rightIdx) {
        int leftSize = midIdx - leftIdx + 1;
        int rightSize = rightIdx - midIdx;
        
        copyToAuxiliary(leftIdx, leftSize, 0);
        copyToAuxiliary(midIdx + 1, rightSize, leftSize);
        
        mergeFromAuxiliary(leftIdx, midIdx, rightIdx, leftSize, rightSize);
    }

    private void copyToAuxiliary(int sourceIdx, int length, int destOffset) {
        for (int i = 0; i < length; i++) {
            auxArray[destOffset + i] = array[sourceIdx + i];
        }
    }

    private void mergeFromAuxiliary(int leftIdx, int midIdx, int rightIdx, int leftSize, int rightSize) {
        int leftPos = 0;
        int rightPos = 0;
        int arrayPos = leftIdx;
        
        while (leftPos < leftSize && rightPos < rightSize) {
            if (auxArray[leftPos] <= auxArray[leftSize + rightPos]) {
                array[arrayPos++] = auxArray[leftPos++];
            } else {
                array[arrayPos++] = auxArray[leftSize + rightPos++];
            }
        }
        
        while (leftPos < leftSize) {
            array[arrayPos++] = auxArray[leftPos++];
        }
        
        while (rightPos < rightSize) {
            array[arrayPos++] = auxArray[leftSize + rightPos++];
        }
    }

    public void sort(int l, int r) {
        if (l < r) {
            int midIdx = l + (r - l) / 2;
            sort(l, midIdx);
            sort(midIdx + 1, r);
            merge(l, midIdx, r);
        }
    }

    @Override
    public void run() {
        if (this.leftIdx < this.rightIdx) {
            int size = this.rightIdx - this.leftIdx + 1;
            
            // sprawdzenie progu - jeśli tablica mała, sortuj sekwencyjnie
            if (size < THRESHOLD) {
                sort(this.leftIdx, this.rightIdx);
                return;
            }
            
            int midIdx = this.leftIdx + (this.rightIdx - this.leftIdx) / 2;
            
            // tworzymy TYLKO JEDEN nowy wątek (dla lewej połowy)
            // prawa połowa sortowana jest w BIEŻĄCYM wątku
            // UZASADNIENIE: Tworzenie dwóch wątków jest nieefektywne:
            // - Bieżący wątek i tak czeka na join() - marnuje zasoby
            // - Overhead tworzenia wątku jest kosztowny
            // - Wystarczy jeden nowy wątek, drugi może używać bieżącego
            MergeSort leftTask = new MergeSort(array, this.leftIdx, midIdx, auxArray);
            Thread leftThread = new Thread(leftTask);
            
            leftThread.start();
            
            // W BIEŻĄCYM wątku sortujemy prawą połowę (nie tworzymy nowego wątku)
            // To jest kluczowa optymalizacja - eliminuje zbędny wątek
            MergeSort rightTask = new MergeSort(array, midIdx + 1, this.rightIdx, auxArray);
            rightTask.run();  // Wywołanie bezpośrednie run(), nie przez Thread.start()
            
            // Czekamy tylko na jeden wątek (lewy)
            // Prawy już się zakończył (wywołany synchronicznie powyżej)
            joinThread(leftThread);
            
            this.merge(this.leftIdx, midIdx, this.rightIdx);
        }
    }

    // Uproszczona metoda joinThread (tylko jeden wątek)
    private void joinThread(Thread thread) {
        try {
            thread.join();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            throw new RuntimeException("Sorting interrupted", e);
        }
    }
}

```