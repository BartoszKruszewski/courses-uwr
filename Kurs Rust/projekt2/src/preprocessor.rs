use std::fs::File;
use std::io::{self, BufRead};

pub fn read_and_trim_lines(file_path: &str) -> io::Result<Vec<String>> {
    let file = File::open(file_path)?;
    let reader = io::BufReader::new(file);
    let lines = reader
        .lines()
        .filter_map(Result::ok) // Ignoruj błędne linie
        .map(|line| line.trim().to_string())
        .filter(|line| !line.is_empty()) // Pomijaj puste linie
        .collect();
    Ok(lines)
}