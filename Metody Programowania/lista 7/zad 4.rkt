#lang racket
;(parametric->/c [a b] (-> a b a))
(define/contract (f1 a b)
  (parametric->/c [a b] (-> a b a)) a)

;(parametric->/c [a b c] (-> (-> a b c) (-> a b) a c))
(define/contract (f2 fp1 fp2 a)
  (parametric->/c [a b c] (-> (-> a b c) (-> a b) a c))
  (fp1 a (fp2 a)))

;(parametric->/c [a b c] (-> (-> b c) (-> a b) (-> a c)))
(define/contract (f3 fp1 fp2)
  (parametric->/c [a b c] (-> (-> b c) (-> a b) (-> a c)))
  (lambda (x) (fp1 (fp2 x))))

;(parametric->/c [a] (-> (-> (-> a a) a) a))
(define/contract (f4 fp)
  (parametric->/c [a] (-> (-> (-> a a) a) a))
  (fp (lambda (x) x)))