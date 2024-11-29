use crate::syntax::Ins;
use crate::keywords::Kw;
use crate::num_parser::parse as parse_num;

pub fn parse(input: Vec<String>) -> Vec<Ins> {
    _parse(input.iter().map(|x| Kw::new(x.as_str())).collect())
}

fn _parse(input: Vec<Kw>) -> Vec<Ins> {
    let mut res: Vec<Ins> = Vec::new();
    let mut i: usize = 0;
    while i < input.len() {
        let kw = &input[i];
        let mut next_block = Vec::new();
        match kw {
            Kw::Repeat(_) | Kw::If(_) | Kw::To(_) => {
                next_block = _find_first_block(input[i..].to_vec());
                i += next_block.len() + 3;
            }
            _ => { i += 1; }
        }

        res.push(match kw {
            Kw::Forward(args) => Ins::Forward(parse_num(args)),
            Kw::Backward(args) => Ins::Backward(parse_num(args)),
            Kw::Left(args) => Ins::Left(parse_num(args)),
            Kw::Right(args) => Ins::Right(parse_num(args)),
            Kw::PenUp => Ins::PenUp,
            Kw::PenDown => Ins::PenDown,
            Kw::Call(name, args) => _parse_call(name, args),
            Kw::Repeat(args) => Ins::Repeat(parse_num(args), _parse(next_block)),
            Kw::If(args) => Ins::If(parse_num(args), _parse(next_block)),
            Kw::To(args) => {_parse_to(args, next_block)}
            Kw::BlockStart => panic!("Block start out of context!"),
            Kw::BlockEnd => panic!("Block end out of context!"),
        });
    }
    res
}

fn _parse_to(args: &str, block: Vec<Kw>) -> Ins {
    let parts: Vec<&str> = args.split_whitespace().collect();

    Ins::Define(
        parts[0].to_string(),
        parts[1..].iter().map(|&s| s.replace(":", "")).collect(),
        _parse(block)
    )
}

fn _parse_call(name: &str, args: &str) -> Ins {
    Ins::Call(
        name.to_string(),
        args.split(",").map(|s| parse_num(s)).collect()
    )
}

fn _find_first_block(block: Vec<Kw>) -> Vec<Kw> {
    let start = block.iter().position(|x| *x == Kw::BlockStart).unwrap();
    let mut i = start + 1;
    let mut deep = 1;
    while deep > 0 && i < block.len() {
        match block[i] {
            Kw::BlockStart => { deep += 1},
            Kw::BlockEnd => { deep -= 1},
            _ => {}
        };
        i += 1;
    }
    block[start + 1..i - 1].to_vec()
}

#[cfg(test)]
mod tests {
    use super::parse;
    use crate::syntax::{Ins, Num, Op};

    #[test]
    fn test_simple() {
        let input: Vec<String> = vec![
            "to square :x",
            "[",
            "repeat 4",
            "[",
            "repeat 10",
            "[",
            "forward :x",
            "]",
            "right 90",
            "]",
            "]",
            "to foo",
            "[",
            "repeat 10",
            "[",
            "forward 20",
            "left 3",
            "]",
            "]",
        ].iter().map(|&s| s.to_string()).collect();
        let output: Vec<Ins> = vec![
            Ins::Define("square".to_string(), vec!["x".to_string()], vec![
                Ins::Repeat(Num::Value(4.0), vec![
                    Ins::Repeat(Num::Value(10.0), vec![
                        Ins::Forward(Num::Variable(":x".to_string())),
                    ]),
                    Ins::Right(Num::Value(90.0)),
                ]),
            ]),
            Ins::Define("foo".to_string(), vec![], vec![
                Ins::Repeat(Num::Value(10.0), vec![
                    Ins::Forward(Num::Value(20.0)),
                    Ins::Left(Num::Value(3.0)),
                ]),
            ])
        ];
        assert_eq!(parse(input), output);
    }

    #[test]
    fn test_all_enums() {
        let input: Vec<String> = vec![
            "to complex_example :a :b",
            "[",
            "if :a + :b",
            "[",
            "repeat 3",
            "[",
            "forward :a * :b",
            "right :b / 2",
            "penup",
            "left :a - :b",
            "pendown",
            "]",
            "]",
            "repeat 2",
            "[",
            "sub_function :a :b",
            "]",
            "]"
        ].iter().map(|&s| s.to_string()).collect();
    
        let output: Vec<Ins> = vec![
            Ins::Define("complex_example".to_string(), vec!["a".to_string(), "b".to_string()], vec![
                Ins::If(Num::Op(Op::Add, Box::new(Num::Variable(":a".to_string())), Box::new(Num::Variable(":b".to_string()))), vec![
                    Ins::Repeat(Num::Value(3.0), vec![
                        Ins::Forward(Num::Op(Op::Mul, Box::new(Num::Variable(":a".to_string())), Box::new(Num::Variable(":b".to_string())))),
                        Ins::Right(Num::Op(Op::Div, Box::new(Num::Variable(":b".to_string())), Box::new(Num::Value(2.0)))),
                        Ins::PenUp,
                        Ins::Left(Num::Op(Op::Sub, Box::new(Num::Variable(":a".to_string())), Box::new(Num::Variable(":b".to_string())))),
                        Ins::PenDown,
                    ])
                ]),
                Ins::Repeat(Num::Value(2.0), vec![
                    Ins::Call("sub_function".to_string(), vec![Num::Variable("a".to_string()), Num::Variable("b".to_string())]),
                ]),
            ])
        ];
    
        assert_eq!(parse(input), output);
    }
}
