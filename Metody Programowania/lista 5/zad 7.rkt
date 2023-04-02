#lang plait

(define-type Prop
   (var [v : String ])
   (conj [l : Prop ] [r : Prop ])
   (disj [l : Prop ] [r : Prop ])
   (neg [f : Prop ]))

(define (free-vars [p : Prop] )
  (no-repeat-list (all-vars p)))

(define (no-repeat-list l)
  (local [(define (it l nl)
    (if (empty? l)
        nl
        (it (rest l) (append nl (if (member (first l) nl) '() (list (first l)))))))]
  (it l '())))

(define (all-vars [p : Prop])
  (cond
    [(var?  p) (list (var-v p))]
    [(conj? p) (flatten (list (all-vars (conj-l p)) (all-vars (conj-r p))))]
    [(disj? p) (flatten (list (all-vars (disj-l p)) (all-vars (disj-r p))))]
    [(neg? p) (flatten (list (all-vars (neg-f p))))]))

(define (flatten lst)
  (if (empty? lst) '()
      (append (first lst) (flatten (rest lst)))))

(free-vars (conj (disj (var "x") (neg (var "x"))) (var "y")))