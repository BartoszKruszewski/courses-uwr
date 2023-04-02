#lang plait

(define (map f l)
  (if (empty? l) '()
      (cons (f (first l)) (map f (rest l)))))

(map (lambda (x) (+ x 1)) '(1 2 3 4 5))

; dla dowolnych funkcji f i g oraz listy xs zachodzi (map f (map g xs)) ≡ (map (lambda (x) (f (g x))) xs)
;
; Indukcja względem xs
; P := (map f (map g xs)) ≡ (map (lambda (x) (f (g x))) xs)
;
; (i) Do udowodnienia: (map f (map g empty)) ≡ (map (lambda (x) (f (g x))) empty)
;
;     L ≡ (map f (map g empty)) ≡ (map f empty) ≡ empty
;     P ≡ (map (lambda (x) (f (g x))) empty) ≡ empty
;
; (ii) Zał. (map f (map g xs)) ≡ (map (lambda (x) (f (g x))) xs)
;      Do udowodnienia: dla dowolnego elementu x (map f (map g (cons x xs))) ≡ (map (lambda (x) (f (g x))) (cons x xs))
;
;      (map f (map g (cons x xs))) ≡
;      (map f (cons (g x) (map g xs))) ≡
;      (cons (f (g x)) (map f (map g xs))) ≡
;      (cons (f (g x)) (map (lambda (x) (f (g x))) xs)) ≡
;      (map (lambda (x) (f (g x))) (cons x xs))
;
; więc dla dowolnych funkcji f i g oraz listy xs zachodzi (map f (map g xs)) ≡ (map (lambda (x) (f (g x))) xs)

