fn order_weight(s: &str) -> String {
    let mut v: Vec<&str> = s.split_whitespace().into_iter().collect();
    v.sort_by(|&a, &b| {
        let sum_a = a.chars().fold(0 as u32, |acc, c| acc + c.to_digit(10).unwrap());
        let sum_b = b.chars().fold(0 as u32, |acc, c| acc + c.to_digit(10).unwrap());
        sum_a.cmp(&sum_b).then_with(|| a.cmp(b))
    });
    v.join(" ")
}   

#[cfg(test)]
mod tests {
    use super::order_weight;

    fn testing(s: &str, exp: &str) -> () { assert_eq!(order_weight(s), exp) }

    #[test] fn test1() { testing("103 123 4444 99 2000", "2000 103 123 4444 99"); }
    #[test] fn test2() { testing("2000 10003 1234000 44444444 9999 11 11 22 123", "11 11 2000 10003 22 123 1234000 44444444 9999"); }
    #[test] fn test3() { testing("12 21 30 3", "12 21 3 30"); }
    #[test] fn test4() { testing("81 54 71 17 42", "42 17 71 54 81"); }
    #[test] fn test5() { testing("42", "42"); }
}
