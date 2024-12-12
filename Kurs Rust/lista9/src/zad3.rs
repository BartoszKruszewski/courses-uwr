#[allow(unused)]
fn stock_list(list_art: Vec<&str>, list_cat: Vec<&str>) -> String {
    if list_art.is_empty() { return String::new(); }
    list_cat.iter().map(|&category| {
        let total = list_art
            .iter()
            .filter(|&entry| entry.starts_with(category))
            .map(|entry| entry
                .split_whitespace()
                .nth(1)
                .unwrap_or("0")
                .parse::<i32>()
                .unwrap_or(0)
            )
            .sum::<i32>();
        format!("({} : {})", category, total)
    }).collect::<Vec<String>>().join(" - ")
}

#[cfg(test)]
    mod tests {
    use super::*;

    fn dotest(list_art: Vec<&str>, list_cat: Vec<&str>, exp: &str) -> () {
        println!("list_art: {:?};", list_art);
        println!("list_cat: {:?};", list_cat);
        let ans = stock_list(list_art, list_cat);
        println!("actual:\n{:?};", ans);
        println!("expect:\n{:?};", exp);
        println!("{};", ans == exp);
        assert_eq!(ans, exp);
        println!("{};", "-");
    }

    #[test]
    fn basic_tests() {
        let mut b = vec!["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"];
        let mut c = vec!["A", "B", "C", "D"];
        dotest(b, c, "(A : 0) - (B : 1290) - (C : 515) - (D : 600)");

        b = vec!["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"];
        c = vec!["A", "B"];
        dotest(b, c, "(A : 200) - (B : 1140)");

    }
}
