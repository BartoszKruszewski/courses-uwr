#lang plait

(define-type Racket-Exp
  (r-num [value : Number])
  (r-var [name : Symbol])
  (r-lambda [arg : (Listof Symbol)] [out : Racket-Exp])
  (r-app [func : Racket-Exp] [args : (Listof Racket-Exp)])
  (r-let [bindings : (Listof (Symbol * Racket-Exp))] [body : Racket-Exp])
  (r-if [condition : Racket-Exp] [then : Racket-Exp] [else : Racket-Exp])
  (r-cond [clauses : (Listof (Racket-Exp * Racket-Exp))]))
 
(define (parse-Racket-Exp s)
    (cond
      [(s-exp-number? s) (r-num (s-exp->number s))]
      [(s-exp-symbol? s) (r-var (s-exp->symbol s))]
      [(s-exp-list? s)
       (let* ([xs (s-exp->list s)] [name (s-exp->symbol (first xs))])
         (cond
           [(equal? name 'lambda)
            (r-lambda
             (map s-exp->symbol (s-exp->list (second xs))) 
             (parse-Racket-Exp (third xs)))]
           [(equal? name 'app)
            (r-app
             (parse-Racket-Exp (second xs))
             (map parse-Racket-Exp (s-exp->list (third xs))))]
           [(equal? name 'let)
            (r-let
             (map (lambda (x)
                    (let ([p (s-exp->list x)])
                      (pair (s-exp->symbol (first p)) (parse-Racket-Exp (second p)))))
                  (s-exp->list (second xs)))
             (parse-Racket-Exp (third xs)))]
           [(equal? name 'if)
            (r-if
             (parse-Racket-Exp (second xs))
             (parse-Racket-Exp (third xs))
             (parse-Racket-Exp (fourth xs)))]
           [(equal? name 'cond)
            (r-cond
             (map (lambda (x)
                    (let ([p (s-exp->list x)])
                      (pair (parse-Racket-Exp (first p)) (parse-Racket-Exp (second p)))))
                  (s-exp->list (second xs))))]))]))

(parse-Racket-Exp `(cond ((1 (let ((x 1) (y 2)) (app (lambda (x y z) (if 1 x 1)) (1 1 1)))) (x 1))))
