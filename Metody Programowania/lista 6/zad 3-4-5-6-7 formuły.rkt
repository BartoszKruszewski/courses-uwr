#lang plait

(define-type (NNF 'v)
   (nnf-lit [polarity : Boolean ] [var : 'v ])
   (nnf-conj [l : (NNF 'v)] [r : (NNF 'v) ])
   (nnf-disj [l : (NNF 'v)] [r : (NNF 'v) ]) )

; Zasada Indukcji dla NNF
; Niech P będzie własnością formuły φ typu NNF, taką że
; (i) Dla φ będącego lit zachodzi P(φ)
; (ii) Dla φ będącego conj zakładając P(l) i P(r) zachodzi P(φ)
; (iii) Dla φ będącego disj zakładając P(l) i P(r) zachodzi P(φ)
; Wówczas dla dowlnego φ zachodzi P(φ)

(define (neg-nnf formula)
  (cond [(nnf-lit? formula) (nnf-lit (not (nnf-lit-polarity formula)) (nnf-lit-var formula))]
        [(nnf-conj? formula) (nnf-disj (neg-nnf (nnf-conj-l formula)) (neg-nnf (nnf-conj-r formula)))]
        [(nnf-disj? formula) (nnf-conj (neg-nnf (nnf-disj-l formula)) (neg-nnf (nnf-disj-r formula)))]))

(define example-formula-nnf (nnf-conj (nnf-lit #t 'p) (nnf-disj (nnf-lit #f 'p) (nnf-lit #t 'q))))

;(neg-nnf (neg-nnf example-formula-nnf))


; Indukcja względem φ
; P(φ) := (neg-nnf (neg-nnf φ)) ≡ φ
;
; (i) (neg-nnf (neg-nnf lit)) ≡
;     (neg-nnf (lit (not polarity) var)) ≡
;     (lit (not (not polarity)) var) ≡
;     (lit polarity var) ≡ lit
;
; (ii) zał. (neg-nnf (neg-nnf l)) ≡ l i (neg-nnf (neg-nnf r)) ≡ r
;
;     (neg-nnf (neg-nnf conj)) ≡
;     (neg-nnf (disj (neg-nnf l) (neg-nnf r)) ≡
;     (conj (neg-nnf (neg-nnf l)) (neg-nnf (neg-nnf r))) ≡
;     (conj l r) ≡ conj
;
; (iii) analogicznie jak (ii)
;
; więc (neg-nnf (neg-nnf φ)) ≡ φ dla dowolnego φ

(define (eval-nnf valuation formula)
  (cond [(nnf-lit? formula) (if (nnf-lit-polarity formula) (valuation (nnf-lit-var formula)) (not (valuation (nnf-lit-var formula))))]
        [(nnf-conj? formula) (and (eval-nnf valuation (nnf-conj-l formula)) (eval-nnf valuation (nnf-conj-r formula)))]
        [(nnf-disj? formula) (or (eval-nnf valuation (nnf-disj-l formula)) (eval-nnf valuation (nnf-disj-r formula)))]))

(define (example-valuation x)
  (cond [(equal? x 'x) #t]
        [(equal? x 'y) #f]
        [(equal? x 'a) #f]
        [(equal? x 'b) #t]))

; Indukcja względem φ
; P(φ) := (eval-nnf σ (neg-nnf φ)) ≡ (not (eval-nnf σ φ))
;
; (i) L ≡ (eval-nnf σ (neg-nnf lit)) ≡
;     (eval-nnf σ (lit (not polarity) var)) ≡
;     (not (σ lit))
;     P ≡ (not (eval-nnf σ lit)) ≡
;     (not (σ lit))
;
; (ii) zał. (eval-nnf σ (neg-nnf l)) ≡ (not (eval-nnf σ l) i (eval-nnf σ (neg-nnf r)) ≡ (not (eval-nnf σ r)
;      Do udowodnienia: (eval-nnf σ (neg-nnf conj)) ≡ (not (eval-nnf σ conj))
;
;     L ≡ (eval-nnf σ (neg-nnf conj)) ≡
;     (eval-nnf σ (disj (neg-nnf l) (neg-nnf r))) ≡
;     (or (eval-nnf σ (neg-nnf l)) (eval-nnf σ (neg-nnf r))) ≡
;     (or (not (eval-nnf σ l) (not (eval-nnf σ r)) ≡
;     P ≡ (not (eval-nnf σ conj)) ≡
;     (not (and (eval-nnf σ l) (eval-nnf σ r))) ≡
;     (or (not (eval-nnf σ l) (not (eval-nnf σ r))
;
; (iii) analogicznie jak (ii)
;
; więc (eval-nnf σ (neg-nnf φ)) ≡ (not (eval-nnf σ φ))

(define-type (Formula 'v)
  (var [var : 'v ])
  (neg [f : (Formula 'v) ])
  (conj [l : (Formula 'v)] [r : (Formula 'v)])
  (disj [l : (Formula 'v)] [r : (Formula 'v)]))

(define (to-nnf formula)
  (cond
    [(var? formula) (nnf-lit #t (var-var formula))]  
    [(conj? formula) (nnf-conj (to-nnf (conj-l formula)) (to-nnf (conj-r formula)))]
    [(disj? formula) (nnf-disj (to-nnf (disj-l formula)) (to-nnf (disj-r formula)))]
    [(neg? formula)
     (let ((f (neg-f formula)))
       (cond
         [(var? f) (nnf-lit #f (var-var f))]
         [(neg? f) (to-nnf (neg-f f))]
         [(conj? f) (nnf-disj (neg-nnf (to-nnf (conj-l f))) (neg-nnf (to-nnf (conj-r f))))]
         [(disj? f) (nnf-conj (neg-nnf (to-nnf (disj-l f))) (neg-nnf (to-nnf (disj-r f))))]))]))

(define (eval-formula valuation formula)
  (cond
    [(var?  formula) (valuation (var-var formula))]
    [(conj? formula) (and (eval-formula valuation (conj-l formula)) (eval-formula valuation (conj-r formula)))]
    [(disj? formula) (or (eval-formula valuation (disj-l formula)) (eval-formula valuation (disj-r formula)))]
    [(neg? formula) (not (eval-formula valuation (neg-f formula)))]))

(define example-formula (neg (neg (neg (conj (var 'x) (disj (var 'a) (var 'y)))))))

; Zasada Indukcji dla Formuł
; Niech P będzie własnością formuły φ, taką że
; (i) Dla φ będącego var zachodzi P(φ)
; (ii) Dla φ będącego conj zakładając P(l) i P(r) zachodzi P(φ)
; (iii) Dla φ będącego disj zakładając P(l) i P(r) zachodzi P(φ)
; (iv) Dla φ będącego neg zakładając P(f) zachodzi P(φ)
; Wówczas dla dowlnego φ zachodzi P(φ)
; 
; Lemat 1.:
; Dla dowolnego wartościowania σ: (nnf-lit-var nnf-lit) = (var-var var) => (σ nnf-lit) ≡ (σ var)
; Dowód:
; L ≡ (σ nnf-lit) ≡ (σ (nnf-lit-var nnf-lit)) = (σ (var-var var)) 
; P ≡ (σ var) ≡ (σ (var-var var)) 
;
; Indukcja względem φ
; P := (eval-nnf σ (to-nnf φ)) ≡ (eval-formula σ φ)
;
;
; (i) Do udowodnienia: (eval-nnf σ (to-nnf var)) ≡ (eval-formula σ var)
;
;     L ≡ (eval-nnf σ (to-nnf var)) ≡
;     (eval-nnf σ nnf-lit) ≡ (σ nnf-lit)
;     P ≡ (eval-formula σ var) ≡ (σ var)
;     Równość z Lematu 1.
;
; (ii) zał. (eval-nnf σ (to-nnf l)) ≡ (eval-formula σ l) i (eval-nnf σ (to-nnf r)) ≡ (eval-formula σ r)
;      Do udowodnienia: (eval-nnf σ (to-nnf conj)) ≡ (eval-formula σ conj)
;
;      L ≡ (eval-nnf σ (to-nnf conj)) ≡
;      (eval-nnf σ (nnf-conj (to-nnf l) (to-nnf r))) ≡
;      (and (eval-nnf σ (to-nnf l)) (eval-nnf σ (to-nnf r))) ≡
;      (and (eval-formula σ l) (eval-formula σ r))
;      P ≡ (eval-formula σ conj) ≡
;      (and (eval-formula σ l) (eval-formula σ r))
;
; (iii) analogicznie jak (ii)
;
; (iv) zał. (eval-nnf σ (to-nnf f)) ≡ (eval-formula σ f)
;      Do udowodnienia: (eval-nnf σ (to-nnf neg)) ≡ (eval-formula σ neg)
;
;      1. f = var:
;         L ≡ (eval-nnf σ (to-nnf neg)) ≡
;         (eval-nnf σ (lit (not polarity))) ≡
;         (not (σ lit))
;         P ≡ (eval-formula σ neg) ≡
;         (not (eval-formula σ var)) ≡
;         (not (σ var))
;         Równość z Lematu 1.
;
;      2. f = conj:
;         L ≡ (eval-nnf σ (to-nnf neg)) ≡
;         (eval-nnf σ (nnf-disj (neg-nnf nnf-l) (neg-nnf nnf-r))) ≡
;         (or (eval-nnf σ (neg-nnf (to-nnf l))) (eval-nnf σ (neg-nnf (to-nnf r)))) ≡
;         z poprzedniego zadania: (eval-nnf σ (neg-nnf φ)) ≡ (not (eval-nnf σ φ))
;         (or (not (eval-nnf σ (to-nnf l))) (not (eval-nnf σ (to-nnf r)))) ≡
;         (or (not (eval-formula σ l)) (not (eval-formula σ r)))
;         P ≡ (eval-formula σ neg) ≡
;         (not (and (eval-formula σ l) (eval-formula σ r)))
;         (or (not (eval-formula σ l)) (not (eval-formula σ r)))
;
;      3. f = disj analogicznie jak f = conj
;
;      4. f = neg rozpatrujemy powyższe przypadki aż dojdziemy do sytuacji w której f ≠ neg
;         
; więc (eval-nnf σ (to-nnf φ)) ≡ (eval-formula σ φ)       