```java
class MergeSort implements Runnable {
    // protected -> private final
    // dodanie auxArray - współdzielona tablica pomocnicza

    private final int[] array;
    private final int leftIdx;
    private final int rightIdx;
    private final int[] auxArray;

    // konstruktor delegujący z oryginalnymi argumentami
    // zachowuje kompatybilność wsteczną z oryginalnym API
    // konstruktor tworzy tablicę pomocniczą raz (new int[arr.length])
    // zamiast tworzyć dwie tablice w każdym wywołaniu merge
    MergeSort(int arr[], int l, int r) {        
        this(arr, l, r, new int[arr.length]);
    }

    // prywatny konstruktor wewnętrzny z parametrem auxArray używany w run()
    private MergeSort(int[] array, int leftIdx, int rightIdx, int[] auxArray) {
        this.array = array;
        this.leftIdx = leftIdx;
        this.rightIdx = rightIdx;
        this.auxArray = auxArray;
    }

    // usunięto synchronized z metody merge
    // Synchronizacja niepotrzebna - wątki pracują na rozłącznych zakresach tablicy
    // wydzielona logika do metod copyToAuxiliary i mergeFromAuxiliary
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

    // zmieniono obliczanie środka: (l+r)/2 → l+(r-l)/2 (zapobiega integer overflow)
    public void sort(int l, int r) {
        if (l < r) {
            int midIdx = l + (r - l) / 2;
            sort(l, midIdx);
            sort(midIdx + 1, r);
            merge(l, midIdx, r);
        }
    }

    // Wydzielono logikę join do osobnej metody joinThreads
    @Override
    public void run() {
        if (this.leftIdx < this.rightIdx) {
            int midIdx = this.leftIdx + (this.rightIdx - this.leftIdx) / 2;

            MergeSort leftTask = new MergeSort(array, this.leftIdx, midIdx, auxArray);
            MergeSort rightTask = new MergeSort(array, midIdx + 1, this.rightIdx, auxArray);
            
            Thread leftThread = new Thread(leftTask);
            Thread rightThread = new Thread(rightTask);
            
            leftThread.start();
            rightThread.start();
            
            
            joinThreads(leftThread, rightThread);
            
            this.merge(this.leftIdx, midIdx, this.rightIdx);
        }
    }

    // zamiana e.printStackTrace() na RuntimeException z przyczyną
    private void joinThreads(Thread leftThread, Thread rightThread) {
        try {
            leftThread.join();
            rightThread.join();
        } catch (InterruptedException e) {
            throw new RuntimeException("Sorting interrupted", e);
        }
    }
}
```
