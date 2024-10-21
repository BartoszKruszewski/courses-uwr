// Pierwsza liczba w n-tym wierszu ma przed sobą 1 + 2 + 3 + ... + (n - 1) liczb
// Jest ich (z sumy ciągu arytmetycznego) n(n - 1) / 2 = S
// Więc pierwsza liczba w n-tym wierszu to S * 2 + 1 = n(n - 1) / 2 * 2 + 1 = n^2 - n + 1

// Ostatnia liczba w wierszu jest większa o 2n, więc to n^2 + n - 1
// Suma liczba w wierszu (z sumy ciągu arytmetycznego) to n/2 * (n^2 - n + 1 + n^2 + n - 1) = n^3

fn row_sum_odd_numbers(n: i64) -> i64 {
    n * n * n
}

#[cfg(test)]
mod tests {
    use super::row_sum_odd_numbers;

    #[test]
    fn test_row_1() {
        assert_eq!(row_sum_odd_numbers(1), 1);
    }

    #[test]
    fn test_row_2() {
        assert_eq!(row_sum_odd_numbers(2), 8);
    }

    #[test]
    fn test_row_3() {
        assert_eq!(row_sum_odd_numbers(3), 27);
    }

    #[test]
    fn test_row_4() {
        assert_eq!(row_sum_odd_numbers(4), 64);
    }

    #[test]
    fn test_large_input() {
        assert_eq!(row_sum_odd_numbers(10), 1000);
    }
}
