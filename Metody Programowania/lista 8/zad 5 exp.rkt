#lang plait

(define-type Op-dual
  (op-add) (op-mul) (op-sub) (op-div) (op-pow))

(define-type Op-single
  (op-fact) (op-opp))

(define-type Exp
  (exp-number [n : Number])
  (exp-op-single [op : Op-single] [e : Exp])
  (exp-op-dual [op : Op-dual] [e1 : Exp] [e2 : Exp]))

(define (parse-Op-single s)
  (let ([sym (s-exp->symbol s)])
  (cond
    [(equal? sym '!) (op-fact)]
    
    [(equal? sym '-) (op-opp)])))

(define (parse-Op-dual s)
  (let ([sym (s-exp->symbol s)])
  (cond
    [(equal? sym '+) (op-add)]
    [(equal? sym '-) (op-sub)]
    [(equal? sym '*) (op-mul)]
    [(equal? sym '/) (op-div)]
    [(equal? sym '^) (op-pow)])))

(define (parse-Exp s)
  (cond
    [(s-exp-number? s) (exp-number (s-exp->number s))]
    [(s-exp-list? s)
     (let ([xs (s-exp->list s)])
       (if (= 3 (length xs))
           (exp-op-dual (parse-Op-dual  (first  xs))
                        (parse-Exp (second xs))
                        (parse-Exp (third  xs)))
           (exp-op-single (parse-Op-single  (first  xs))
                          (parse-Exp (second xs)))))]))

; ==============================================

(define (pow a b)
  (if (= b 0)
      1
      (* a (pow a (- b 1)))))

(define (fact n)
  (if (= n 0)
      1
      (* n (fact (- n 1)))))

(define (opp n)
  (* n -1))

(define (eval-op-dual op)
  (type-case Op-dual op
    [(op-add) +]
    [(op-sub) -]
    [(op-mul) *]
    [(op-div) /]
    [(op-pow) pow]))

(define (eval-op-single op)
  (type-case Op-single op
    [(op-fact) fact]
    [(op-opp) opp]))

(define (eval e)
  (type-case Exp e
    [(exp-number n) n]
    [(exp-op-dual op e1 e2)
     ((eval-op-dual op) (eval e1) (eval e2))]
    [(exp-op-single op e)
     ((eval-op-single op) (eval e))]))

(eval (parse-Exp `(- (^ 2 7))))
