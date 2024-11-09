fn longest_vowel_chain(s: &str) -> usize {
    s.split(|c| !"aeiou".contains(c)).map(str::len).max().unwrap_or(0)
}

#[cfg(test)]
mod tests {
    use super::longest_vowel_chain;

    #[test] fn test1() { assert_eq!(longest_vowel_chain("codewarriors"), 2); }
    #[test] fn test2() { assert_eq!(longest_vowel_chain("suoidea"), 3); }
    #[test] fn test3() { assert_eq!(longest_vowel_chain("ultrarevolutionariees"), 3); }
    #[test] fn test4() { assert_eq!(longest_vowel_chain("strengthlessnesses"), 1); }
    #[test] fn test5() { assert_eq!(longest_vowel_chain("cuboideonavicuare"), 2); }
    #[test] fn test6() { assert_eq!(longest_vowel_chain("chrononhotonthuooaos"), 5); }
    #[test] fn test7() { assert_eq!(longest_vowel_chain("iiihoovaeaaaoougjyaw"), 8); }
}