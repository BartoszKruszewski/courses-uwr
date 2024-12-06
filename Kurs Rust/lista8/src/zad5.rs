#[allow(dead_code)]
fn first_n_smallest(arr: &[i32], n: usize) -> Vec<i32> {
    if n == 0 || arr.is_empty() { return Vec::new(); }

    let mut sorted_smallest: Vec<i32> = arr.to_vec();
    sorted_smallest.sort_unstable();
    sorted_smallest.truncate(n);

    let mut result = Vec::new();

    for &num in arr {
        if let Some(pos) = sorted_smallest.iter().position(|&x| x == num) {
            result.push(num);
            sorted_smallest.remove(pos);
        }
    }

    result
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_basic() {
        assert_eq!(first_n_smallest(&[1,2,3,4,5],3), [1,2,3]);
        assert_eq!(first_n_smallest(&[5,4,3,2,1],3), [3,2,1]);
        assert_eq!(first_n_smallest(&[1,2,3,1,2],3), [1,2,1]);
        assert_eq!(first_n_smallest(&[1,2,3,-4,0],3), [1,-4,0]);
        assert_eq!(first_n_smallest(&[1,2,3,4,5],0), []);
        assert_eq!(first_n_smallest(&[1,2,3,4,5],5), [1,2,3,4,5]);
        assert_eq!(first_n_smallest(&[1,2,3,4,2],4), [1,2,3,2]);
        assert_eq!(first_n_smallest(&[2,1,2,3,4,2],2), [2,1]);
        assert_eq!(first_n_smallest(&[2,1,2,3,4,2],3), [2,1,2]);
        assert_eq!(first_n_smallest(&[2,1,2,3,4,2],4), [2,1,2,2]);
    }
}
