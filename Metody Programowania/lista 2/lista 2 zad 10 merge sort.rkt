#lang racket

(define (split l)
  (define (it l1 l2 l)
    (if (null? l)
        (cons l1 l2)
        (if (null? (rest l))
            (cons (append (list (first l)) l1) l2)
            (it (append (list (first l)) l1) (append (list (second l)) l2) (cddr l)))))
  (it '() '() l))

(define (merge l1 l2)
  (define (it l1 l2 l)
    (if (null? l1)
        (append l l2)
        (if (null? l2)
            (append l l1)
            (if (< (first l1) (first l2))
                (it (rest l1) l2 (append l (list (first l1))))
                (it l1 (rest l2) (append l (list (first l2))))))))
  (it l1 l2 '()))

(define (merge-sort l)
  (if (null? (rest l))
      l
      (let ((s (split l))) (merge (merge-sort (first s)) (merge-sort (rest s))))))

(merge-sort (list 7 8 37 15 18 9 11))

  