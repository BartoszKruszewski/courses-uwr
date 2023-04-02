#lang racket

(define empty-queue (cons null null))

(define (empty? q) (null? (car q)))

(define (update q)
  (if (and (null? (car q)) (not (null? (cdr q))))
      (cons (reverse (cdr q)) null)
      q))

(define (push-back x q)
  (update
   (cons (car q) (cons x (cdr q)))))

(define (front q) (car (car q)))

(define (pop q)
  (update
   (cons (cdr (car q)) (cdr q))))

(define q1 empty-queue)

(empty? q1)

(define q2 (push-back 1 q1))
(define q3 (push-back 2 q2))
(define q4 (push-back 3 q3))
(define q5 (push-back 4 q4))
(define q6 (push-back 5 q5))
(define q7 (pop q6))

q6
q7