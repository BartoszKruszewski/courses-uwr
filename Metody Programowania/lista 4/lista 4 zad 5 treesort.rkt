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

(define example-tree
  (node (node (leaf) 1 (leaf))
        2
        (node (node (leaf) 3 (leaf))
              4
              (leaf))))

(define (insert-bst x t)
  (cond [(leaf? t) (node (leaf) x (leaf))]
        [(node? t)
         (cond [(<= x (node-elem t))
                 (node (insert-bst x (node-l t))
                       (node-elem t)
                       (node-r t))]
                [else
                 (node (node-l t)
                       (node-elem t)
                       (insert-bst x (node-r t)))])]))

(define (flatten t)
  (define (flat-append t xs)
  (if (leaf? t)
      xs
      (flat-append (node-l t) (cons (node-elem t) (flat-append (node-r t) xs)))))
  (flat-append t '()))

(define (treesort l)
  (define (it t l)
    (if (null? l)
        t
        (it (insert-bst (first l) t) (rest l))))
  (flatten (it (leaf) l)))

(treesort '(15 4 2 18 9 5))
  


