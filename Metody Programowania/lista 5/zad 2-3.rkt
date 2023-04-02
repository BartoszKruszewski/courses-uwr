#lang plait

; zad 2

( define ( apply f x) (f x)) ; (('a -> 'b) 'a -> 'b)
( define ( compose f g) ( lambda (x) (f (g x)))) ; (('a -> 'b) ('c -> 'a) -> ('c -> 'b))
( define ( flip f) ( lambda (x y) (f y x))) ; (('a 'b -> 'c) -> ('b 'a -> 'c))
( define ( curry f) ( lambda (x) ( lambda (y) (f x y)))) ; (('a 'b -> 'c) -> ('a -> ('b -> 'c)))

; zad 3

( curry compose ) ; (('_a -> '_b) -> (('_c -> '_a) -> ('_c -> '_b)))
(( curry compose ) ( curry compose )) ; (('_a -> ('_b -> '_c)) -> ('_a -> (('_d -> '_b) -> ('_d -> '_c))))
(( curry compose ) ( curry apply )) ; (('_a -> ('_b -> '_c)) -> ('_a -> ('_b -> '_c)))
(( curry apply ) ( curry compose )) ; (('_a -> '_b) -> (('_c -> '_a) -> ('_c -> '_b)))
( compose curry flip ) ; (('_a '_b -> '_c) -> ('_b -> ('_a -> '_c)))