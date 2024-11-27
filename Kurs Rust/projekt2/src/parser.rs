use crate::syntax::Ins;
use crate::keywords::Kw;
use crate::num_parser::parse_num;

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

fn _parse_to(args: &str, block: Vec<Kw>) -> Ins {
    let parts: Vec<&str> = args.split_whitespace().collect();

    Ins::Define(
        parts[0].to_string(),
        parts[1..].iter().map(|&s| s.replace(":", "")).collect(),
        _parse(block)
    )
}

fn _parse_call(name: &str, args: &str) -> Ins {
    Ins::Call(name.to_string(), args.split_whitespace().map(|s| s.replace(":", "")).collect())
}
