fn last_digit(a_str: &str, b_str: &str) -> i32 {
    if b_str == "0" { return 1; }

    let cycles: Vec<Vec<i32>> = vec![
        vec![0],
        vec![1],
        vec![2, 4, 8, 6],
        vec![3, 9, 7, 1],
        vec![4, 6],
        vec![5],
        vec![6],
        vec![7, 9, 3, 1],
        vec![8, 4, 2, 6],
        vec![9, 1],
    ];

    let a_mod_10 = a_str.chars().last().unwrap().to_digit(10).unwrap();
    let cycle = &cycles[a_mod_10 as usize];
    let cycle_len = cycle.len() as i32;

    let mut b_mod = 0;
    for digit in b_str.chars() {
        let digit_val = digit.to_digit(10).unwrap() as i32;
        b_mod = (b_mod * 10 + digit_val) % cycle_len;
    }

    let b_mod = if b_mod == 0 { cycle_len } else { b_mod };
    cycle[(b_mod - 1) as usize]
}

#[cfg(test)]
mod tests {
    use super::last_digit;

    #[test]
    fn returns_expected() {
        assert_eq!(last_digit("4", "1"), 4);
        assert_eq!(last_digit("4", "2"), 6);
        assert_eq!(last_digit("9", "7"), 9);
        assert_eq!(last_digit("10","10000000000"), 0);
        assert_eq!(last_digit("1606938044258990275541962092341162602522202993782792835301376","2037035976334486086268445688409378161051468393665936250636140449354381299763336706183397376"), 6);
        assert_eq!(last_digit("3715290469715693021198967285016729344580685479654510946723", "68819615221552997273737174557165657483427362207517952651"), 7);
    }

    #[test]
    fn test_small_numbers() {
        assert_eq!(last_digit("2", "3"), 8);
        assert_eq!(last_digit("2", "4"), 6);
        assert_eq!(last_digit("3", "2"), 9);
        assert_eq!(last_digit("7", "1"), 7);
        assert_eq!(last_digit("5", "1000000000"), 5);
        assert_eq!(last_digit("4", "7"), 4);
    }

    #[test]
    fn test_large_numbers() {
        assert_eq!(last_digit("123456789", "987654321987654321987654321"), 9);
        assert_eq!(last_digit("2", "100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"), 6);
        assert_eq!(last_digit("7", "987654321987654321"), 7);
    }

    #[test]
    fn test_cycles() {
        assert_eq!(last_digit("3", "1000000000000000000000000000"), 1);
        assert_eq!(last_digit("9", "0"), 1);
        assert_eq!(last_digit("8", "100000"), 6);
    }

    #[test]
    fn test_small_exponent() {
        assert_eq!(last_digit("2", "1"), 2);
        assert_eq!(last_digit("9", "1"), 9);
        assert_eq!(last_digit("4", "1"), 4);
    }

    #[test]
    fn test_large_exponent() {
        assert_eq!(last_digit("6", "100000000000000000000000000000"), 6);
        assert_eq!(last_digit("2", "1000000000000000000000000000000"), 6);
        assert_eq!(last_digit("3", "987654321987654321987654321987654321987654321987654321987654321987654321987654321987654321"), 3);
    }
}
