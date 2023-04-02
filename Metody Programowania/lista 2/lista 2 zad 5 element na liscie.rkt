#lang racket

(define (elem? x xs)
  (if (equal? (first xs) x)
      #t
      (if (null? (rest xs))
           #f
           (elem? x (rest xs)))))

(define l (list 1 2 3 4 5 6))
(elem? 1 l)