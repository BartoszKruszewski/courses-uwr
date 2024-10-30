use std::fs::File;
use std::io::{Result, Write};

pub struct Image {
    width: usize,
    height: usize,
    pixels: Vec<(u8, u8, u8)>
}

impl Image {
    pub fn new(width: usize, height: usize) -> Self {
        Image { width, height, pixels : vec![(255, 255, 255); width * height] }
    }

    pub fn set_pixel(&mut self, x: usize, y: usize, color: (u8, u8, u8)) {
        if x < self.width && y < self.height {
            self.pixels[y * self.width + x] = color;
        }
    }

    pub fn save_ppm(&self, filename: &str) -> Result<()> {
        let mut file = File::create(filename)?;
        writeln!(file, "P3\n{} {}\n255", self.width, self.height)?;

        for &(r, g, b) in &self.pixels {
            writeln!(file, "{} {} {}", r, g, b)?;
        }

        Ok(())
    }
}
