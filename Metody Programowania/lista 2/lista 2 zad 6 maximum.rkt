#lang racket

(define (maximum l)
  (define (it m l)
    (if (null? l)
        m
        (it (if (> m (first l)) m (first l)) (rest l))))
  (it 0 l))

(define l (list 19 2 7 4 5 11))
(maximum l)