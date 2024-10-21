fn number(bus_stops:&[(i32,i32)]) -> i32 {
    bus_stops.into_iter().map(|e| e.0-e.1).sum()
}

#[cfg(test)]
mod tests {
    use super::number;

    #[test]
    fn test_empty_bus_stops() {
        assert_eq!(number(&[]), 0);
    }

    #[test]
    fn test_single_stop() {
        assert_eq!(number(&[(10, 0)]), 10);
    }

    #[test]
    fn test_multiple_stops() {
        assert_eq!(number(&[(10, 0), (3, 5), (2, 8)]), 2);
    }

    #[test]
    fn test_all_exit() {
        assert_eq!(number(&[(5, 5), (10, 10), (3, 3)]), 0);
    }
    
    #[test]
    fn test_large_numbers() {
        assert_eq!(number(&[(1000, 500), (300, 100), (200, 400)]), 500);
    }
}
