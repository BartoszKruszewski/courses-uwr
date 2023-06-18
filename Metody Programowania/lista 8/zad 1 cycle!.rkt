#lang racket

(define (cycle! lst)
  (define (it first lst)
    (if (null? (mcdr lst))
        (set-mcdr! lst first)
        (it first (mcdr lst))))
  (it lst lst))

(define example-mlist (mcons 1 (mcons 2 (mcons 3 '()))))
example-mlist
(cycle! example-mlist)
example-mlist