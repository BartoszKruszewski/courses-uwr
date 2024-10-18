fn gimme_the_letters(sp: &str) -> String {
    (sp.chars().next().unwrap()..=sp.chars().last().unwrap()).collect()
}

#[cfg(test)]
mod tests {
    use super::gimme_the_letters;
        
    fn dotest(sp: &str, expected: &str) {
        let actual = gimme_the_letters(sp);
        assert!(actual == expected, 
            "With sp = \"{sp}\"\nExpected \"{expected}\" but got \"{actual}\"")
    }

    #[test]
    fn fixed_tests() {
        dotest("a-z", "abcdefghijklmnopqrstuvwxyz");
        dotest("h-o", "hijklmno");
        dotest("Q-Z", "QRSTUVWXYZ");
        dotest("J-J", "J");
        dotest("a-b", "ab");
        dotest("A-A", "A");
        dotest("g-i", "ghi");
        dotest("H-I", "HI");
        dotest("y-z", "yz");
        dotest("e-k", "efghijk");
        dotest("a-q", "abcdefghijklmnopq");
        dotest("F-O", "FGHIJKLMNO");
    }
    #[test]fn test_lowercase_range() { dotest("a-d", "abcd"); }
    #[test]fn test_uppercase_range() { dotest("A-D", "ABCD"); }
    #[test]fn test_lowercase_single_letter() { dotest("a-a", "a"); }
    #[test]fn test_uppercase_single_letter() { dotest("A-A", "A"); }
}
