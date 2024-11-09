use std::ops::{Add, Mul, Sub, Div};

#[derive(Debug, Clone, Copy, PartialEq)]
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

    pub fn conjugate(self) -> Self {
        Complex {
            real: self.real,
            imag: -self.imag,
        }
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

impl Sub for Complex {
    type Output = Self;

    fn sub(self, other: Self) -> Self {
        Complex {
            real: self.real - other.real,
            imag: self.imag - other.imag,
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

impl Div for Complex {
    type Output = Self;

    fn div(self, other: Self) -> Self {
        let denominator = other.real * other.real + other.imag * other.imag;
        Complex {
            real: (self.real * other.real + self.imag * other.imag) / denominator,
            imag: (self.imag * other.real - self.real * other.imag) / denominator,
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_addition() {
        let a = Complex::new(1.0, 2.0);
        let b = Complex::new(3.0, 4.0);
        assert_eq!(a + b, Complex::new(4.0, 6.0));
    }

    #[test]
    fn test_subtraction() {
        let a = Complex::new(5.0, 6.0);
        let b = Complex::new(3.0, 4.0);
        assert_eq!(a - b, Complex::new(2.0, 2.0));
    }

    #[test]
    fn test_multiplication() {
        let a = Complex::new(1.0, 2.0);
        let b = Complex::new(3.0, 4.0);
        assert_eq!(a * b, Complex::new(-5.0, 10.0));
    }

    #[test]
    fn test_division() {
        let a = Complex::new(1.0, 2.0);
        let b = Complex::new(3.0, 4.0);
        assert_eq!(a / b, Complex::new(0.44, 0.08));
    }

    #[test]
    fn test_modulus() {
        let a = Complex::new(3.0, 4.0);
        assert_eq!(a.modulus(), 5.0);
    }

    #[test]
    fn test_conjugate() {
        let a = Complex::new(1.0, -2.0);
        assert_eq!(a.conjugate(), Complex::new(1.0, 2.0));
    }
}
