mod parser;
mod syntax;
mod keywords;
mod preprocessor;
mod num_parser;
mod turtle;

use crate::parser::parse;
use std::io;
use preprocessor::read_and_trim_lines;
use turtle::Turtle;
use svg::Document;

fn main() -> io::Result<()> {
    const INPUT_PATH: &str  = "example_snowflake.txt";
    const OUTPUT_PATH: &str  = "output.svg";

    let lines = read_and_trim_lines(INPUT_PATH)?;
    let instructions = parse(lines);
    println!("{:#?}", instructions);

    let mut turtle = Turtle::new();
    turtle.run(&instructions);
    let (min_x, min_y, max_x, max_y) = turtle.get_bounds();
    let view_box = (min_x, min_y, max_x - min_x, max_y - min_y);
    
    let document = Document::new().set("viewBox", view_box).add(turtle.get_doc_group());
    svg::save(OUTPUT_PATH, &document)?;
    Ok(())
}
