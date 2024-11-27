mod parser;
mod syntax;
mod keywords;
mod preprocessor;
mod num_parser;

use crate::parser::parse;
use std::io;
use preprocessor::read_and_trim_lines;

fn main() -> io::Result<()> {
    const INPUT_PATH: &str  = "instructions.txt";
    //const OUTPUT_PATH: &str  = "output.svg";
    //const VIEW_BOX: (isize, isize, isize, isize)  = (-500, -500, 1000, 1000);

    let lines = read_and_trim_lines(INPUT_PATH)?;
    println!("{:#?}", lines); 
    let instructions = parse(lines);
    println!("{:#?}", instructions); 
    Ok(())

    // let mut turtle = Turtle::new();
    // turtle.exec(&instructions);
    
    // let document = Document::new().set("viewBox", VIEW_BOX).add(turtle.get_doc_group());
    // svg::save(OUTPUT_PATH, &document)?;
    // Ok(())
}
