fn xo(string: &'static str) -> bool {
    string.chars().fold(0, |acc, c| match c {
        'x' | 'X' => acc + 1,
        'o' | 'O' => acc - 1,
        _ => acc,
    }) == 0
}

#[cfg(test)]
mod tests {
    use super::xo;

    #[test] fn test1() { assert_eq!(xo("xo"), true); }
    #[test] fn test2() { assert_eq!(xo("Xo"), true); }
    #[test] fn test3() { assert_eq!(xo("xxOo"), true); }
    #[test] fn test4() { assert_eq!(xo("xxxm"), false); }
    #[test] fn test5() { assert_eq!(xo("Oo"), false); }
    #[test] fn test6() { assert_eq!(xo("ooom"), false); }
}
