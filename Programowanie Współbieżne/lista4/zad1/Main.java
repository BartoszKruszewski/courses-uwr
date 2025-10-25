public class Main {
    
    public static void main(String[] args) {
        try {
            LongestSequence finder = new LongestSequence();
            
            int[] array1 = {1, 2, 1, 2, 1, 2, 1, 2, 3, 3, 3};
            System.out.print("Tablica: ");
            print(array1);
            System.out.print("Wynik: ");
            print(finder.find(array1, 4));
            System.out.println();
            
            int[] array2 = {1, 2, 3, 3, 4, 1};
            System.out.print("Tablica: ");
            print(array2);
            System.out.print("Wynik: ");
            print(finder.find(array2, 4));
            System.out.println();
            
            int[] array3 = {5, 5, 5, 5, 1, 1, 7, 7, 7, 7, 7, 2, 2};
            System.out.print("Tablica: ");
            print(array3);
            System.out.print("Wynik: ");
            print(finder.find(array3, 4));
            
        } catch (InterruptedException e) {}
    }
    
    static void print(int[] arr) {
        System.out.print("[");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
            if (i < arr.length - 1) System.out.print(", ");
        }
        System.out.println("]");
    }
}
