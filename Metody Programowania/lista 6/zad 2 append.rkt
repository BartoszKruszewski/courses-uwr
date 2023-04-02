#lang plait

(define (append xs ys)
   (if (empty? xs )
        ys
        (cons (first xs ) (append (rest xs ) ys))))

; Do udowodnienia: dla dowolnych list xs, ys istnieje taka lista zs, że (append xs ys) ≡ zs
;
; Indukcja względem xs
; P := (append xs ys) ≡ zs
;
; (i) (append empty ys) ≡ ys, czyli zs istnieje
; (ii) zał. (append xs ys) ≡ zs
;      do udowodnienia: dla dowolnego elementu x zachodzi (append (cons x xs) ys) ≡ zs
;
;      Weźmy dowolny element x  i podstawmy
;      (append (cons x xs) ys) ≡
;      (cons x (append xs ys)) ≡
;      (cons x zs) które jest listą
;
; dla dowolnych list xs, ys istnieje taka lista zs, że (append xs ys) ≡ zs


