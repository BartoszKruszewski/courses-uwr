#lang racket

(define/contract (bad-fold-right f x xs)
  (parametric->/c [a] (-> (-> a a a) a (listof a) a))
  (if (empty? xs) x
     (f x (bad-fold-right f (first xs) (rest xs)))))

(bad-fold-right + 0 '(1 2 3 4))
(bad-fold-right cons '() '(1 2 3 4))