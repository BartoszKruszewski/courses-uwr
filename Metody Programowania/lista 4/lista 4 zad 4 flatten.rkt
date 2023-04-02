#lang racket

(define-struct leaf () #:transparent)
(define-struct node (l elem r) #:transparent)

(define (tree? x)
  (cond [(leaf? x) #t]
        [(node? x) (and (tree? (node-l x))
                        (tree? (node-r x)))]
        [else #f]))

(define (tree-node l elem r)
  (if (and (tree? l) (tree? r) (number? elem))
      (node l elem r)
      (error "nieprawidłowe pola węzła")))

(define (tree-alt? x)
  (or (leaf? x)
      (and (node? x)
           (tree-alt? (node-l x))
           (tree-alt? (node-r x)))))

(define (flatten t)
  (define (flat-append t xs)
  (if (leaf? t)
      xs
      (flat-append (node-l t) (cons (node-elem t) (flat-append (node-r t) xs)))))
  (flat-append t '()))
 
(define t1
  (node (node (leaf) 1 (leaf))
        2
        (node (node (leaf) 3 (leaf))
              5
              (node (node (leaf) 11 (leaf))
                    7
                    (leaf)))))

(flatten t1)

