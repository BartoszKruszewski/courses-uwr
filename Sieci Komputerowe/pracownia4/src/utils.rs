// Bartosz Kruszewski 337568

use std::path::Path;

pub fn mime_type(path: &Path) -> &'static str {
    match path
        .extension()
        .and_then(|e| e.to_str())
        .unwrap_or("")
        .to_ascii_lowercase()
        .as_str()
    {
        "html" | "htm" => "text/html; charset=utf-8",
        "txt" => "text/plain; charset=utf-8",
        "css" => "text/css",
        "jpg" | "jpeg" => "image/jpeg",
        "png" => "image/png",
        "pdf" => "application/pdf",
        _ => "application/octet-stream",
    }
}

pub fn status_color(code: u16) -> &'static str {
    match code {
        200 => "\x1b[92m",
        301 => "\x1b[93m",
        403 | 404 | 501 => "\x1b[91m",
        _ => "\x1b[0m",
    }
}
