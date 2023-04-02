#lang racket

(( lambda (x y) (+ x (* x y))) 1 2) ; 3

(( lambda (x) x) ( lambda (x) x)) ; zwraca funkcje lambda (x) x

(( lambda (x) (x x)) ( lambda (x) x)) ; zwraca funkcje lambda (x) x z argumentem funkcja lambda (x) x

(( lambda (x) (x x)) ( lambda (x) (x x))) ; tak jak poprzedni podpunkt tylko się zapętla