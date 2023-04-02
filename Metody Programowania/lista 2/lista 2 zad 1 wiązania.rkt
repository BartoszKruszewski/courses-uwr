#lang racket

( let ([ x 3])
   (+ x y)) ;y nie zwiazny

( let ([ x 1]
       [ y (+ x 2) ]) ;x nie zwiazany
   (+ x y))

( let ([ x 1])
   ( let ([ y (+ x 2) ])
      (* x y)))

( define ( f x y)
   (* x y z )) ;z nie zwiazany

( define ( f x)
   ( define (g y z)
      (* x y z))
   ( f x x x)) ;f przyjmuje jeden argument a przekazywane są trzy
