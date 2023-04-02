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

(define t1
  (node (node (leaf) 1 (leaf))
        2
        (node (node (leaf) 3 (leaf))
              5
              (node (node (leaf) 7 (leaf))
                    11
                    (leaf)))))

(define t2
  (node (node (leaf) 1 (leaf))
        2
        (node (leaf) 3 (leaf))))

(define (bst? t)
  (or (leaf? t)
      (and
       (or (and (leaf? (node-l t)) (leaf? (node-r t)))
           (and (leaf? (node-r t)) (< (node-elem (node-l t)) (node-elem t)))
           (and (leaf? (node-l t)) (> (node-elem (node-r t)) (node-elem t)))
           (and (< (node-elem (node-l t)) (node-elem t)) (> (node-elem (node-r t)) (node-elem t))))
           (bst? (node-l t))
           (bst? (node-r t)))))

(define (sum-paths t)
  (define (it t sum)
    (if (leaf? t)
        (leaf)
        (let ((s (+ sum (node-elem t))))
        (node (it (node-l t) s)
              s
              (it (node-r t) s)))))
  (it t 0))
  

(node-elem (node-r t2))
(bst? t1)
(sum-paths (leaf))
(pretty-print (sum-paths t1))