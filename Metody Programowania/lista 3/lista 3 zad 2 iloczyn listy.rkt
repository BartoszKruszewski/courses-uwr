#lang racket


(define (product l)
  (define (it l acc)
    (if (null? l)
        acc
        (it (cdr l) (* (car l) acc))))
  (if (null? l)
      0
      (it l 1)))

(define (product2 l)
  (foldl * 1 l))

(product2 (list 1 2 3 4 5 ))