#lang racket

(define (sorted? l)
   (if (null? (rest l))
       #t
       (if (> (first l) (second l)) #f (sorted? (rest l)))))

(define l (list 1 2 3 4 5 6))

(sorted? l)
  