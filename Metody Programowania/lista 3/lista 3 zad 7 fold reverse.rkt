#lang racket

( define ( foldr-reverse xs )
   ( foldr ( lambda (y ys ) ( append ys ( list y))) null xs ))

( define ( foldl-reverse xs )
   ( foldl( lambda (y ys) (cons y ys)) null xs ))

(foldl-reverse (build-list 10 identity))
( length ( foldl-reverse ( build-list 100000 identity )))