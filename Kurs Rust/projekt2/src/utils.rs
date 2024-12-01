use std::fs::File;
use std::io::{self, BufRead, Write};

pub fn split_by_first_char(input: &str, sep: char) -> Option<(String, String)> {
    if let Some(index) = input.find(sep) {
        let (left, right) = input.split_at(index);
        Some((left.to_string(), right[1..].to_string()))
    } else {
        None
    }
}

pub fn to_bool(input: f64) -> bool {
    if input != 0.0 { true } else { false }
}

pub fn to_f64(input: bool) -> f64 {
    if input { 1.0 } else { 0.0 }
}

pub fn remove_whitespace(input: &str) -> String {
    input.chars().filter(|c| !c.is_whitespace()).collect()
}

pub fn read_and_trim_lines(file_path: &str) -> io::Result<Vec<String>> {
    let file = File::open(file_path)?;
    let reader = io::BufReader::new(file);
    let lines = reader
        .lines()
        .filter_map(Result::ok)
        .map(|line| line.trim().to_string())
        .filter(|line| !line.is_empty())
        .collect();
    Ok(lines)
}

pub fn save_string(content: &str, file_path: &str) -> io::Result<()> {
    let mut file = File::create(file_path)?;
    file.write_all(content.as_bytes())?;
    Ok(())
}
