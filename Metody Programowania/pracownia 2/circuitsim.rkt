#lang racket
(require data/heap)
(provide sim? wire?
        (contract-out
          [make-sim        (-> sim?)]
          [sim-wait!       (-> sim? positive? void?)]
          [sim-time        (-> sim? real?)]
          [sim-add-action! (-> sim? positive? (-> any/c) void?)]

          [make-wire       (-> sim? wire?)]
          [wire-on-change! (-> wire? (-> any/c) void?)]
          [wire-value      (-> wire? boolean?)]
          [wire-set!       (-> wire? boolean? void?)]

          [bus-value (-> (listof wire?) natural?)]
          [bus-set!  (-> (listof wire?) natural? void?)]

          [gate-not  (-> wire? wire? void?)]
          [gate-and  (-> wire? wire? wire? void?)]
          [gate-nand (-> wire? wire? wire? void?)]
          [gate-or   (-> wire? wire? wire? void?)]
          [gate-nor  (-> wire? wire? wire? void?)]
          [gate-xor  (-> wire? wire? wire? void?)]

          [wire-not  (-> wire? wire?)]
          [wire-and  (-> wire? wire? wire?)]
          [wire-nand (-> wire? wire? wire?)]
          [wire-or   (-> wire? wire? wire?)]
          [wire-nor  (-> wire? wire? wire?)]
          [wire-xor  (-> wire? wire? wire?)]

          [flip-flop (-> wire? wire? wire? void?)]))


;; ====== Przewód ======

;; Struktura przewodu
(struct wire (sim [value #:mutable] [actions #:mutable]))

;; Struktura symulacji
(struct sim ([time #:mutable] events))

;; Funkcja tworząca nowy przewód
(define (make-wire sim)
  (wire sim #f '()))

;; Funckja dodająca wszystkie akcje przewodu do symulacji
(define (add-actions! wire)
  (let* ([sim (wire-sim wire)] [time (sim-time sim)])
    (for-each
     (lambda (action-record)
       (sim-add-action! sim (+ time (car action-record)) (cdr action-record)))
     (wire-actions wire))))

;; Funkcja ustawiająca wartość dla przewodu
(define (wire-set! wire value)
  (unless (equal? (wire-value wire) value)
    (set-wire-value! wire value)
    (add-actions! wire)))

;; Funkcja dodająca akcję do przewodu
(define (wire-on-change! wire action-record)
  (set-wire-actions! wire (cons action-record (wire-actions wire)))
  ((cdr action-record)))

;; ====== Symulacja ======

;; Funkcja tworząca nową symulację
(define (make-sim)
  (sim 0 (make-heap (lambda (pair1 pair2) (< (car pair1) (car pair2))))))

;; Funkcja "przesuwająca" symulację do przodu o podany czas
(define (sim-wait! sim time)
  (define end-time (+ (sim-time sim) time))
  (define heap (sim-events sim))
  (define (execute-next-action)
    (unless (zero? (heap-count heap))
      (let* ([action-record (heap-min heap)]
             [action-time (car action-record)]
             [action (cdr action-record)])
        (unless (> action-time end-time)
          (heap-remove-min! heap)
          (set-sim-time! sim action-time)
          (action)
          (execute-next-action)))))
  (execute-next-action)
  (set-sim-time! sim end-time))

;; Funkcja dodająca akcję do symulacji
(define (sim-add-action! sim time action)
  (heap-add! (sim-events sim) (cons time action)))

;; ====== Akcje ======

;; Funckja tworząca nową akcję
(define (make-action out in1 in2 proc)
  (if (null? in2)
      (lambda () (wire-set! out (proc (wire-value in1))))
      (lambda () (wire-set! out (proc (wire-value in1) (wire-value in2))))))

;; ====== Bramki logiczne ======

;; Generyczna funkcja do tworzenia bramek
(define (gate-gen out in1 in2 proc wait-time)
  (wire-on-change! in1 (cons wait-time (make-action out in1 in2 proc)))
  (unless (null? in2)
    (wire-on-change! in2 (cons wait-time (make-action out in1 in2 proc)))))

;; Funkcja łącząca dwa przewody w bramkę NOT
(define (gate-not out in)
  (gate-gen out in null not 1))

;; Funkcja tworząca bramkę OR
(define (gate-or out in1 in2)
  (gate-gen out in1 in2 (lambda (p q) (or p q)) 1))

;; Funkcja tworząca bramkę AND
(define (gate-and out in1 in2)
  (gate-gen out in1 in2 (lambda (p q) (and p q)) 1))

;; Funkcja tworząca bramkę NOR
(define (gate-nor out in1 in2)
  (gate-gen out in1 in2 (lambda (p q) (not (or p q))) 1))

;; Funkcja tworząca bramkę NAND
(define (gate-nand out in1 in2)
  (gate-gen out in1 in2 (lambda (p q) (not (and p q))) 1))

;; Funkcja tworząca bramkę XOR
(define (gate-xor out in1 in2)
  (gate-gen out in1 in2 (lambda (p q) (not (equal? p q))) 2))

;; Funkcja tworzącą nowy przewód i tworząca do niego bramkę NOT
(define (wire-not in)
  (define new-wire (make-wire (wire-sim in)))
  (gate-not new-wire in)
  new-wire)

;; Funkcja tworzącą nowy przewód i tworząca do niego bramkę AND
(define (wire-and in1 in2)
  (define new-wire (make-wire (wire-sim in1)))
  (gate-and new-wire in1 in2)
  new-wire)

;; Funkcja tworzącą nowy przewód i tworząca do niego bramkę OR
(define (wire-or in1 in2)
  (define new-wire (make-wire (wire-sim in1)))
  (gate-or new-wire in1 in2)
  new-wire)

;; Funkcja tworzącą nowy przewód i tworząca do niego bramkę NOR
(define (wire-nor in1 in2)
  (define new-wire (make-wire (wire-sim in1)))
  (gate-nor new-wire in1 in2)
  new-wire)

;; Funkcja tworzącą nowy przewód i tworząca do niego bramkę NAND
(define (wire-nand in1 in2)
  (define new-wire (make-wire (wire-sim in1)))
  (gate-nand new-wire in1 in2)
  new-wire)

;; Funkcja tworzącą nowy przewód i tworząca do niego bramkę XOR
(define (wire-xor in1 in2)
  (define new-wire (make-wire (wire-sim in1)))
  (gate-xor new-wire in1 in2)
  new-wire)

;; ===== Magistrale =====

(define (bus-set! wires value)
  (match wires
    ['() (void)]
    [(cons w wires)
     (begin
       (wire-set! w (= (modulo value 2) 1))
       (bus-set! wires (quotient value 2)))]))

(define (bus-value ws)
  (foldr (lambda (w value) (+ (if (wire-value w) 1 0) (* 2 value)))
         0
         ws))

(define (flip-flop out clk data)
  (define sim (wire-sim data))
  (define w1  (make-wire sim))
  (define w2  (make-wire sim))
  (define w3  (wire-nand (wire-and w1 clk) w2))
  (gate-nand w1 clk (wire-nand w2 w1))
  (gate-nand w2 w3 data)
  (gate-nand out w1 (wire-nand out w3)))


