use std::ops::{Add, Mul};

#[derive(Debug, Clone, Copy)]
pub struct Complex {
    pub real: f64,
    pub imag: f64,
}

impl Complex {
    pub fn new(real: f64, imag: f64) -> Self {
        Complex { real, imag }
    }

    pub fn modulus(self) -> f64 {
        (self.real * self.real + self.imag * self.imag).sqrt()
    }
}

impl Add for Complex {
    type Output = Self;

    fn add(self, other: Self) -> Self {
        Complex {
            real: self.real + other.real,
            imag: self.imag + other.imag,
        }
    }
}

impl Mul for Complex {
    type Output = Self;

    fn mul(self, other: Self) -> Self {
        Complex {
            real: self.real * other.real - self.imag * other.imag,
            imag: self.real * other.imag + self.imag * other.real,
        }
    }
}
