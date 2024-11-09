mod image;
mod complex;

use image::Image;
use complex::Complex;

fn mandelbrot(c: Complex, max_iter: usize) -> usize {
    let mut z = Complex::new(0.0, 0.0);
    for i in 0..max_iter {
        z = z * z + c;
        if z.modulus() > 2.0 {
            return i;
        }
    }
    max_iter
}

fn generate_mandelbrot(res: usize, max_iter: usize) -> Image {
    let mut image = Image::new(res, res);

    for px in 0..res {
        for py in 0..res {

            // Zamiana wspolrzednych dyskretnych na ciagle od -1 do 1
            let x = 2.0 * (px as f64) / (res as f64 - 1.0) - 1.0;
            let y = 2.0 * (py as f64) / (res as f64 - 1.0) - 1.0;

            // Wyznaczenie wartosci fraktalu w punkcie
            let m = mandelbrot(Complex::new(x, y), max_iter);

            // Mapowanie na sinusoide dla zroznicowania kolorów
            let r = (255.0 * (m as f64 * 0.16).sin()) as u8;
            let g = (255.0 * (m as f64 * 0.08).sin()) as u8;
            let b = (255.0 * (m as f64 * 0.04).sin()) as u8;

            image.set_pixel(px, py, (r, g, b));
        }
    }
    image
}

fn main() {
    let res = 1000;
    let max_iter = 1000;
    let img = generate_mandelbrot(res, max_iter);
    let file_name = format!("mandelbrot_{}_{}.ppm", res, max_iter);
    img.save_ppm(&file_name).expect("Failed to save the image.");
}

#[cfg(test)]
mod tests {
    use super::*;
    use complex::Complex;

    #[test]
    fn test_mandelbrot() {
        // Test known points within the Mandelbrot set
        assert_eq!(mandelbrot(Complex::new(0.0, 0.0), 1000), 1000);
        assert_eq!(mandelbrot(Complex::new(-1.0, 0.0), 1000), 1000);

        // Test points outside the Mandelbrot set
        assert!(mandelbrot(Complex::new(2.0, 2.0), 1000) < 1000);
        assert!(mandelbrot(Complex::new(-2.0, -2.0), 1000) < 1000);
    }

    #[test]
    fn test_generate_mandelbrot() {
        let res = 10;
        let max_iter = 100;
        let image = generate_mandelbrot(res, max_iter);

        // Test if image dimensions are correct
        assert_eq!(image.get_width(), res);
        assert_eq!(image.get_height(), res);

        // Check some pixels have color values set
        let (r, g, b) = image.get_pixel(0, 0).unwrap();
        assert!(r < 255 || g < 255 || b < 255, "Expected non-white pixel color.");
    }
}

