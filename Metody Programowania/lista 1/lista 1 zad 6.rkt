#lang racket

(define (new-if ifCond ifTrue ifFalse) (or (and ifCond ifTrue) ifFalse))