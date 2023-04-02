#lang plait

(define-type (Tree 'a)
  (leaf [elem : 'a])
  (node [childs : (Listof (Tree 'a))]))

(define (tree-flatten t)
  (if (leaf? t) (list (leaf-elem t))
      (flatten (map (lambda (child) (tree-flatten child)) (node-childs t)))))

(define (flatten lst)
  (if (empty? lst) '()
      (append (first lst) (flatten (rest lst)))))

(define t1 (node (list
                  (node (list
                         (leaf 1)
                         (leaf 2)
                         (leaf 3)))
                  (leaf 4)
                  (leaf 5)
                  (leaf 6)
                  (node (list
                         (leaf 7)
                         (leaf 8)
                         (leaf 9))))))

(tree-flatten t1)
