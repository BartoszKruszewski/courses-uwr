#lang racket
; <expr> ::= <term> | <expr> "+" <term> | <expr> "-" <term>
; <term> ::= <factor> | <term> "*" <factor> | <term> "/" <factor>
; <factor> ::= <power> | <factor> "!" | "-" <factor>
; <power> ::= <unary> | <power> "^" <unary>
; <unary> ::= <number> | "-" <unary> | "(" <expr> ")" | <unary> "!"

; ; <number> ::= <digit>+ | <digit>+.<digit>+
; <digit> ::= "0" | "1" | "2" | ...