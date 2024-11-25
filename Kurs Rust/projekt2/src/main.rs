use std::collections::HashMap;

// Definicja AST
#[derive(Debug, Clone)]
enum LogoCommand {
    Forward(i32),
    Left(i32),
    Right(i32),
    Repeat(i32, Vec<LogoCommand>),
    If(Box<LogoCondition>, Vec<LogoCommand>),
    Function(String, Vec<LogoCommand>), // Definicja funkcji
    Call(String),                       // Wywołanie funkcji
    Polygon(i32, i32),                  // Wielokąt o określonej liczbie boków i rozmiarze
}

#[derive(Debug, Clone)]
enum LogoCondition {
    Greater(String, i32),  // Zmienna > liczba
    LessOrEqual(String, i32), // Zmienna <= liczba
}

// Kontekst wykonania programu
#[derive(Debug, Default)]
struct ExecutionContext {
    variables: HashMap<String, i32>,
    functions: HashMap<String, Vec<LogoCommand>>,
}

impl ExecutionContext {
    fn new() -> Self {
        Self {
            variables: HashMap::new(),
            functions: HashMap::new(),
        }
    }

    fn execute(&mut self, commands: &[LogoCommand]) {
        for command in commands {
            match command {
                LogoCommand::Forward(steps) => {
                    println!("Moving forward {} steps.", steps);
                }
                LogoCommand::Left(angle) => {
                    println!("Turning left {} degrees.", angle);
                }
                LogoCommand::Right(angle) => {
                    println!("Turning right {} degrees.", angle);
                }
                LogoCommand::Repeat(count, body) => {
                    for _ in 0..*count {
                        self.execute(body);
                    }
                }
                LogoCommand::If(condition, body) => {
                    if self.evaluate_condition(condition) {
                        self.execute(body);
                    }
                }
                LogoCommand::Function(name, body) => {
                    self.functions.insert(name.clone(), body.clone());
                }
                LogoCommand::Call(name) => {
                    if let Some(body) = self.functions.get(name) {
                        self.execute(&body.clone());
                    } else {
                        panic!("Undefined function: {}", name);
                    }
                }
                LogoCommand::Polygon(sides, size) => {
                    for _ in 0..*sides {
                        println!("Drawing side of length {}.", size);
                        println!("Turning right {} degrees.", 360 / sides);
                    }
                }
            }
        }
    }

    fn evaluate_condition(&self, condition: &LogoCondition) -> bool {
        match condition {
            LogoCondition::Greater(var, value) => self.variables.get(var).unwrap_or(&0) > value,
            LogoCondition::LessOrEqual(var, value) => {
                self.variables.get(var).unwrap_or(&0) <= value
            }
        }
    }
}

// Lexer - dzielenie na tokeny
fn tokenize(input: &str) -> Vec<String> {
    input
        .replace("[", " [ ")
        .replace("]", " ] ")
        .split_whitespace()
        .map(|s| s.trim().to_string())
        .collect()
}

// Parser dla programu z `repeat` i `if`
fn parse_program(tokens: &[String]) -> Vec<LogoCommand> {
    let mut commands = vec![];
    let mut i = 0;

    while i < tokens.len() {
        match tokens[i].as_str() {
            "to" => {
                let func_name = tokens[i + 1].clone();
                let (body, consumed) = parse_function(&tokens[i + 2..]);
                commands.push(LogoCommand::Function(func_name, body));
                i += 2 + consumed;
            }
            _ => {
                let (command, consumed) = parse_command(&tokens[i..]);
                commands.push(command);
                i += consumed;
            }
        }
    }

    commands
}

// Parser komendy
fn parse_command(tokens: &[String]) -> (LogoCommand, usize) {
    match tokens[0].as_str() {
        "forward" => {
            let steps = tokens[1].parse().unwrap();
            (LogoCommand::Forward(steps), 2)
        }
        "right" => {
            let angle = tokens[1].parse().unwrap();
            (LogoCommand::Right(angle), 2)
        }
        "repeat" => {
            let count = tokens[1].parse().unwrap();
            let (body, consumed) = parse_block(&tokens[2..]);
            (LogoCommand::Repeat(count, body), 2 + consumed)
        }
        "if" => {
            let condition = match tokens[1].as_str() {
                "x>" => LogoCondition::Greater(tokens[2].clone(), tokens[3].parse().unwrap()),
                "x<=" => LogoCondition::LessOrEqual(tokens[2].clone(), tokens[3].parse().unwrap()),
                _ => panic!("Invalid condition syntax: {}", tokens[1]),
            };
            let (body, consumed) = parse_block(&tokens[4..]);
            (LogoCommand::If(Box::new(condition), body), 4 + consumed)
        }
        _ => panic!("Unexpected token: {}", tokens[0]),
    }
}

// Parsowanie bloku `[ instrukcje ]`
fn parse_block(tokens: &[String]) -> (Vec<LogoCommand>, usize) {
    if tokens[0] != "[" {
        panic!("Expected '[', found: {}", tokens[0]);
    }

    let mut commands = vec![];
    let mut i = 1;

    while tokens[i] != "]" {
        let (command, consumed) = parse_command(&tokens[i..]);
        commands.push(command);
        i += consumed;
    }

    (commands, i + 1) // +1 bo zamykające `]`
}

// Parsowanie funkcji
fn parse_function(tokens: &[String]) -> (Vec<LogoCommand>, usize) {
    let mut commands = vec![];
    let mut i = 0;

    while tokens[i] != "end" {
        let (command, consumed) = parse_command(&tokens[i..]);
        commands.push(command);
        i += consumed;
    }

    (commands, i + 1) // +1 dla `end`
}

// Główna funkcja
fn main() {
    let input = "
    to square
        repeat 4 [ forward 100 right 90 ]
    end

    to pattern
        repeat 36 [ square right 10 ]
    end

    if x> 10 [ square ]
    ";

    let tokens = tokenize(input);
    let program = parse_program(&tokens);

    let mut context = ExecutionContext::new();
    context.variables.insert("x".to_string(), 15);
    context.execute(&program);
}