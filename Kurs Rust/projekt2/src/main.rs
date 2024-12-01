mod parser;
mod syntax;
mod keywords;
mod num_parser;
mod turtle;
mod utils;

use crate::parser::parse;
use std::io;
use utils::{read_and_trim_lines, save_string};
use turtle::Turtle;

fn main() -> io::Result<()> {
    const INPUT_PATH: &str  = "examples\\dragon.txt";
    const OUTPUT_PATH: &str  = "output.svg";

    let lines = read_and_trim_lines(INPUT_PATH)?;
    let instructions = parse(lines);
    // println!("{:#?}", instructions);

    let mut turtle = Turtle::new();
    turtle.run(&instructions);

    save_string(&turtle.get_svg(), OUTPUT_PATH)?;
    Ok(())
}
