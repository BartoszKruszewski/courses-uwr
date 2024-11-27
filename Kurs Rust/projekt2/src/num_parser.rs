use crate::syntax::{Num, Op};
use std::str::Chars;
use std::iter::Peekable;

#[derive(Debug)]
pub struct NumParser<'a> {
    input: Peekable<Chars<'a>>,
}

pub fn parse_num(input: &str) -> Num {
    NumParser::new(input).parse_add_sub().unwrap()
}

impl<'a> NumParser<'a> {
    pub fn new(input: &'a str) -> Self {
        NumParser {
            input: input.chars().peekable(),
        }
    }

    fn parse_add_sub(&mut self) -> Result<Num, String> {
        let mut left = self.parse_mul_div()?;

        while let Some(&op) = self.input.peek() {
            match op {
                '+' | '-' => {
                    self.input.next();
                    let right = self.parse_mul_div()?;
                    left = Num::Op(
                        if op == '+' { Op::Add } else { Op::Sub },
                        Box::new(left),
                        Box::new(right),
                    );
                }
                _ => break,
            }
        }

        Ok(left)
    }

    fn parse_mul_div(&mut self) -> Result<Num, String> {
        let mut left = self.parse_term()?;

        while let Some(&op) = self.input.peek() {
            match op {
                '*' | '/' => {
                    self.input.next();
                    let right = self.parse_term()?;
                    left = Num::Op(
                        if op == '*' { Op::Mul } else { Op::Div },
                        Box::new(left),
                        Box::new(right),
                    );
                }
                _ => break,
            }
        }

        Ok(left)
    }

    fn parse_term(&mut self) -> Result<Num, String> {
        self.skip_whitespace();
    
        if let Some(&ch) = self.input.peek() {
            if ch.is_digit(10) || ch == '.' {
                // Jeśli zaczyna się od cyfry lub kropki, to liczba
                return self.parse_number();
            } else if ch == ':' {
                // Jeśli zaczyna się od ':', to zmienna
                return self.parse_variable();
            } else if ch == '(' {
                // Jeśli nawias otwierający, parsuj jako wyrażenie w nawiasach
                self.input.next(); // Pomija '('
                let expr = self.parse_add_sub()?;
                self.expect(')')?; // Upewnia się, że jest zamykający nawias
                return Ok(expr);
            }
        }
    
        Err("Unexpected character while parsing term".to_string())
    }

    fn parse_number(&mut self) -> Result<Num, String> {
        let mut num_str = String::new();

        while let Some(&ch) = self.input.peek() {
            if ch.is_digit(10) || ch == '.' {
                num_str.push(ch);
                self.input.next();
            } else {
                break;
            }
        }

        num_str
            .parse::<f64>()
            .map(Num::Value)
            .map_err(|_| "Invalid number".to_string())
    }

    fn parse_variable(&mut self) -> Result<Num, String> {
        let mut var_name = String::new();
    
        // Upewnij się, że zmienna zaczyna się od ':'
        if let Some(&ch) = self.input.peek() {
            if ch == ':' {
                var_name.push(ch);
                self.input.next();
            } else {
                return Err("Expected ':' at the beginning of a variable name".to_string());
            }
        }
    
        // Dodaj pozostałe znaki nazwy zmiennej (alfanumeryczne i '_')
        while let Some(&ch) = self.input.peek() {
            if ch.is_alphanumeric() || ch == '_' {
                var_name.push(ch);
                self.input.next();
            } else {
                break; // Koniec nazwy zmiennej
            }
        }
    
        if var_name.len() > 1 {
            Ok(Num::Variable(var_name))
        } else {
            Err("Variable name cannot be empty after ':'".to_string())
        }
    }

    fn expect(&mut self, expected: char) -> Result<(), String> {
        self.skip_whitespace();

        match self.input.next() {
            Some(ch) if ch == expected => Ok(()),
            _ => Err(format!("Expected '{}'", expected)),
        }
    }

    fn skip_whitespace(&mut self) {
        while let Some(&ch) = self.input.peek() {
            if ch.is_whitespace() {
                self.input.next();
            } else {
                break;
            }
        }
    }
}
