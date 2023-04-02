#lang plait

(define (perms lst)
  (no-repeat-list (perms-repeats lst)))

(define (perms-repeats lst)
  (if (empty? lst) '(())
        (flatten (map (lambda (x) (map (lambda (y) (cons x y)) (perms (remove x lst)))) lst))))

(define (flatten lst)
  (if (empty? lst) '()
      (append (first lst) (flatten (rest lst)))))

(define (remove x l)
  (if (equal? x (first l))
      (rest l)
      (append (list (first l)) (remove x (rest l)))))

(define (no-repeat-list l)
  (local [(define (it l nl)
    (if (empty? l)
        nl
        (it (rest l) (append nl (if (member (first l) nl) '() (list (first l)))))))]
  (it l '())))

(perms '(1 1 1))