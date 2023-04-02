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
              5
              (node (node (leaf) 11 (leaf))
                    7
                    (leaf)))))

(define t1
  (node (node (leaf) 1 (leaf))
        2
        (node (leaf) 3 (leaf))))
              

(define (fold-tree f acc tree)
  (if (leaf? tree)
      acc
      (f (node-elem tree) (fold-tree f acc (node-l tree)) (fold-tree f acc (node-r tree)))))

(define (tree-sum t) (fold-tree + 0 t))

(define (tree-reverse t) (fold-tree (lambda (e l r) (tree-node r e l)) (leaf) t))

(define (tree-height t)
  (fold-tree (lambda (e l r) (+ 1 (max l r))) 0 t))

(define (tree-span t)
  (fold-tree (lambda (e l r)
               (cons (if (leaf? (car l)) e (car l))
                     (if (leaf? (cdr r)) e (cdr r))))
             (cons (leaf) (leaf)) t)) 

(define (flatten t)
  (fold-tree (lambda (e l r) (append l (cons e r))) '() t)) 
   

(tree-sum example-tree)

(tree-reverse example-tree)

(tree-height example-tree)

(tree-span example-tree)

(flatten example-tree)

  