#lang racket
; <expr> ::= "`"<atom> | <special>
; <atom> ::= <boolean> | <number> | <character> | <string> | <symbol>
; <boolean> ::= "#t" | "#f"
; <number> ::= <digit>+ | <digit>+.<digit>+
; <string> ::= /"<character>*/"
; <character> ::= dowolny znka ASCII 
; <symbol> ::= "'"<atom>
; <special> ::= "'(" (<expr>" ")* <expr>")" | "`(" (<expr>" ")* <expr>")" |
;            (<expr>" ")+  ". " <expr> | "'" <expr> | "`" <expr> | ", "<expr> 
; <digit> ::= "0" | "1" | "2" | ...
