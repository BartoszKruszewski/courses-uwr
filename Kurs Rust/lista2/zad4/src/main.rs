fn count_red_beads(n: u32) -> u32 {
    n.saturating_sub(1) * 2
}

#[cfg(test)]
mod tests {
    use super::count_red_beads;
    #[test]
    fn test() {
      assert_eq!(count_red_beads(0), 0);
      assert_eq!(count_red_beads(1), 0);
      assert_eq!(count_red_beads(3), 4);
      assert_eq!(count_red_beads(5), 8);
    }

    #[test] fn test_count_red_beads_two() { assert_eq!(count_red_beads(2), 2); }
    #[test] fn test_count_red_beads_four() { assert_eq!(count_red_beads(4), 6); }
    #[test] fn test_count_red_beads_ten() { assert_eq!(count_red_beads(10), 18); }
    #[test] fn test_count_red_beads_large() { assert_eq!(count_red_beads(1000), 1998); }
}
