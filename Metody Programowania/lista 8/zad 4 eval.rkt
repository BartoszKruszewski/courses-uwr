#lang plait

(define (parse-Op s)
  (let ([sym (s-exp->symbol s)])
  (cond
    [(equal? sym '+) +]
    [(equal? sym '-) -]
    [(equal? sym '*) *]
    [(equal? sym '/) /])))

(define (eval s)
  (cond
    [(s-exp-number? s) (s-exp->number s)]
    [(s-exp-list? s)
     (let ([xs (s-exp->list s)])
       ((parse-Op (first  xs)) (eval (second xs)) (eval (third xs))))]))

(eval `(+ (* 3 7) 2))

