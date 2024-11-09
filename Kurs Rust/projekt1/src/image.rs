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

    pub fn get_pixel(&self, x: usize, y: usize) -> Option<(u8, u8, u8)> {
        if x < self.width && y < self.height { Some(self.pixels[y * self.width + x]) } else { None }
    }

    pub fn get_width(&self) -> usize {
        self.width
    }

    pub fn get_height(&self) -> usize {
        self.height
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

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_image_creation() {
        let image = Image::new(2, 2);
        assert_eq!(image.width, 2);
        assert_eq!(image.height, 2);
        assert_eq!(image.pixels.len(), 4);
        assert_eq!(image.pixels, vec![(255, 255, 255); 4]);
    }

    #[test]
    fn test_set_pixel() {
        let mut image = Image::new(3, 3);
        let color = (0, 128, 255);
        image.set_pixel(1, 1, color);
        assert_eq!(image.pixels[1 * image.width + 1], color);
    }

    #[test]
    fn test_get_pixel() {
        let mut image = Image::new(3, 3);
        let color = (100, 150, 200);
        image.set_pixel(2, 2, color);
        
        assert_eq!(image.get_pixel(2, 2), Some(color)); // Within bounds
        assert_eq!(image.get_pixel(3, 3), None); // Out of bounds
    }

    #[test]
    fn test_save_ppm() {
        let mut image = Image::new(2, 2);
        image.set_pixel(0, 0, (255, 0, 0));
        image.set_pixel(1, 0, (0, 255, 0));
        image.set_pixel(0, 1, (0, 0, 255));
        image.set_pixel(1, 1, (255, 255, 0));

        let filename = "test_output.ppm";
        image.save_ppm(filename).expect("Failed to save PPM file");

        let contents = std::fs::read_to_string(filename).expect("Failed to read PPM file");
        let expected_contents = "P3\n2 2\n255\n255 0 0\n0 255 0\n0 0 255\n255 255 0\n";
        assert_eq!(contents, expected_contents);

        std::fs::remove_file(filename).expect("Failed to delete test PPM file");
    }
}
