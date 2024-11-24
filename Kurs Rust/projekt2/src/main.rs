mod instruction;
mod turtle;

use crate::instruction::Instruction;
use crate::turtle::Turtle;
use svg::Document;
use std::io::{self, BufRead};
use std::fs::File;

fn main() -> io::Result<()> {
    const INPUT_PATH: &str  = "instructions.txt";
    const OUTPUT_PATH: &str  = "output.svg";
    const VIEW_BOX: (isize, isize, isize, isize)  = (-500, -500, 1000, 1000);

    let lines = read_lines(INPUT_PATH)?;
    let instructions = Instruction::parse(&lines);

    let mut turtle = Turtle::new();
    turtle.exec(&instructions);
    
    let document = Document::new().set("viewBox", VIEW_BOX).add(turtle.get_doc_group());
    svg::save(OUTPUT_PATH, &document)?;
    Ok(())
}

fn read_lines(path: &str) -> io::Result<Vec<String>> {
    let file = File::open(path)?;
    let lines: Vec<String> = io::BufReader::new(file)
        .lines()
        .collect::<Result<_, _>>()?;
    Ok(lines)
}
