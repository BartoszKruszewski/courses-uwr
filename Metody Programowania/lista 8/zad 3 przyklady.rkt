#lang racket

(require "zad-3-mqueue.rkt")

(define example-mqueue (make-mqueue))
(mqueue-push-front example-mqueue 5)
(mqueue-push-front example-mqueue 6)
(mqueue-push-front example-mqueue 7)
(mqueue-push-front example-mqueue 8)
(mqueue-push-back example-mqueue 5)
(mqueue-push-back example-mqueue 6)
(mqueue-push-back example-mqueue 7)
(mqueue-push-back example-mqueue 8)
(print-mqueue example-mqueue)
(mqueue-pop-back example-mqueue)
(mqueue-pop-back example-mqueue)
(mqueue-pop-front example-mqueue)
(print-mqueue example-mqueue)