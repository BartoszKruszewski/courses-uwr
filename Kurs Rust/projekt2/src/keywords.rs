use std::str::FromStr;

#[derive(PartialEq, Clone, Debug)]
pub enum Kw {
    Forward(String),
    Backward(String),
    Left(String),
    Right(String),
    PenUp,
    PenDown,
    Repeat(String),
    If(String),
    To(String),
    Call(String, String),
    BlockStart,
    BlockEnd,
}

impl Kw {
    pub fn new(input: &str) -> Self {
        let name = input.split_whitespace().next().unwrap();
        let args = String::from_str(if let Some(pos) = input.find(' ') { &input[pos + 1..] } else {""}).unwrap();
        match name {
            "forward" => Kw::Forward(args),
            "backward" => Kw::Backward(args),
            "left" => Kw::Left(args),
            "right" => Kw::Right(args),
            "penup" => Kw::PenUp,
            "pendown" => Kw::PenDown,
            "repeat" => Kw::Repeat(args),
            "if" => Kw::If(args),
            "def" => Kw::To(args),
            "{" => Kw::BlockStart,
            "}" => Kw::BlockEnd,
            name => Kw::Call(name.to_string(), args)
        }
    }
}