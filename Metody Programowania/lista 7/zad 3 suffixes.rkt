#lang racket

(define/contract (suffixes-with-contract lst)
  (parametric->/c [a] (-> (listof a) (listof (listof a))))
  (if (null? lst) '(())
      (cons lst (suffixes-with-contract (cdr lst)))))

(define (suffixes-no-contract lst)
  (if (null? lst) '(())
      (cons lst (suffixes-no-contract (cdr lst)))))

(time (suffixes-no-contract (range 3000)) 0)
(time (suffixes-with-contract (range 3000)) 0)