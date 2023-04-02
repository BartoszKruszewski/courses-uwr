#lang plait

(define-type Prop
   (var [v : String ])
   (conj [l : Prop ] [r : Prop ])
   (disj [l : Prop ] [r : Prop ])
   (neg [f : Prop ]))

(define (eval [h : (Hashof String Boolean)] [p : Prop])
  (cond
    [(var?  p) (some-v (hash-ref h (var-v p)))]
    [(conj? p) (and (eval h (conj-l p)) (eval h (conj-r p)))]
    [(disj? p) (or (eval h (disj-l p)) (eval h (disj-r p)))]
    [(neg? p) (not (eval h (neg-f p)))]))

(define h (hash (list (pair "x" #t) (pair "y" #f))))

(eval h (conj (var "x") (var "y")))
(eval h (disj (var "x") (var "y")))
(eval h (conj (disj (var "x") (neg (var "x"))) (var "y")))
