#lang racket
(provide run-parser)

(define (match-type pat s)
  (match pat
    ['ANY    (list s)]
    ['SYMBOL (and (symbol? s) (list s))]
    ['NUMBER (and (number? s) (list s))]
    ['()     (and (null? s)   null)]
    [(cons p1 p2)
     (and (pair? s)
          (let ([r1 (match-type p1 (car s))])
            (and r1
                 (let ([r2 (match-type p2 (cdr s))])
                   (and r2 (append r1 r2))))))]
    [_
     (cond
       [(symbol? pat) (and (symbol? s) (eq? pat s) null)])]))

(define (run-parser p s)
  (match p
    ['() (error "Syntax error")]
    [(cons (list pat action) rest-p)
     (let ([r (match-type pat s)])
       (if r
           (apply action r)
           (run-parser rest-p s)))]))
