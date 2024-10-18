fn longest(a1: &str, a2: &str) -> String {
    let mut distinct_vec = [a1, a2]
        .concat()
        .chars()
        .collect::<std::collections::HashSet<char>>()
        .into_iter()
        .collect::<Vec<char>>();
    distinct_vec.sort();
    distinct_vec.into_iter().collect()
}

#[cfg(test)]
mod tests {
    use super::longest;
   
    fn testing(s1: &str, s2: &str, exp: &str) -> () {
        println!("s1:{:?} s2:{:?}", s1, s2);
        println!("{:?} {:?}", longest(s1, s2), exp);
        println!("{}", longest(s1, s2) == exp);
        assert_eq!(&longest(s1, s2), exp)
    }

    #[test]
    fn basic_tests() {
        testing("aretheyhere", "yestheyarehere", "aehrsty");
        testing("loopingisfunbutdangerous", "lessdangerousthancoding", "abcdefghilnoprstu");
    }
    #[test] fn test_empty_strings() { testing("", "", ""); }
    #[test] fn test_identical_strings() { testing("abc", "abc", "abc"); }
    #[test] fn test_non_overlapping_strings() { testing("abc", "def", "abcdef"); }
    #[test] fn test_partial_overlap() { testing("abc", "bcd", "abcd"); }
    #[test] fn test_distinct_characters() { testing("abc", "xyz", "abcxyz"); }
}
