#[derive(Debug, PartialEq, Clone)]
pub enum Op {
    Add,
    Sub,
    Mul,
    Div,
    Eq,
    Gt,
    Lt,
    And,
    Or
}

#[derive(Debug, PartialEq, Clone)]
pub enum Num {
    Value(f64),
    Variable(String),
    Op(Op, Box<Num>, Box<Num>)
}

#[derive(Debug, PartialEq, Clone)]
pub enum Ins {
    Forward(Num),
    Backward(Num),
    Left(Num),
    Right(Num),
    PenUp,
    PenDown,
    Text(Num, String),
    Repeat(Num, Vec<Ins>),
    If(Num, Vec<Ins>),
    Let(String, Num),
    Define(String, Vec<String>, Vec<Ins>),
    Call(String, Vec<Num>)
}

impl Op {
    pub fn new(op: char) -> Op {
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
            bad_op => panic!("Wrong syntax: {bad_op}!")
        }
    }
}