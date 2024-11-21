fn coin_combo(cents: u64) -> [u64; 4] {
    [cents % 5, cents % 25 % 10 / 5, cents % 25 / 10, cents / 25]
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test] fn test1() { assert_eq!(coin_combo(1), [1, 0, 0, 0]); } 
    #[test] fn test2() { assert_eq!(coin_combo(2), [2, 0, 0, 0]) } 
    #[test] fn test3() { assert_eq!(coin_combo(5), [0, 1, 0, 0]); } 
    #[test] fn test4() { assert_eq!(coin_combo(6), [1, 1, 0, 0]); } 
    #[test] fn test5() { assert_eq!(coin_combo(10), [0, 0, 1, 0]); } 
    #[test] fn test6() { assert_eq!(coin_combo(11), [1, 0, 1, 0]); }
    #[test] fn test7() { assert_eq!(coin_combo(15), [0, 1, 1, 0]); }
    #[test] fn test8() { assert_eq!(coin_combo(17), [2, 1, 1, 0]); }
    #[test] fn test9() { assert_eq!(coin_combo(36), [1, 0, 1, 1]); }
    #[test] fn test10() { assert_eq!(coin_combo(20), [0, 0, 2, 0]); }
    #[test] fn test11() { assert_eq!(coin_combo(30), [0, 1, 0, 1]); }
    #[test] fn test12() { assert_eq!(coin_combo(36), [1, 0, 1, 1]); }
    #[test] fn test13() { assert_eq!(coin_combo(43), [3, 1, 1, 1]); }
}
