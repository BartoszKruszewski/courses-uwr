fn printer_error(s: &str) -> String {
    format!("{}/{}", s.chars().filter(|&c| c > 'm').count(), s.len())
}

#[cfg(test)]
mod tests {
    use super::printer_error;

    #[test]
    fn success() {
        assert_eq!(printer_error("zhnpgjkqocllpfgfylkbdefb"), "7/24");
        assert_eq!(printer_error("rdrvuwinrinprdkzyuhhaqvwts"), "18/26");
        assert_eq!(printer_error("uotnmcojnoslkatikivclsyi"), "12/24");
        assert_eq!(printer_error("vvssipfin"), "6/9");
        assert_eq!(printer_error("garzxscvjsmahxncoqrhcb"), "11/22");
    }
}
