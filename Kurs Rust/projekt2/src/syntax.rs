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
    Repeat(Num, Vec<Ins>),
    If(Num, Vec<Ins>),
    Define(String, Vec<String>, Vec<Ins>),
    Call(String, Vec<Num>)
}
