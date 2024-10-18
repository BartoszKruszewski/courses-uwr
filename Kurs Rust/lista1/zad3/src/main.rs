fn get_circle_area(square_area: f32) -> f32 {
    (square_area.sqrt() / 2.0).powi(2) * std::f32::consts::PI
}

#[cfg(test)]
mod tests {
    use super::get_circle_area;

    #[test]
    fn success() {
        assert!((get_circle_area(1.0) - 0.78539816).abs() < 1e-8);
        assert!((get_circle_area(4.0) - 3.14159265).abs() < 1e-8);
        assert!((get_circle_area(9.0) - 7.06858347).abs() < 1e-8);
        assert!((get_circle_area(16.0) - 12.56637061).abs() < 1e-8);
        assert!((get_circle_area(25.0) - 19.63495409).abs() < 1e-8);
    }
}