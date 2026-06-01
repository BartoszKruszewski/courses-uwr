// Bartosz Kruszewski 337568

use std::collections::HashMap;
use std::fs::OpenOptions;
use std::io::{self, Write};
use std::net::{SocketAddr, ToSocketAddrs, UdpSocket};
use std::time::{Duration, Instant};

const MAX_PACKET_SIZE: usize = 1500;
const MAX_CHUNK_SIZE: usize = 1000;
const WINDOW_SIZE: usize = 1000;
const TIMEOUT_MS: u64 = 500;

struct ChunkRequest {
    start: usize,
    length: usize,
    last_request: Instant,
}

pub struct Downloader {
    server_addr: SocketAddr,
    socket: UdpSocket,
    file: std::fs::File,
    total_size: usize,
    pending_requests: HashMap<usize, ChunkRequest>,
    received_chunks: HashMap<usize, Vec<u8>>,
    current_request_position: usize,
    written_position: usize,
}

impl Downloader {
    pub fn new(
        server_ip: String,
        server_port: u16,
        output_file: String,
        total_size: usize,
    ) -> io::Result<Self> {
        let server_addr = format!("{}:{}", server_ip, server_port)
            .to_socket_addrs()?
            .next()
            .expect("Unable to resolve server address");

        let socket = UdpSocket::bind("0.0.0.0:0")?;
        socket.set_read_timeout(Some(Duration::from_millis(100)))?;

        let file = OpenOptions::new()
            .create(true)
            .write(true)
            .append(true)
            .open(output_file)?;

        Ok(Self {
            server_addr,
            socket,
            file,
            total_size,
            pending_requests: HashMap::new(),
            received_chunks: HashMap::new(),
            current_request_position: 0,
            written_position: 0,
        })
    }

    pub fn run(&mut self) -> io::Result<()> {
        while self.written_position < self.total_size {
            self.send_new_requests()?;
            self.receive_responses()?;
            self.retransmit_requests()?;
            self.write_ready_chunks()?;
        }
        Ok(())
    }

    fn send_new_requests(&mut self) -> io::Result<()> {
        while (self.pending_requests.len() + self.received_chunks.len()) < WINDOW_SIZE
            && self.current_request_position < self.total_size
        {
            let chunk_size = MAX_CHUNK_SIZE.min(self.total_size - self.current_request_position);
            self.send_request(self.current_request_position, chunk_size)?;
            self.pending_requests.insert(
                self.current_request_position,
                ChunkRequest {
                    start: self.current_request_position,
                    length: chunk_size,
                    last_request: Instant::now(),
                },
            );
            self.current_request_position += chunk_size;
        }
        Ok(())
    }

    fn send_request(&self, start: usize, length: usize) -> io::Result<()> {
        let request = format!("GET {} {}\n", start, length);
        self.socket.send_to(request.as_bytes(), self.server_addr)?;
        Ok(())
    }

    fn receive_responses(&mut self) -> io::Result<()> {
        let mut buf = [0u8; MAX_PACKET_SIZE];
        if let Ok((size, src)) = self.socket.recv_from(&mut buf) {
            if src == self.server_addr {
                if let Some((start, length, payload)) = Self::parse_response(&buf[..size]) {
                    if let Some(req) = self.pending_requests.get(&start) {
                        if req.length == length {
                            self.received_chunks.insert(start, payload);
                            self.pending_requests.remove(&start);
                        }
                    }
                }
            }
        }
        Ok(())
    }

    fn parse_response(packet: &[u8]) -> Option<(usize, usize, Vec<u8>)> {
        if let Some(pos) = packet.iter().position(|&b| b == b'\n') {
            let header = std::str::from_utf8(&packet[..pos]).ok()?;
            let mut parts = header.split_whitespace();
            if parts.next()? != "DATA" {
                return None;
            }
            let start: usize = parts.next()?.parse().ok()?;
            let length: usize = parts.next()?.parse().ok()?;
            let data = packet[pos + 1..].to_vec();
            if data.len() == length {
                Some((start, length, data))
            } else {
                None
            }
        } else {
            None
        }
    }

    fn retransmit_requests(&mut self) -> io::Result<()> {
        let now = Instant::now();
        let mut to_retransmit = Vec::new();

        for req in self.pending_requests.values_mut() {
            if now.duration_since(req.last_request) > Duration::from_millis(TIMEOUT_MS) {
                to_retransmit.push((req.start, req.length));
                req.last_request = Instant::now();
            }
        }

        for (start, length) in to_retransmit {
            self.send_request(start, length)?;
        }

        Ok(())
    }

    fn write_ready_chunks(&mut self) -> io::Result<()> {
        while let Some(data) = self.received_chunks.remove(&self.written_position) {
            self.file.write_all(&data)?;
            self.written_position += data.len();
        }
        Ok(())
    }
}
