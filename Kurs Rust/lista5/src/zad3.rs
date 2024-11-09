fn solution(n: f64) -> f64 {
    (n * 2.0).round() / 2.0
}

#[cfg(test)]
mod tests {
    use super::solution;
    
    #[test] fn test1() { assert_eq!(solution(4.2), 4.0); }
    #[test] fn test2() { assert_eq!(solution(4.4), 4.5); }
    #[test] fn test3() { assert_eq!(solution(4.6), 4.5);}
    #[test] fn test4() { assert_eq!(solution(4.8), 5.0);}
    #[test] fn test5() { assert_eq!(solution(100.0), 100.0); }
}