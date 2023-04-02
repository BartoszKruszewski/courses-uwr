#lang racket

(define (list->llist l) (lambda (x) (append l x)))

(define (llist->list f) (f '()))

(define (llist-null) (lambda (x) x))

(define (llist-singleton a) (lambda (x) (cons a x)))

(define (llist-append f g) (lambda (x) (f (g x))))

(define (foldr-llist-reverse l)
   (llist->list (foldr (lambda (x y) (llist-append y (llist-singleton x))) (llist-null) l)))

(define f (list->llist '(1 2)))
(define g (llist-singleton 5))
(define h (llist-append f g))

(f '(3 4))
(g '(3 4))
(h '(3 4))

(llist->list f)
(foldr-llist-reverse '(1 2 3 4 5 6 7 8 9 10))