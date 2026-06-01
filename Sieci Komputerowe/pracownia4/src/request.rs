// Bartosz Kruszewski 337568

use std::io::{BufRead, BufReader};
use std::net::TcpStream;
use std::path::Path;

use crate::response::resolve_response;

pub fn handle_connection(stream: &mut TcpStream, root: &Path) -> std::io::Result<()> {
    let mut reader = BufReader::new(stream.try_clone()?);
    let mut line = String::new();

    if reader.read_line(&mut line)? == 0 {
        return Ok(());
    }

    let parts: Vec<&str> = line.trim().split_whitespace().collect();
    if parts.len() < 3 {
        return resolve_response(stream, "???", "", "localhost", root, false);
    }

    let method = parts[0];
    let url_path = parts[1];

    let (host, connection_close) = parse_headers(&mut reader)?;
    println!("{method} {url_path} (Host: {host})");

    resolve_response(stream, method, url_path, &host, root, connection_close)
}

fn parse_headers(reader: &mut BufReader<TcpStream>) -> std::io::Result<(String, bool)> {
    let mut host = "localhost".to_string();
    let mut close = false;

    loop {
        let mut line = String::new();
        if reader.read_line(&mut line)? == 0 {
            break;
        }

        let line = line.trim();
        if line.is_empty() {
            break;
        }

        if let Some(h) = line.strip_prefix("Host:") {
            host = h
                .trim()
                .split(':')
                .next()
                .unwrap_or("localhost")
                .to_string();
        } else if line.eq_ignore_ascii_case("Connection: close") {
            close = true;
        }
    }

    Ok((host, close))
}
