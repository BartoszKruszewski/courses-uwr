#lang plait

(define-syntax my-and
  (syntax-rules ()
    [(my-and) #t]
    [(my-and [a : Boolean]) a]
    [(my-and a b ...) (if a (my-and b ...) a)] ))

(define-syntax my-or
  (syntax-rules ()
    [(my-or) #f]
    [(my-or [a : Boolean]) a]
    [(my-or a b ...) (if a a (my-or b ...))]))

(define-syntax let
  (syntax-rules ()
    [(let () a) a]
    [(let ([x1 a1] [x2 a2] ...) body)
     ((lambda (x1 x2 ...) body) a1 a2 ...)]))

(define-syntax let*
  (syntax-rules ()
    [(let* () a) a]
    [(let* ([x1 a1] [x2 a2] ...) body)
     ((lambda (x1) (let* ([x2 a2] ...) body)) a1)]))



(let* ([a 10] [b (+ a 10)]) (+ a b))





 
     