#lang plait

(module+ test
  (print-only-errors #t))

;; abstract syntax -------------------------------

(define-type Op
  (add) (sub) (mul))

(define-type Exp
  (numE [n : Number])
  (opE [op : Op] [e1 : Exp] [e2 : Exp])
  (varE [x : Symbol])
  (lamE [x : Symbol] [e : Exp])
  (appE [e0 : Exp] [e1 : Exp])
  (writeE [e : Exp])
  (beginE [e1 : Exp] [e2 : Exp]))

(define-type-alias Output (Listof Number))
(define-type-alias (M 'a) ('a * Output))

;; semantics: the identity monad and values

(define (returnM [v : 'a]) : (M 'a)
  (values v empty))

(define (bindM [c : (M 'a)] [f : ('a -> (M 'b))]) : (M 'b)
  (let ([v1 (fst c)] [out1 (snd c)])
    (let* ([n (f v1)] [v2 (fst n)] [out2 (snd n)])
      (values v2 (append out2 out1)))))

(define (errorM [l : Symbol] [m : String]) : (M 'a)
  (error l m))

(define (showM [c : (M Value)]) : String
  (let ([v (fst c)] [out (snd c)])
     (string-append "value: "
                    (string-append (value->string v)
                                   (string-append " , output: " (output->string out))))))

(define-type Value
  (numV [n : Number])
  (funV [f : (Value -> (M Value))])
  (voidV))

(define (value->string [v : Value]) : String
  (type-case Value v
    [(numV n) (to-string n)]
    [(funV _) "#<procedure>"]
    [(voidV) "#<void>"]))

(define (output->string [out : Output]) : String
  (let ([s (foldr (lambda (x a) (string-append a (string-append (to-string x) " "))) "" out)])
    (if (= (string-length s) 0) ""
        (substring s 0 (- (string-length s) 1)))))

;; environments

(define-type Binding
  (bind [name : Symbol]
        [val : Value]))

(define-type-alias Env (Listof Binding))

(define mt-env empty)

(define (extend-env [env : Env] [x : Symbol] [v : Value]) : Env
  (cons (bind x v) env))

(define (lookup-env [x : Symbol] [env : Env]) : (M Value)
  (type-case (Listof Binding) env
    [empty
     (errorM 'lookup-env "unbound variable")]
    [(cons b rst-env)
     (cond
       [(eq? x (bind-name b))
        (returnM (bind-val b))]
       [else
        (lookup-env x rst-env)])]))

;; primitive operations

(define (op-num-num->proc [f : (Number Number -> Number)]) : (Value Value -> (M Value))
  (λ (v1 v2)
    (type-case Value v1
      [(numV n1)
       (type-case Value v2
         [(numV n2)
          (returnM (numV (f n1 n2)))]
         [else
          (errorM 'prim-op "not a number")])]
      [else
       (errorM 'prim-op "not a number")])))

(define (op->proc [op : Op]) : (Value Value -> (M Value))
  (type-case Op op
    [(add) (op-num-num->proc +)]
    [(sub) (op-num-num->proc -)]
    [(mul) (op-num-num->proc *)]))

;; evaluation function (eval/apply)

(define (eval [e : Exp] [env : Env]) : (M Value)
  (type-case Exp e
    [(numE n)
     (returnM (numV n))]
    [(opE o e1 e2)
     (bindM (eval e1 env)
            (λ (v1) (bindM (eval e2 env)
                           (λ (v2) ((op->proc o) v1 v2)))))]
    [(varE x)
     (lookup-env x env)]
    [(lamE x b)
     (returnM (funV (λ (v) (eval b (extend-env env x v)))))]
    [(appE e0 e1)
     (bindM (eval e0 env)
            (λ (v0) (bindM (eval e1 env)
                           (λ (v1) (apply v0 v1)))))]
    [(writeE e)
     (bindM (eval e env)
            (λ (v) (pair (voidV) (list (numV-n v)))))]
    [(beginE e1 e2)
     (bindM (eval e1 env)
            (λ (v1) (bindM (eval e2 env)
                           (λ (v2) (pair v2 empty)))))]))

(define (apply [v0 : Value] [v1 : Value]) : (M Value)
  (type-case Value v0
    [(funV f) (f v1)]
    [else (errorM 'apply "not a function")]))

(define (run [e : S-Exp]) : String
  (showM (eval (parse e) mt-env)))


;; parse ----------------------------------------

(define (parse [s : S-Exp]) : Exp
  (cond
    [(s-exp-match? `NUMBER s)
     (numE (s-exp->number s))]
    [(s-exp-match? `{lambda {SYMBOL} ANY} s)
     (lamE (s-exp->symbol
            (first (s-exp->list 
                    (second (s-exp->list s)))))
           (parse (third (s-exp->list s))))]
    
    [(s-exp-match? `(write ANY) s)
     (writeE (parse (second (s-exp->list s))))]
    [(s-exp-match? `(begin ANY ANY) s)
     (beginE (parse (second (s-exp->list s)))
             (parse (third (s-exp->list s))))]
    [(s-exp-match? `SYMBOL s)
     (varE (s-exp->symbol s))]
    [(s-exp-match? `{SYMBOL ANY ANY} s)
     (opE (parse-op (s-exp->symbol (first (s-exp->list s))))
          (parse (second (s-exp->list s)))
          (parse (third (s-exp->list s))))]
    [(s-exp-match? `{ANY ANY} s)
     (appE (parse (first (s-exp->list s)))
           (parse (second (s-exp->list s))))]
    [else (begin (display s) (error 'parse "invalid input"))]))

(define (parse-op [op : Symbol]) : Op
  (cond
    [(eq? op '+) (add)]
    [(eq? op '-) (sub)]
    [(eq? op '*) (mul)]
    [else (error 'parse "unknown operator")]))

(run `{write {{lambda {x} {begin {write x} {+ x 1}}} 5}})

(module+ test
  (test (run `{+ {* 2 3} {+ 5 8}})
        "value: 19 , output: ")
  (test/exn (run `{1 2})
            "not a function")
  (test (run `{write {{lambda {x} {begin {write x} {+ x 1}}} 5}})
        "value: #<void> , output: 5 6"))
