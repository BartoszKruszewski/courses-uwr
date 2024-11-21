fn wave(s: &str) -> Vec<String> {
    let mut res: Vec<String> = Vec::new();
    for i in 0..s.len() {
        let mut chars: Vec<_> = s.chars().collect();
        if chars[i].is_whitespace() { continue; }
        chars[i] = chars[i].to_uppercase().next().unwrap();
        res.push(chars.into_iter().collect());
    }
    res
}

#[cfg(test)]
mod tests {
    use super::wave;

    #[test] fn test1() { assert_eq!(wave("hello"), ["Hello", "hEllo", "heLlo", "helLo", "hellO"]); }
    #[test] fn test2() { assert_eq!(wave("codewars"), ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]); }
    #[test] fn test3() { let expect: [&str; 0] = []; assert_eq!(wave(""), expect); }
    #[test] fn test4() { assert_eq!(wave("two words"), ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]); }
    #[test] fn test5() { assert_eq!(wave(" gap "), [" Gap ", " gAp ", " gaP "]); }
}        
