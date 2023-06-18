#lang plait
(define-type (Tree 'a)
  (leaf)
  (node2 [l : (Tree 'a)] [r : (Tree 'a)] [e : 'a])
  (node3 [l : (Tree 'a)] [r : (Tree 'a)] [s : (Tree 'a)] [a : 'a] [b : 'a]))

(define (min-value tree)
  (type-case (Tree 'a) tree 
    [(leaf) +inf.0]
    [(node2 l r e) (min-list (list e (min-value l) (min-value r)))]
    [(node3 l r s a b) (min-list (list a b (min-value l) (min-value r) (min-value s)))]))

(define (min-list xs)
  (if (empty? (rest xs)) (first xs)
      (min (first xs) (min-list (rest xs)))))

(define (max-value tree)
  (type-case (Tree 'a) tree 
    [(leaf) -inf.0]
    [(node2 l r e) (max-list (list e (max-value l) (max-value r)))]
    [(node3 l r s a b) (max-list (list a b (max-value l) (max-value r) (max-value s)))]))

(define (max-list xs)
  (if (empty? (rest xs)) (first xs)
      (max (first xs) (max-list (rest xs)))))

(define (max-path tree)
    (type-case (Tree 'a) tree 
    [(leaf) 0]
    [(node2 l r e) (+ 1 (max (max-path l) (max-path r)))]
    [(node3 l r s a b) (+ 1 (max-list (list (max-path l) (max-path r) (max-path s))))]))

(define (min-path tree)
    (type-case (Tree 'a) tree 
    [(leaf) 0]
    [(node2 l r e) (+ 1 (min (min-path l) (min-path r)))]
    [(node3 l r s a b) (+ 1 (min-list (list (min-path l) (min-path r) (min-path s))))]))

(define (and-list xs)
  (if (empty? (rest xs)) (first xs)
      (and (first xs) (and-list (rest xs)))))

(define (tree? tree)
  (and (= (max-path tree) (min-path tree)) 
      (type-case (Tree 'a) tree 
        [(leaf) #t]
        [(node2 l r e) (and-list (list
                                  (>= e (max-value l))
                                  (<= e (min-value r))
                                  (tree? l)
                                  (tree? r)))]
        [(node3 l r s a b) (and-list (list
                                      (>= a (max-value l))
                                      (<= b (min-value r))
                                      (<= a b)
                                      (>= b (max-value s))
                                      (<= a (min-value s))
                                      (tree? l)
                                      (tree? r)
                                      (tree? s)))])))

(define example-tree (node3 (node2 (leaf) (leaf) 1) (node2 (leaf) (leaf) 5) (node2 (leaf) (leaf) 3) 2 4))

(tree? example-tree)