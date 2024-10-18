fn bin_len(input: u32) -> u32 {
    input.count_ones()
}

fn count_bits(n: i64) -> u32 {
    let mut num: i64 = n;
    let mut res: u32 = 0;
    while num > 0 {
        res += (num % 2) as u32;
        num /= 2;
    }
    res
}

#[cfg(test)]
mod tests {
    use super::bin_len;
    use super::count_bits;

    #[test]
    fn idom() {
        assert_eq!(bin_len(1234), 5);
        assert_eq!(bin_len(0), 0);
        assert_eq!(bin_len(1), 1);
        assert_eq!(bin_len(8), 1);
        assert_eq!(bin_len(7), 3);
    }

    #[test]
    fn classic() {
        assert_eq!(count_bits(1234), 5);
        assert_eq!(count_bits(0), 0);
        assert_eq!(count_bits(1), 1);
        assert_eq!(count_bits(8), 1);
        assert_eq!(count_bits(7), 3);
    }
}
