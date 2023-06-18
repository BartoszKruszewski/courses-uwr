#lang plait

(define (sorted? l)
  (if (or (empty? l) (empty? (rest l))) #t
      (and (< (first l) (second l)) (sorted? (rest l)))))

(define (insert x l)
  (if (empty? l) (list x)
      (if (< x (first l))
             (cons x l)
             (cons (first l) (insert x (rest l))))))

(insert 3 '())

; Do udowodnienia: jeśli (sorted? xs) ≡ #t to (sorted? (insert x xs)) ≡ #t
;
; Indukcja względem xs
; P := (sorted? xs) ≡ #t => (sorted? (insert x xs)) ≡ #t
;
; (i) zał. (sorted? empty) ≡ #t
;     Do udowodnienia: (sorted? (insert x empty)) ≡ #t
;
;     (sorted? (insert x empty)) ≡
;     (sorted? '(x)) ≡ #t
;
; (ii) zał. (sorted? xs) ≡ #t => (sorted? (insert x xs)) ≡ #t
;      Do udowodnienia: (sorted? (cons y xs)) ≡ #t => (sorted? (insert x (cons y xs))) ≡ #t
;
;      zał 2. (sorted? (cons y xs)) ≡ #t
;      Do udowodnienia: (sorted? (insert x (cons y xs))) ≡ #t
;
;      Rozpatrzmy dwa przypadki:
;      1. x < y
;         (sorted? (insert x (cons y xs))) ≡
;         (sorted? (cons x (cons y xs))) ≡
;         (and (< x y) (sorted? (cons y xs))) ≡
;         (and #t #t) ≡ #t
;      2. x >= y
;         (sorted? (insert x (cons y xs))) ≡
;         (sorted? (cons y (insert x xs))) ≡
;         (and #t (sorted? (insert x xs))) ≡ ponieważ (sorted? (cons y xs)) ≡ #t to y <= wszystkie elementy xs oraz x >= y
;         (and #t #t) ≡ #t ponieważ (sorted? (cons y xs)) ≡ #t to
;                                   (and (< y (first xs)) (sorted? xs)) ≡ #t to
;                                   (sorted? xs) ≡ #t
;                                    to z zał. indukcyjenego (sorted? (insert x xs)) ≡ #t
;
; więc jeśli (sorted? xs) ≡ #t to (sorted? (insert x xs)) ≡ #t      

