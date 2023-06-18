#lang racket

(define (mreverse! lst)
  (define (reverse-helper current prev)
    (if (null? current)
        prev
        (let ([next (mcdr current)])
          (set-mcdr! current prev)
          (reverse-helper next current))))
  (reverse-helper lst '()))

(define example-mlist (mcons 1 (mcons 2 (mcons 3 '()))))
(define x (mreverse! example-mlist))
x