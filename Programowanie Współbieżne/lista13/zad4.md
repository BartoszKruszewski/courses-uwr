#### Algorytm

```java
public class Node {
    enum CStatus{IDLE, FIRST, SECOND, RESULT, ROOT};
    // IDLE: nikt jeszcze nie używa węzła.
    // FIRST: pierwszy wątek się tu zameldował (aktywny).
​    // SECOND: drugi wątek się tu zameldował (pasywny już zapisał swoją wartość).
​    // RESULT: wynik dla pasywnego wątku jest gotowy.
​    // ROOT: specjalny stan korzenia

    boolean locked; // zakaz wstępu od węzła
    CStatus cStatus;
    int firstValue, secondValue; // wartości do połączenia
    int result; // wynik do przekazania wyżej
    Node parent;

    public Node() {
        cStatus = CStatus.ROOT;
        locked = false;
    }

    public Node(Node myParent) {
        parent = myParent;
        cStatus = CStatus.IDLE;
        locked = false;
    }

    synchronized boolean precombine() {
        while (locked) wait();
        switch (cStatus) {
            case IDLE:
                cStatus = CStatus.FIRST;
                return true;
            case FIRST:
                locked = true;
                cStatus = CStatus.SECOND;
                return false;
            case ROOT:
                return false;
            default:
                throw new PanicException("unexpected Node state " + cStatus);
        }
    }

    synchronized int combine(int combined) {
        while (locked) wait();
        locked = true;
        firstValue = combined;
        switch (cStatus) {
        case FIRST:
            return firstValue;
        case SECOND:
            return firstValue + secondValue;
        default:
            throw new PanicException("unexpected Node state " + cStatus);
        }
    }

    synchronized int op(int combined) {
        switch (cStatus) {
        case ROOT:
            int prior = result;
            result += combined;
            return prior;
        case SECOND:
            secondValue = combined;
            locked = false;
            notifyAll(); // wake up waiting threads
            while (cStatus != CStatus.RESULT) wait();
            locked = false;
            notifyAll();
            cStatus = CStatus.IDLE;
            return result;
        default:
            throw new PanicException("unexpected Node state");
        }
    }

    synchronized void distribute(int prior) {
        switch (cStatus) {
            case FIRST:
                cStatus = CStatus.IDLE;
                locked = false;
                break;
            case SECOND:
                result = prior + firstValue;
                cStatus = CStatus.RESULT;
                break;
            default:
                throw new PanicException("unexpected Node state");
        }
        notifyAll();
    }
}


// zwykle budowanie drzewa binarnego z Node
public CombiningTree(int width) {
    Node[] nodes = new Node[width - 1];
    nodes[0] = new Node();

    for (int i = 1; i < nodes.length; i++) {
        nodes[i] = new Node(nodes[(i-1)/2]);
    }

    leaf = new Node[(width + 1)/2];

    for (int i = 0; i < leaf.length; i++) {
        leaf[i] = nodes[nodes.length - i - 1];
    }
}

public int getAndIncrement() {
    Stack<Node> stack = new Stack<Node>();
    Node myLeaf = leaf[ThreadID.get()/2];
    Node node = myLeaf;

    // precombining phase
    while (node.precombine()) {
        node = node.parent;
    }
    Node stop = node;

    // combining phase
    node = myLeaf;
    int combined = 1;
        while (node != stop) {
        combined = node.combine(combined);
        stack.push(node);
        node = node.parent;
    }

    // operation phase
    int prior = stop.op(combined);

    // distribution phase
    while (!stack.empty()) {
        node = stack.pop();
        node.distribute(prior);
    }
    return prior;
}
```

#### Dlaczego `precombine()` i `combine()` czekają na `locked == false`?

Aby nie wchodzić w drogę wątkom, które właśnie przetwarzają poprzednią falę operacji. Nowe wątki muszą czekać, aż węzeł będzie "czysty" i gotowy na nową parę.
​
#### Dlaczego `op()` i `distribute()` nie czekają?

Ponieważ wykonują je wątki, które już "trzymają" ten węzeł. To one są odpowiedzialne za trwającą operację, więc nie muszą czekać na samych siebie.
​
#### Wpływ przypisania locked na inne wątki:

- Włączenie (true) w precombine/combine: Blokuje wejście dla "spóźnialskich" wątków z dołu, zmuszając je do czekania w kolejce na następny cykl.
​
- Wyłączenie (false) w op/distribute: Sygnał "koniec pracy" – budzi czekającego partnera (wątek pasywny) lub otwiera węzeł dla zupełnie nowych wątków.
​