// Bartosz Kruszewski 337568

use std::fs;
use std::io::{ErrorKind, Write};
use std::net::TcpStream;
use std::path::Path;

use crate::utils::{mime_type, status_color};

pub fn resolve_response(
    stream: &mut TcpStream,
    method: &str,
    url_path: &str,
    host: &str,
    root: &Path,
    close: bool,
) -> std::io::Result<()> {
    if method != "GET" {
        return respond_with(stream, 501, "Not Implemented", "Only GET is supported.");
    }

    if url_path.ends_with('/') {
        let location = format!("{url_path}index.html");
        return respond_redirect(stream, &location);
    }

    let rel_path = url_path.trim_start_matches('/');
    let abs_path = root.join(host).join(rel_path);
    let abs_path = match abs_path.canonicalize() {
        Ok(p) => p,
        Err(_) => return respond_with(stream, 404, "Not Found", "File not found."),
    };

    let allowed_root = match root.join(host).canonicalize() {
        Ok(p) => p,
        Err(_) => return respond_with(stream, 404, "Not Found", "Domain directory not found."),
    };

    if !abs_path.starts_with(&allowed_root) {
        return respond_with(stream, 403, "Forbidden", "Access denied.");
    }

    if !abs_path.is_file() {
        return respond_with(stream, 404, "Not Found", "File not found.");
    }

    respond_file(stream, &abs_path, url_path, close)
}

fn respond_file(
    stream: &mut TcpStream,
    path: &Path,
    url_path: &str,
    close: bool,
) -> std::io::Result<()> {
    let content = fs::read(path)?;
    let mime = mime_type(path);
    write!(
        stream,
        "HTTP/1.1 200 OK\r\nContent-Length: {}\r\nContent-Type: {}\r\n\r\n",
        content.len(),
        mime
    )?;
    try_write_all(stream, &content)?;
    log_response(200, "OK", url_path);
    if close {
        stream.shutdown(std::net::Shutdown::Both).ok();
    }
    Ok(())
}

fn respond_redirect(stream: &mut TcpStream, location: &str) -> std::io::Result<()> {
    let body = format!(
        "<html><body><h1>301 Moved Permanently</h1>\
         <p>Redirect to: <a href=\"{0}\">{0}</a></p></body></html>",
        location
    );
    write!(
        stream,
        "HTTP/1.1 301 Moved Permanently\r\nLocation: {}\r\nContent-Length: {}\r\nContent-Type: text/html; charset=utf-8\r\n\r\n{}",
        location, body.len(), body
    )?;
    log_response(301, "Moved Permanently", location);
    Ok(())
}

fn respond_with(
    stream: &mut TcpStream,
    code: u16,
    reason: &str,
    message: &str,
) -> std::io::Result<()> {
    let body = format!("<html><body><h1>{code} {reason}</h1><p>{message}</p></body></html>");
    write!(
        stream,
        "HTTP/1.1 {} {}\r\nContent-Length: {}\r\nContent-Type: text/html; charset=utf-8\r\n\r\n{}",
        code,
        reason,
        body.len(),
        body
    )?;
    log_response(code, reason, message);
    Ok(())
}

fn try_write_all(stream: &mut TcpStream, data: &[u8]) -> std::io::Result<()> {
    match stream.write_all(data) {
        Err(e) if e.kind() == ErrorKind::BrokenPipe => {
            eprintln!("Broken pipe - client disconnected.");
            Ok(())
        }
        other => other,
    }
}

fn log_response(code: u16, reason: &str, path: &str) {
    let color = status_color(code);
    println!("{}{} {}\x1b[0m - {}", color, code, reason, path);
}
