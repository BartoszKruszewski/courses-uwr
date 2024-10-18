fn str_to_i32(input: &str) -> i32 {
    input.parse::<i32>().unwrap()
}

#[cfg(test)]
mod tests {
    use super::str_to_i32;

    #[test]
    fn success() {
        assert_eq!(str_to_i32("1234"), 1234);
        assert_eq!(str_to_i32("605"), 605);
        assert_eq!(str_to_i32("1405"), 1405);
        assert_eq!(str_to_i32("-7"), -7);
        assert_eq!(str_to_i32("-89"), -89);
    }
}
