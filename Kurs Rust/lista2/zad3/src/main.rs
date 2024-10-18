fn summy(strng: &str) -> i32 {
    strng.split(" ").filter_map(|s| s.parse::<i32>().ok()).sum()
}

#[cfg(test)]
mod tests {
    use super::summy;
    
    #[test]
    fn sample_tests() {
        assert_eq!(summy("1 2 3"), 6);
        assert_eq!(summy("1 2 3 4"), 10);
        assert_eq!(summy("1 2 3 4 5"), 15);
        assert_eq!(summy("10 10"), 20);
        assert_eq!(summy("0 0"), 0);
    }

    #[test] fn test_sum_empty() { assert_eq!(summy(""), 0); }
    #[test] fn test_sum_single_number() { assert_eq!(summy("5"), 5); }
    #[test] fn test_sum_multiple_numbers() { assert_eq!(summy("1 2 3 4 5"), 15); }
    #[test] fn test_sum_with_negative_numbers() { assert_eq!(summy("-1 -2 3 4"), 4); }
}
