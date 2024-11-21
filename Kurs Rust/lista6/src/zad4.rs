fn largest_difference(data: &[i32]) -> usize {
    let mut max_diff = 0;
    for i in 0..data.len() {
        for j in (i + 1)..data.len() {
            if data[i] <= data[j] {
                max_diff = max_diff.max(j - i);
            }
        }
    }
    max_diff
}

#[cfg(test)]
mod tests {
    use super::largest_difference;
    
    fn dotest(data: &[i32], expected: usize) {
        assert_eq!(largest_difference(data), expected)
    }

    #[test] fn test1() { dotest(&[9, 4, 1, 10, 3, 4, 0, -1, -2], 4); }
    #[test] fn test2() { dotest(&[3, 2, 1], 0); }
    #[test] fn test3() { dotest(&[1, 2, 3], 2); }
    #[test] fn test4() { dotest(&[9, 4, 1, 2, 3, 0, -1, -2], 2); }
    #[test] fn test5() { dotest(&[9, 4, 1, 2, 3, 4, 0, -1, -2], 4); }
    #[test] fn test6() { dotest(&[78, 88, 64, 94, 17, 91, 57, 69, 38, 62, 13, 17, 35, 15, 20], 10); }
    #[test] fn test7() { dotest(&[4, 3, 3, 1, 5, 2], 4); }
}
