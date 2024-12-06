struct Cache {
    ann: Vec<i32>,
    john: Vec<i32>
}

impl Cache {
    fn new(n: i32) -> Self {
        Cache {
            ann: [vec![1], vec![-1; n as usize]].concat(),
            john: [vec![0], vec![-1; n as usize]].concat(),
        }
    }

    fn j(&mut self, n: i32) -> i32 {
        if self.john[n as usize] != -1 { return self.john[n as usize]; }
        let x = self.j(n - 1);
        let res = n - self.a(x);
        self.john[n as usize] = res;
        res
    }

    fn a(&mut self, n: i32) -> i32 {
        if self.ann[n as usize] != -1 { return self.ann[n as usize]; }
        let x = self.a(n - 1);
        let res = n - self.j(x);
        self.ann[n as usize] = res;
        res
    }
}

#[allow(dead_code)]
fn john(n: i32) -> Vec<i32> {
    let mut cache = Cache::new(n);
    (0..n).map(|i| cache.j(i)).collect()
}

#[allow(dead_code)]
fn ann(n: i32) -> Vec<i32> {
    let mut cache = Cache::new(n);
    (0..n).map(|i| cache.a(i)).collect()
}

#[allow(dead_code)]
fn sum_john(n: i32) -> i32 {
    john(n).iter().sum()
}

#[allow(dead_code)]
fn sum_ann(n: i32) -> i32 {
    ann(n).iter().sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_john() {
        assert_eq!(john(11), vec![0, 0, 1, 2, 2, 3, 4, 4, 5, 6, 6]);
        assert_eq!(john(14), vec![0, 0, 1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 7, 8]);
    }
    #[test]
    fn test_ann() {
        assert_eq!(ann(6), vec![1, 1, 2, 2, 3, 3]);
        assert_eq!(ann(15), vec![1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 8, 8, 9]);
    }
    #[test]
    fn test_sum_john() {
        assert_eq!(sum_john(75), 1720);
        assert_eq!(sum_john(78), 1861);
    }
    #[test]
    fn test_sum_ann() {
        assert_eq!(sum_ann(115), 4070);
        assert_eq!(sum_ann(150), 6930);
    }
}