#lang plait
;Zadanie 1

;('a 'b -> 'a )
(define (f1 a b) a)

;(('a 'b -> 'c ) ('a -> 'b ) 'a -> 'c )
(define (f2 fh1 fh2 a) (fh1 a(fh2 a))) ;function composition

;((( 'a -> 'a ) -> 'a ) -> 'a )
(define (f3 f) (f (lambda (x) (f (lambda (x) x)))))

; (('a - > 'b ) ('a - > 'c ) - > ('a - > ('b * 'c ) ) )
(define (f4 f g) (lambda (x) (pair (f x) (g x))))

; (('a -> ( Optionof ('a * 'b ) ) ) 'a -> ( Listof 'b ) )
(define (f5 [f : ('a -> (Optionof ('a * 'b)))] a) (list (snd (some-v (f a)))))