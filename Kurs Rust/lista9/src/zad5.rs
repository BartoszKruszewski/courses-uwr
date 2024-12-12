#[allow(unused)]
fn good_vs_evil(good: &str, evil: &str) -> String {
    let good_worth = [1, 2, 3, 3, 4, 10];
    let evil_worth = [1, 2, 2, 2, 3, 5, 10];

    let good_counts: Vec<i32> = good.split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let evil_counts: Vec<i32> = evil.split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();

    let good_total: i32 = good_counts.iter()
        .zip(good_worth.iter())
        .map(|(count, &worth)| count * worth)
        .sum();

    let evil_total: i32 = evil_counts.iter()
        .zip(evil_worth.iter())
        .map(|(count, &worth)| count * worth)
        .sum();

    if good_total > evil_total {
        "Battle Result: Good triumphs over Evil".to_string()
    } else if evil_total > good_total {
        "Battle Result: Evil eradicates all trace of Good".to_string()
    } else {
        "Battle Result: No victor on this battle field".to_string()
    }
}

#[cfg(test)]
mod tests {
    use super::good_vs_evil;

    fn do_test(good: &str, evil: &str, expected: &str) {
        let actual = good_vs_evil(good, evil);
        assert_eq!(
            actual, expected,
            "\n  Good: \"{good}\n  Evil: \"{evil}\"\nYour answer (left) is not the expected answer (right).",
        );
    }

    #[test]
    fn test_good_wins() {
        do_test(
            "1 0 1 0 0 0",
            "1 0 0 0 0 0 0",
            "Battle Result: Good triumphs over Evil",
        );
        do_test(
            "0 0 0 0 0 10",
            "0 0 0 0 0 0 0",
            "Battle Result: Good triumphs over Evil",
        );
    }

    #[test]
    fn test_evil_wins() {
        do_test(
            "1 0 0 0 0 0",
            "0 0 0 0 1 0 0",
            "Battle Result: Evil eradicates all trace of Good",
        );
        do_test(
            "0 0 0 0 0 0",
            "0 0 0 0 0 0 10",
            "Battle Result: Evil eradicates all trace of Good",
        );
    }

    #[test]
    fn test_tie() {
        do_test(
            "1 0 0 0 0 0",
            "1 0 0 0 0 0 0",
            "Battle Result: No victor on this battle field",
        );
        do_test(
            "0 0 0 0 0 10",
            "0 0 0 0 0 0 10",
            "Battle Result: No victor on this battle field",
        );
    }
    #[test]
    fn edge_case() {
        do_test(
            "0 0 0 0 0 0",
            "0 0 0 0 0 0 0",
            "Battle Result: No victor on this battle field",
        );
    }
}
