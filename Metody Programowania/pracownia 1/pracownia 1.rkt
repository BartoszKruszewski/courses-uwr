#lang racket

(provide (struct-out column-info)
         (struct-out table)
         (struct-out and-f)
         (struct-out or-f)
         (struct-out not-f)
         (struct-out eq-f)
         (struct-out eq2-f)
         (struct-out lt-f)
         table-insert
         table-project
         table-sort
         table-select
         table-rename
         table-cross-join
         table-natural-join)




; struktury 
(define-struct column-info (name type) #:transparent)

(define-struct table (schema rows) #:transparent)


; przykładowe tabele
(define cities
  (table
   (list (column-info 'city    'string)
         (column-info 'country 'string)
         (column-info 'area    'number)
         (column-info 'capital 'boolean))
   (list (list "Wrocław" "Poland"  293 #f)
         (list "Warsaw"  "Poland"  517 #t)
         (list "Poznań"  "Poland"  262 #f)
         (list "Berlin"  "Germany" 892 #t)
         (list "Munich"  "Germany" 310 #f)
         (list "Paris"   "France"  105 #t)
         (list "Rennes"  "France"   50 #f))))

(define countries
  (table
   (list (column-info 'country 'string)
         (column-info 'population 'number))
   (list (list "Poland" 38)
         (list "Germany" 83)
         (list "France" 67)
         (list "Spain" 47))))

(define (empty-table columns) (table columns '()))

(define countries2
  (table
   (list (column-info 'country 'string))
   (list (list "Poland")
         (list "Germany"))))

(define example-empty-table (table '() '()))

; FUNKCJE UNIWERSALNE

; funkcja zwracająca index elementu na liście
(define (list-index x xs)
    (define (it x xs n)
        (if (equal? x (car xs)) 
            n
            (it x (cdr xs) (+ n 1))))
    (it x xs 0))

; funckja zwracająca listę elementów występujących na obu listach
(define (lists-product tab1 tab2)
  (filter (lambda (x) (member x tab2)) tab1))

; funkcja, która zwraca listę elementów które nie są parami
(define (skip-pairs xs)
  (filter (lambda (x) (not (pair? x))) xs))

; funkcja, która zwraca listę pierwszych elementów z listy par
(define (pair-list-decomp xs)
  (map (lambda (x) (car x)) (filter pair? xs)))

; funkcja zwracająca listę nazw kolumn 
(define (schema->list schema)
  (map column-info-name schema))

; funkcja sprawdzająca czy tabla ma kolumnę o podanej nazwie
(define (correct-col-name? col tab)
  (member col (schema->list (table-schema tab))))

; funkcja sprawdzająca czy tabla ma listę kolumn o podanej nazwie
(define (correct-cols-names? cols tab)
  (if (null? cols) #t
      (and (correct-col-name? (car cols) tab) (correct-cols-names? (cdr cols) tab))))
      

; funkcja pomocniczna służąca do debugowania
(define (print-debug x)
  (define (it n x void)
    (if (= n 0)
        x
        (it (- n 1) x (pretty-print x))))
  (it 1 x null))

; funckja porównująca, uwzględniająca typ
  (define (compare a b)
    (cond
      [(number? a) (< a b)]
      [(string? a) (string<? a b)]
      [(symbol? a) (symbol<? a b)]
      [(boolean? a) a]))

; WSTAWIANIE WIERSZA DO TABELI
(define (table-insert row tab)

  ; funkcja pomocnicza do sprawdzania, czy wartość jest typu oczekiwanego
  (define (check-type val expected-type)
    (cond
      [(equal? expected-type 'number) (number? val)]
      [(equal? expected-type 'string) (string? val)]
      [(equal? expected-type 'symbol) (symbol? val)]
      [(equal? expected-type 'boolean) (boolean? val)]
      [else #f]))

  ; funkcja sprawdzająca czy wstawiany wiersz jest poprawnego typu
  (define (check-row row schema)
    (and (= (length row) (length schema))
         (andmap check-type row (map column-info-type schema))))

  ; główne wywołanie funkcji
  (if (check-row row (table-schema tab))
      (table (table-schema tab) (cons row (table-rows tab)))
      (error "Invalid row!")))

; PROJEKCJA WYBRANYCH KOLUMN
(define (table-project cols tab)
  (if (correct-cols-names? cols tab)
  (let ([schema (table-schema tab)])
    (table (filter (lambda (col-info) (member (column-info-name col-info) cols)) schema)
           (map (lambda (row) (foldr
                    (lambda (val col-info acc) 
                    (if (member (column-info-name col-info) cols) (cons val acc) acc))
                    '() row schema))
                (table-rows tab))))
  (error "Invalid column name!")))

; SORTOWANIE WIERSZY
(define (table-sort cols tab)

  ; funckja do rekurencyjnego porównania
  (define (r-compare cols row1 row2 col-names)
    (if (null? cols)
        #f
        (let ([index (list-index (car cols) col-names)])
          (let ([a (list-ref row1 index)] [b (list-ref row2 index)])
            (if (equal? a b)
                (r-compare (cdr cols) row1 row2 col-names)
                (compare a b))))))
  
  ; główne wywołanie funkcji
  (if (correct-cols-names? cols tab)
  (let ([schema (table-schema tab)])
    (table schema (sort (table-rows tab) (lambda (row1 row2) (r-compare cols row1 row2 (schema->list schema))))))
  (error "Invalid column name!")))


; formuły do selekcji
(define-struct and-f (l r))
(define-struct or-f (l r))
(define-struct not-f (e))
(define-struct eq-f (name val))
(define-struct eq2-f (name name2))
(define-struct lt-f (name val))

; SELEKCJA WIERSZY SPEŁNIAJĄCYCH FORMUŁĘ
(define (table-select form tab)
  
  ; funkcja sprawdzająca czy wiersz spełnia formułę
  (define (evaluate-form? form row col-names)
    (cond ((and-f? form)
           (and (evaluate-form? (and-f-l form) row col-names)
                (evaluate-form? (and-f-r form) row col-names)))
          ((or-f? form)
           (or (evaluate-form? (or-f-l form) row col-names)
               (evaluate-form? (or-f-r form) row col-names)))
          ((not-f? form)
           (not (evaluate-form? (not-f-e form) row col-names)))
          ((eq-f? form)
           (eq? (get-value (eq-f-name form) row col-names)
                (eq-f-val form)))
          ((eq2-f? form) 
           (eq? (get-value (eq2-f-name form) row col-names)
                (get-value (eq2-f-name2 form) row col-names)))
          ((lt-f? form)
           (compare (print-debug (get-value (lt-f-name form) row col-names))
              (lt-f-val form)))))

  ; funkcja zwracająca wartość komórki dla podanego wiersza i kolumny
  (define (get-value col row col-names)
    (if (member col col-names)
        (list-ref row (list-index col col-names))
        (error "Invalid column name!")))

  ;główne wywołanie funkcji
  (table (table-schema tab)
         (let ([col-names (schema->list (table-schema tab))])
           (filter (lambda (row) (evaluate-form? form row col-names)) (table-rows tab)))))

; ZMIANA NAZWY KOLUMNY
(define (table-rename col ncol tab)
  (if (correct-col-name? col tab)
    (table 
        (map (lambda (col-info)
                    (if (equal? (column-info-name col-info) col) 
                        (column-info ncol (column-info-type col-info))
                        col-info))
                (table-schema tab))
        (table-rows tab))
    (error "Invalid column name!")))
  

; ZŁĄCZENIE KARTEZJAŃSKIE
(define (table-cross-join tab1 tab2)
  (table (append (table-schema tab1) (table-schema tab2))
         (foldr (lambda (row2 acc) (append (map (lambda (row1) (append row1 row2)) (table-rows tab1)) acc)) '() (table-rows tab2))))

; ZŁĄCZENIE NATURALNE
(define (table-natural-join tab1 tab2)

  ; funkcja zwracająca listę nazw kolumn występujących jednocześnie w obu tabelach 
  (define (table-same-names tab1 tab2)
    (lists-product (schema->list (table-schema tab1)) (schema->list (table-schema tab2))))
  
  ; funkcja zmieniająca nazwy kolumn występujących jednocześnie w obu tabelach
  (define (table-rename-repeat tab1 tab2)
    (define (it cols table)
      (if (null? cols) table
          (it (cdr cols) (table-rename (car cols) (cons (car cols) "*") table))))
    (it (table-same-names tab1 tab2) tab2))
  
  ; funkcja zwracjąca tylko elementy, które mają swój odpwienik w postaci pary,
  ; gdzie są one na pierwszej pozycji
  (define (only-identity xs)
    (lists-product (skip-pairs xs) (pair-list-decomp xs)))
  
  ; funckcja wybierająca kolumny, które w kolumnach o identycznej,
  ; podanej nazwie mają taką samą wartość
  (define (table-identity name tab)
    (table-select (eq2-f name (cons name "*")) tab))
  
  ; funkcja, która zwraca wszystkie wiersze, których wartości w kolumnach powtarząjcyh się są takie same
  (define (table-select-repeat tab)
    (define (it cols tab)
      (if (null? cols)
          tab
          (it (cdr cols) (table-identity (car cols) tab))))
    (it (only-identity (schema->list (table-schema tab))) tab))

  ; główne wywołanie funkcji
  (let ([tab (table-select-repeat (table-cross-join tab1 (table-rename-repeat tab1 tab2)))])
    (table-project (skip-pairs (schema->list (table-schema tab))) tab)))
  
;(pretty-print (table-insert (list 10 "Poland"  100 #f) cities))
;(pretty-print (table-insert (list "Legnica" "Poland"  100 #f) cities))
;(pretty-print (table-project (list 'city 'country) cities))
;(pretty-print (table-rename 'city 'name cities))
;(pretty-print (table-sort '(country city) cities))
;(pretty-print (table-select (and-f (eq-f 'capital #t) (not-f (lt-f 'area 300) )) cities))
;(table-cross-join cities (table-rename 'country 'country* countries))
;(table-project '(city country area capital population) (table-select (eq2-f 'country 'country*)
;      (table-cross-join cities (table-rename 'country 'country* countries))))
;(table-natural-join cities countries)
;(pretty-print (table-cross-join example-empty-table countries2))
;(table-cross-join example-empty-table cities)

