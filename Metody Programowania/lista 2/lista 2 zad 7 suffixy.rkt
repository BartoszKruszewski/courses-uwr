#lang racket

(define (suffixes xs)
  (append (list xs) (if (null? xs) xs (suffixes (rest xs)))))


(define l (list 1 2 3 4 5))

(suffixes l)