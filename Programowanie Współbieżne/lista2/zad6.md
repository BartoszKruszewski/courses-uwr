```java
class Node implements Lock {
    private int globalIndex;
    // threads from left subtree have ID lower than index
    private int i = (ThreadID.get() <= this.globalIndex) ? 0 else 1;

    public void lock() {
        // w lock "poziom wyzej" mozna wejsc dopiero po wyjsciu z petli poziom nizej
        j = 1 - i;
        flag[i] = true;
        victim = i;
        while (flag[j] && victim == i) {};
    }
    public void unlock() {
        flag[i] = false;
    }
}
```

Do zamieszczonej implementacji Locka należy jeszcze dodać klasę "pilnującą porządku" w przechodzeniu pomiędzy poziomami drzewa, która przydziela indeksy odpowiednim wątkom.