// Bartosz Kruszewski 337568

mod request;
mod response;
mod server;
mod utils;

use std::env;
use std::path::PathBuf;

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() != 3 {
        eprintln!("Usage: {} <port> <web_root>", args[0]);
        return;
    }

    let port: u16 = args[1].parse().unwrap_or_else(|_| {
        eprintln!("Invalid port number.");
        std::process::exit(1);
    });

    let root = PathBuf::from(&args[2]);
    if !root.is_dir() {
        eprintln!("Provided directory does not exist.");
        return;
    }

    if let Err(e) = server::start_server(port, root) {
        eprintln!("Server error: {}", e);
    }
}
