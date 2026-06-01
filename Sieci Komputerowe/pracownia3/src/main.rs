// Bartosz Kruszewski 337568

mod downloader;

use downloader::Downloader;
use std::env;
use std::io;
use std::str::FromStr;

fn main() -> io::Result<()> {
    let (server_ip, server_port, output_file, total_size) = parse_input();
    let mut downloader = Downloader::new(server_ip, server_port, output_file, total_size)?;
    downloader.run()
}

fn parse_input() -> (String, u16, String, usize) {
    let args: Vec<String> = env::args().collect();
    if args.len() != 5 {
        eprintln!("Usage: {} <ip> <port> <output_file> <size>", args[0]);
        std::process::exit(1);
    }

    let server_ip = String::from_str(&args[1]).unwrap();
    let server_port: u16 = args[2].parse().expect("Invalid port number");
    let output_file = String::from_str(&args[3]).unwrap();
    let total_size: usize = args[4].parse().expect("Invalid file size");
    (server_ip, server_port, output_file, total_size)
}
