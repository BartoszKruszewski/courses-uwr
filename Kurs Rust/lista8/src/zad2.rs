#[allow(dead_code)]
fn likes(names: &[&str]) -> String {
    match names {
        [] => "no one likes this".to_string(),
        [first] => format!("{first} likes this"),
        [first, second] => format!("{first} and {second} like this"),
        [first, second, third] => format!("{first}, {second} and {third} like this"),
        [first, second, ..] => format!("{first}, {second} and {} others like this", names.len() - 2),

    }
}

#[cfg(test)]
mod tests {
    use super::likes;

    #[test]
    fn example_tests() {
        assert_eq!(likes(&[]), "no one likes this");
        assert_eq!(likes(&["Peter"]), "Peter likes this");
        assert_eq!(likes(&["Jacob", "Alex"]), "Jacob and Alex like this");
        assert_eq!(
            likes(&["Max", "John", "Mark"]),
            "Max, John and Mark like this"
        );
        assert_eq!(
            likes(&["Alex", "Jacob", "Mark", "Max"]),
            "Alex, Jacob and 2 others like this"
        );
    }
}