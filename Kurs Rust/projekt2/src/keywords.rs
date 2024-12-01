use std::str::FromStr;

#[derive(PartialEq, Clone, Debug)]
pub enum Kw {
    Forward(String),
    Backward(String),
    Left(String),
    Right(String),
    PenUp,
    PenDown,
    Text(String),
    Repeat(String),
    If(String),
    Let(String),
    Def(String),
    Call(String, String),
    BlockStart,
    BlockEnd,
}

impl Kw {
    pub fn new(input: &str) -> Self {
        let name = input.split_whitespace().next().unwrap();
        let args = String::from_str(if let Some(pos) = input.find(' ') { &input[pos + 1..] } else {""}).unwrap();
        match name {
            "forward" | "fd" => Kw::Forward(args),
            "backward" | "bk" => Kw::Backward(args),
            "left" | "lt" => Kw::Left(args),
            "right" | "rt" => Kw::Right(args),
            "penup" | "pu" => Kw::PenUp,
            "pendown" | "pd" => Kw::PenDown,
            "text" => Kw::Text(args),
            "repeat" => Kw::Repeat(args),
            "if" => Kw::If(args),
            "let" => Kw::Let(args),
            "def" => Kw::Def(args),
            "{" => Kw::BlockStart,
            "}" => Kw::BlockEnd,
            name => Kw::Call(name.to_string(), args)
        }
    }
}