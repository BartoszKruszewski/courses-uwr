mod parser;
mod turtle;

use crate::parser::Instruction;
use crate::turtle::Turtle;
use svg::Document;
use std::io::{self, Read};
use std::fs::File;

fn main() -> io::Result<()> {
    const INPUT_PATH: &str  = "instructions.txt";
    const OUTPUT_PATH: &str  = "output.svg";
    const VIEW_BOX: (isize, isize, isize, isize)  = (-500, -500, 1000, 1000);

    let lines = read(INPUT_PATH)?;
    let instructions = Instruction::parse(&lines);

    let mut turtle = Turtle::new();
    turtle.exec(&instructions);
    
    let document = Document::new().set("viewBox", VIEW_BOX).add(turtle.get_doc_group());
    svg::save(OUTPUT_PATH, &document)?;
    Ok(())
}

fn read(file_path: &str) -> io::Result<Vec<String>> {
    let mut file = File::open(file_path)?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;
    Ok(contents
        .replace("[", " [ ")
        .replace("]", " ] ")
        .split_whitespace()
        .map(String::from)
        .collect())
}
