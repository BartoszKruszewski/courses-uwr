use std::panic;

pub enum Instruction {
    Forward(f64),
    Backward(f64),
    Left(f64),
    Right(f64),
    PenUp,
    PenDown,
}

impl Instruction {
    pub fn new(instruction_str: &str) -> Self {
        let parts: Vec<&str> = instruction_str.split_whitespace().collect();
        let arg = parts.get(1).unwrap_or(&"0").parse::<f64>().unwrap();

        match parts[0].to_lowercase().as_str() {
            "forward" | "fd" => Instruction::Forward(arg),
            "backward" | "bk" => Instruction::Backward(arg),
            "left" | "lt" => Instruction::Left(arg),
            "right" | "rt" => Instruction::Right(arg),
            "penup" | "pu" => Instruction::PenUp,
            "pendown" | "pd" => Instruction::PenDown,
            name => panic!("Wrong Instruction: {name}"),
        }
    }

    pub fn parse(lines: &Vec<String>) -> Vec<Self> {
        lines.into_iter().filter_map(|s| { panic::catch_unwind(|| Self::new(s)).ok() }).collect()
    }
}
