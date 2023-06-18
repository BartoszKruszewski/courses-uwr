#lang racket

(provide
 mqueue?
 nonempty-mqueue?
 (contract-out
   [mqueue-empty?     (-> mqueue? boolean?)]
   [make-mqueue       (-> mqueue?)]
   [mqueue-push-front (-> mqueue? any/c void?)]
   [mqueue-push-back  (-> mqueue? any/c void?)]
   [mqueue-pop-front  (-> mqueue? any/c)]
   [mqueue-pop-back   (-> mqueue? any/c)]
   [print-mqueue      (-> mqueue? void?)]
   [mqueue-join       (-> nonempty-mqueue? nonempty-mqueue? void?)]))


(struct mqueue
  ([front #:mutable]
   [back  #:mutable]))

(struct node
  ([prev #:mutable]
   [value #:mutable]
   [next #:mutable]))

(define (mqueue-empty? q)
  (and (null? (mqueue-front q))
       (null? (mqueue-back  q))))

(define (nonempty-mqueue? q)
  (and (mqueue? q) (node? (mqueue-front q))))

(define (make-mqueue)
  (mqueue null null))

(define (mqueue-push-back q x)
  (define p (node (mqueue-back q) x null))
  (if (mqueue-empty? q)
      (set-mqueue-front! q p)
      (set-node-next! (mqueue-back q) p))
  (set-mqueue-back! q p))

(define (mqueue-push-front q x)
  (define p (node null x (mqueue-front q)))
  (if (mqueue-empty? q)
      (set-mqueue-back! q p)
      (set-node-prev! (mqueue-front q) p))
  (set-mqueue-front! q p))

(define/contract (mqueue-pop-front q)
  (-> nonempty-mqueue? any/c)
  (define p (mqueue-front q))
  (set-mqueue-front! q (node-next p))
  (set-node-prev! (mqueue-front q) null)
  (if (null? (node-next p))
      (begin (set-mqueue-back! q null) (node-value p))
      (node-value p)))

(define/contract (mqueue-pop-back q)
  (-> nonempty-mqueue? any/c)
  (define p (mqueue-back q))
  (set-mqueue-back! q (node-prev p))
  (set-node-next! (mqueue-back q) null)
  (if (null? (node-prev p))
      (begin (set-mqueue-front! q null) (node-value p))
      (node-value p)))

(define (mqueue-join q1 q2)
  (set-node-next! (mqueue-back q1) (mqueue-front q2))
  (set-node-prev! (mqueue-front q2) (mqueue-back q1))
  (set-mqueue-back! q1 (mqueue-back q2))
  (set-mqueue-front! q2 null)
  (set-mqueue-back!  q2 null))

(define (print-mqueue q)
  (printf "<")
  (define (helper node)
    (if (null? (node-next node)) (print (node-value node))
        (begin (print (node-value node)) (printf ", ") (helper (node-next node)))))
  (helper (mqueue-front q))
  (printf ">"))





