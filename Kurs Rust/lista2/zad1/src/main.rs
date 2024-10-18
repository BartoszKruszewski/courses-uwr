fn get_count(string: &str) -> usize {
    const VOWELS: &str = "aeiou";
    string.chars().filter(| &c| VOWELS.contains(c)).count()
}


#[cfg(test)]
mod tests {
    use super::get_count;

    #[test] fn my_tests() { assert_eq!(get_count("abracadabra"), 5); }
    #[test] fn test_empty_string() { assert_eq!(get_count(""), 0); }
    #[test] fn test_no_vowels() { assert_eq!(get_count("bcdfghjklmnpqrstvwxyz"), 0); }
    #[test] fn test_all_vowels() { assert_eq!(get_count("aeiou"), 5); }
    #[test] fn test_mixed_case() { assert_eq!(get_count("abcdef"), 2); }
    #[test] fn test_special_characters() { assert_eq!(get_count("H@llo W@rld!"), 1); }
}
