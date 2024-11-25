pub enum Instruction {
    Forward(f64),
    Backward(f64),
    Left(f64),
    Right(f64),
    PenUp,
    PenDown,
    Repeat(usize, Vec<Instruction>)
}

enum Code {
    Single(String),
    Nested(Vec<Code>)
}

impl Instruction {
    pub fn parse(commands: &Vec<String>) -> Vec<Self> {
        let code = Self::parse_into_code(commands);
    }

    fn parse_into_code(commands: &Vec<String>) -> (Code, usize) {
        let mut parsed_commands: Vec<Code> = Vec::new();
        let n = commands.len();
        let mut i: usize = 0;
        while i < n {
            let command = &commands[i];
            parsed_commands.push(
                match command.as_str() {
                    "[" => {
                        let (code, end) = Self::parse_into_code(&commands[i..].to_vec());
                        i = end;
                        code
                    }
                    "]" => {
                        return (Code::Nested(parsed_commands), i);
                    }
                    _ => Code::Single(command.clone())
                }
            );
        }
        (Code::Nested(parsed_commands), n)
    }

    fn split_inline(line: &str) -> Vec<Instruction> {
        line
            .split_whitespace()
            .collect::<Vec<&str>>()
            .windows(2)
            .map(|p| Self::new(p[0], p[1]))
            .collect()
    }

    fn string_to_instruction(ins_str: &String, args: Vec<&String>) -> Self {
        match ins_str.to_lowercase().as_str() {
            "forward" | "fd" => Instruction::Forward(args[0].parse::<f64>().unwrap()),
            "backward" | "bk" => Instruction::Backward(args[0].parse::<f64>().unwrap()),
            "left" | "lt" => Instruction::Left(args[0].parse::<f64>().unwrap()),
            "right" | "rt" => Instruction::Right(args[0].parse::<f64>().unwrap()),
            "penup" | "pu" => Instruction::PenUp,
            "pendown" | "pd" => Instruction::PenDown,
            name => panic!("Wrong Instruction: {name}"),
        }
    }
}
