#[derive(Debug)]
pub enum Op {
    Add,
    Sub,
    Mul,
    Div,
    Eq
}

#[derive(Debug)]
pub enum Num {
    Value(f64),
    Variable(String),
    Op(Op, Box<Num>, Box<Num>)
}

#[derive(Debug)]
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
    Call(String, Vec<String>),
    None
}