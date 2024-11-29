use crate::syntax::{Num, Op};

pub fn parse(input: &str) -> Num {
    _parse(&_remove_whitespace(input))
}

fn _parse(input: &str) -> Num {
    _parse_and_or(input)
}

fn _parse_and_or(input: &str) -> Num {
    if let Some(res) = _parse_bin_op(input, '&') { res }
    else if let Some(res) = _parse_bin_op(input, '|') { res }
    else {_parse_logic(input)}
}

fn _parse_logic(input: &str) -> Num {
    if let Some(res) = _parse_bin_op(input, '=') { res }
    else if let Some(res) = _parse_bin_op(input, '>') { res }
    else if let Some(res) = _parse_bin_op(input, '<') { res }
    else {_parse_add_sub(input)}
}

fn _parse_add_sub(input: &str) -> Num {
    if let Some(res) = _parse_bin_op(input, '+') { res }
    else if let Some(res) = _parse_bin_op(input, '-') { res }
    else {_parse_mul_div(input)}
}

fn _parse_mul_div(input: &str) -> Num {
    if let Some(res) = _parse_bin_op(input, '*') { res }
    else if let Some(res) = _parse_bin_op(input, '/') { res }
    else {_parse_val_var(input)}
}

fn _parse_val_var(input: &str) -> Num {
    if let Ok(number) = input.parse::<f64>() {
        Num::Value(number)
    }
    else {
        Num::Variable(input.to_string())
    }
}

fn _parse_bin_op(input: &str, op: char) -> Option<Num> {
    if let Some((left, right)) = _split_by_first_char(input, op) {
        Some(Num::Op(_char_into_op(op), Box::new(_parse(&left)), Box::new(_parse(&right))))
    } 
    else {
        None
    }
}

fn _char_into_op(op: char) -> Op {
    match op {
        '+' => Op::Add,
        '-' => Op::Sub,
        '*' => Op::Mul,
        '/' => Op::Div,
        '&' => Op::And,
        '|' => Op::Or,
        '=' => Op::Eq,
        '>' => Op::Gt,
        '<' => Op::Lt,
        bad_op => panic!("Wrong operator: {bad_op}!")
    }
}

fn _split_by_first_char(input: &str, sep: char) -> Option<(String, String)> {
    if let Some(index) = input.find(sep) {
        let (left, right) = input.split_at(index);
        Some((left.to_string(), right[1..].to_string()))
    } else {
        None
    }
}

fn _remove_whitespace(input: &str) -> String {
    input.chars().filter(|c| !c.is_whitespace()).collect()
}

#[cfg(test)]
mod tests {
    use super::parse;
    use crate::syntax::{Num, Op};

    #[test]
    fn test_num() {
        assert_eq!(parse("123"), Num::Value(123.0));
        assert_eq!(parse("123.2"), Num::Value(123.2));
    }

    #[test]
    fn test_var() {
        assert_eq!(parse(":a"), Num::Variable(":a".to_string()));
    }

    #[test]
    fn test_op() {
        assert_eq!(parse(":a + :b"), Num::Op(Op::Add, Box::new(Num::Variable(":a".to_string())), Box::new(Num::Variable(":b".to_string()))));
        assert_eq!(parse(":a - :b"), Num::Op(Op::Sub, Box::new(Num::Variable(":a".to_string())), Box::new(Num::Variable(":b".to_string()))));
        assert_eq!(parse(":a * :b"), Num::Op(Op::Mul, Box::new(Num::Variable(":a".to_string())), Box::new(Num::Variable(":b".to_string()))));
        assert_eq!(parse(":a / :b"), Num::Op(Op::Div, Box::new(Num::Variable(":a".to_string())), Box::new(Num::Variable(":b".to_string()))));
        assert_eq!(parse(":a & :b"), Num::Op(Op::And, Box::new(Num::Variable(":a".to_string())), Box::new(Num::Variable(":b".to_string()))));
        assert_eq!(parse(":a | :b"), Num::Op(Op::Or, Box::new(Num::Variable(":a".to_string())), Box::new(Num::Variable(":b".to_string()))));
        assert_eq!(parse(":a = :b"), Num::Op(Op::Eq, Box::new(Num::Variable(":a".to_string())), Box::new(Num::Variable(":b".to_string()))));
        assert_eq!(parse(":a > :b"), Num::Op(Op::Gt, Box::new(Num::Variable(":a".to_string())), Box::new(Num::Variable(":b".to_string()))));
        assert_eq!(parse(":a < :b"), Num::Op(Op::Lt, Box::new(Num::Variable(":a".to_string())), Box::new(Num::Variable(":b".to_string()))));
    }

    #[test]
    fn test_order() {
        assert_eq!(
            parse(":a + :b * :c"),
            Num::Op(
                Op::Add,
                Box::new(Num::Variable(":a".to_string())),
                Box::new(Num::Op(
                    Op::Mul,
                    Box::new(Num::Variable(":b".to_string())),
                    Box::new(Num::Variable(":c".to_string()))
                ))
            )
        );
        assert_eq!(
            parse(":a * :b + :c"),
            Num::Op(
                Op::Add,
                Box::new(Num::Op(
                    Op::Mul,
                    Box::new(Num::Variable(":a".to_string())),
                    Box::new(Num::Variable(":b".to_string()))
                )),
                Box::new(Num::Variable(":c".to_string()))
            )
        );
    }
}