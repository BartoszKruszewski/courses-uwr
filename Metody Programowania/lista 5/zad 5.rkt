#lang plait

(define-type (Tree 'a)
  (leaf)
  (node [l : (Tree 'a)] [elem : 'a] [r : (Tree 'a)]))

(define example-tree
  (node (node (leaf) 1 (leaf))
        2
        (node (leaf)
              3
              (node (leaf) 4 (leaf)))))

(define (process-tree f-node f-leaf f-left f-right acc tree)
  (if (leaf? tree)
      (f-leaf acc)
      (f-node acc
              (process-tree f-node f-leaf f-left f-right (f-left acc (node-elem tree)) (node-l tree))
              (node-elem tree)
              (process-tree f-node f-leaf f-left f-right (f-right acc (node-elem tree)) (node-r tree)))))

(define (bst? tree)
    (process-tree
        (lambda (acc l val r) (and (<= (fst acc) val) (> (snd acc) val) l r))
        (lambda (leaf) #t)
        (lambda (acc v) (pair (fst acc) v))
        (lambda (acc v) (pair v (snd acc)))
        (pair -inf.0 +inf.0)
        tree
    )
)

(define (sum-paths tree)
    (process-tree
        (lambda (acc l val r) (node l (+ acc val) r))
        (lambda (x) (leaf))
        (lambda (acc elem) (+ acc elem))
        (lambda (acc elem) (+ acc elem))
        0
        tree
    )
)


(sum-paths example-tree)
