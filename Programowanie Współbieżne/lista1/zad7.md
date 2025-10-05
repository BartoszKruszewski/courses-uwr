#### Zakleszczenie

Wystąpi kiedy wszyscy filozofowie wezmą lewą pałeczkę jednocześnie. Wtedy wszystkie pałeczki będą zajęte i nikt nie będzie mógł wziąć drugiej pałeczki do ręki, a co za tym idzie również nikt nie odłoży żadnej pałeczki. Powstaje wtedy **"cykl oczekiwań"**.

#### Rozwiązanie z przełamaniem symetrii

Można dowolnie podzielić filozofów na leworęcznych i praworęcznych. Wtedy jakiś filozof będzie chciał najpierw podniesć prawą pałeczkę zamiast lewej, co przerwie cykl i nie dopuści do zakleszczenia.

```java
public void run() {
    Random random = new Random();
    while (true) {
        try {
            sleep(random.nextInt(1000));
            sleep(100);
            System.out.println("Philosopher " + id + " is hungry");

            // rozróżnienie na leworęcznych i praworęcznych
            // parzyści są leworęczni
            if ((id % 2) == 0) {
                left.get();
                right.get();
            } else {
                right.get();
                left.get();
            }

            left.put();
            right.put();

        } catch (InterruptedException ex) {
            return;
        }
    }
}
```

#### Rozwiązanie z porządkowaniem pałeczek

Ustalamy kolejności podniesienia pałeczek według jakiegoś stałego porządku, np id. Wtedy również łamiemy symetrie, co ostatecznie ma zlikwidować występowanie cyklu oczekiwań.

```java
public void run() {
    Random random = new Random();
    while (true) {
        try {
            sleep(random.nextInt(1000));
            sleep(100);
            System.out.println("Philosopher " + id + " is hungry");

            // ustalenie kolejności podniesienia pałeczek na podstawie ich id
            Fork first = (left.id < right.id) ? left : right;
            Fork second = (left.id < right.id) ? right : left;

            first.get();
            second.get();

            second.put();
            first.put();

        } catch (InterruptedException ex) {
            return;
        }
    }
}
```
