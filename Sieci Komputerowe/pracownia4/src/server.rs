// Bartosz Kruszewski 337568

use std::io;
use std::net::TcpListener;
use std::path::PathBuf;

use crate::request::handle_connection;

pub fn start_server(port: u16, root: PathBuf) -> io::Result<()> {
    let listener = TcpListener::bind(("0.0.0.0", port))?;
    println!(
        "Server running on port {} with root {}\n",
        port,
        root.display()
    );

    for stream in listener.incoming() {
        if let Ok(mut stream) = stream {
            if let Err(e) = handle_connection(&mut stream, &root) {
                eprintln!("Connection error: {}", e);
            }
        }
    }
    Ok(())
}
