#lang racket

(require rackunit)

(define (F a b c)
  (if (and (< a b) (< a c)) (+ (* b b) (* c c))
      (if (and (< b c) (< b a)) (+ (* a a) (* c c)) (+ (* b b) (* a a)))))

(check-equal? (F 1 2 3) 13)
(check-equal? (F 3 1 2) 13)
(check-equal? (F 2 3 1) 13)