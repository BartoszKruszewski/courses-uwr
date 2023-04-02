#lang plait

(define-type Prop
   (var [v : String ])
   (conj [l : Prop ] [r : Prop ])
   (disj [l : Prop ] [r : Prop ])
   (neg [f : Prop ]))

(define (tautology? p)
  (all-true? (map (lambda (val) (eval val p)) (make-all-val-hash p))))

(define (all-true? l)
  (local [(define (it l acc)
          (if (empty? l) acc
              (it (rest l) (and acc (first l)))))]
    (it l #t)))

(define (make-all-val-hash p)
  (make-hash-list (free-vars p) (all-valuations p)))
  
(define (make-hash-list vars vals)
  (map (lambda (val) (hash (make-pair-list vars val))) vals))

(define (make-pair-list l1 l2)
  (local [(define (it l1 l2 nl)
            (if (empty? l1) nl
                (it (rest l1) (rest l2) (cons (pair (first l1) (first l2)) nl))))]
    (it l1 l2 '())))

(define (all-valuations [p : Prop])
  (all-variations '(#t #f) (list-len (free-vars p))))

(define (list-len l)
  (local [(define (it l k)
          (if (empty? l) k
              (it (rest l) (+ k 1))))]
    (it l 0)))


(define (all-variations lst k)
  (if (= k 0) '(())
      (flatten (map (lambda (x) (map (lambda (y) (cons x y)) (all-variations lst (- k 1)))) lst))))

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

(define (eval [h : (Hashof String Boolean)] [p : Prop])
  (cond
    [(var?  p) (some-v (hash-ref h (var-v p)))]
    [(conj? p) (and (eval h (conj-l p)) (eval h (conj-r p)))]
    [(disj? p) (or (eval h (disj-l p)) (eval h (disj-r p)))]
    [(neg? p) (not (eval h (neg-f p)))]))

(define p1 (conj (disj (var "x") (neg (var "z"))) (var "y"))) ;
(define p2 (disj (neg (var "x")) (var "x"))) ; x | ~x
(define p3 (conj (neg (var "x")) (var "x"))) ; x & ~x
(define p4 (conj
            (disj (neg (var "x")) (var "x"))
            (disj (neg (var "y")) (var "y")))) ; (x | ~x) & (y | ~y)

(tautology? p1)
(tautology? p2)
(tautology? p3)
(tautology? p4)

