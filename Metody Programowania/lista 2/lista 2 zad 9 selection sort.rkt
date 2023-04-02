#lang racket

(define (minimum l)
  (define (it m l)
    (if (null? l)
        m
        (it (if (< m (first l)) m (first l)) (rest l))))
  (it (first l) l))

(define (select l)
  (let ([m (minimum l)]) (cons m (remove m l))))

(define (select-sort l)
  (let ([s (select l)])
    (if (null? (rest s))
        s
        (cons (first s) (select-sort (rest s))))))
      
  
(select-sort (list 15 21 3 42 5))