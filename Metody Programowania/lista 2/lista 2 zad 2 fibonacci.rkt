#lang racket

(define (fib n)
  (if (or (= n 0) (= n 1)) 1
      (+ (fib (- n 1)) (fib (- n 2)))))

(define (fib-iter n)
  (define (it n acc1 acc2)
    (if (or (= n 0) (= n 1))
        acc2
        (it (- n 1) acc2 (+ acc1 acc2))))
  (it n 1 1 ))


(fib-iter 100)