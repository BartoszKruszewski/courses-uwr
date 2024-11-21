fn comp(a: Vec<i64>, b: Vec<i64>) -> bool {
    if a.len() != b.len() { return false; }

    let mut a_squared = a.iter().map(|&x| x * x).collect::<Vec<_>>();
    let mut b_sorted = b.to_vec();
    
    a_squared.sort();
    b_sorted.sort();

    a_squared == b_sorted
}

#[cfg(test)]
mod tests {
    use super::comp;

    fn testing(a: Vec<i64>, b: Vec<i64>, exp: bool) -> () {
        assert_eq!(comp(a, b), exp)
    }

    #[test] fn test1() { testing(vec![121, 144, 19, 161, 19, 144, 19, 11], vec![11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19], true); } 
    #[test] fn test2() { testing(vec![121, 144, 19, 161, 19, 144, 19, 11], vec![11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19], false); } 
    #[test] fn test3() { testing(vec![1, 1, 2, 2], vec![2*2, 1*1, 2*2, 1*1], true); }
    #[test] fn test4() { testing(vec![9, 25, 49, 64], vec![64*64, 9*9, 25*25, 49*49], true); }
    #[test] fn test5() { testing(vec![5, 10, 15], vec![25, 100, 225], true); }
}   
