use std::collections::HashMap;

struct Cipher {
    encode_map: HashMap<char, char>,
    decode_map: HashMap<char, char>,
}
  
impl Cipher {
    fn new(map1: &str, map2: &str) -> Self {
        let encode_map = map1.chars().zip(map2.chars()).collect();
        let decode_map = map2.chars().zip(map1.chars()).collect();
        Cipher { encode_map, decode_map }
    }

    fn encode(&self, string: &str) -> String {
        string.chars().map(|c| *self.encode_map.get(&c).unwrap_or(&c)).collect()
    }

    fn decode(&self, string: &str) -> String {
        string.chars().map(|c| *self.decode_map.get(&c).unwrap_or(&c)).collect()
    }
}

#[cfg(test)]
mod test {
    use super::Cipher;

    #[test]
    fn examples() {
        let map1 = "abcdefghijklmnopqrstuvwxyz";
        let map2 = "etaoinshrdlucmfwypvbgkjqxz";

        let cipher = Cipher::new(map1, map2);
        
        assert_eq!(cipher.encode("abc"), "eta");
        assert_eq!(cipher.encode("xyz"), "qxz");
        assert_eq!(cipher.decode("eirfg"), "aeiou");
        assert_eq!(cipher.decode("erlang"), "aikcfu");
    }

    #[test]
    fn test_encode() {
        let map1 = "abcdefghijklmnopqrstuvwxyz";
        let map2 = "etaoinshrdlucmfwypvbgkjqxz";
        let cipher = Cipher::new(map1, map2);

        assert_eq!(cipher.encode("abc"), "eta");
        assert_eq!(cipher.encode("xyz"), "qxz");
        assert_eq!(cipher.encode("hello"), "hiuuf");
        assert_eq!(cipher.encode("rust"), "pgvb");
    }

    #[test]
    fn test_decode() {
        let map1 = "abcdefghijklmnopqrstuvwxyz";
        let map2 = "etaoinshrdlucmfwypvbgkjqxz";
        let cipher = Cipher::new(map1, map2);

        assert_eq!(cipher.decode("eta"), "abc");
        assert_eq!(cipher.decode("qxz"), "xyz");
        assert_eq!(cipher.decode("hiuuf"), "hello");
        assert_eq!(cipher.decode("pgvb"), "rust");
    }

    #[test]
    fn test_empty_string() {
        let map1 = "abcdefghijklmnopqrstuvwxyz";
        let map2 = "etaoinshrdlucmfwypvbgkjqxz";
        let cipher = Cipher::new(map1, map2);

        assert_eq!(cipher.encode(""), "");
        assert_eq!(cipher.decode(""), "");
    }

    #[test]
    fn test_full_alphabet() {
        let map1 = "abcdefghijklmnopqrstuvwxyz";
        let map2 = "etaoinshrdlucmfwypvbgkjqxz";
        let cipher = Cipher::new(map1, map2);

        assert_eq!(cipher.encode("abcdefghijklmnopqrstuvwxyz"), "etaoinshrdlucmfwypvbgkjqxz");
        assert_eq!(cipher.decode("etaoinshrdlucmfwypvbgkjqxz"), "abcdefghijklmnopqrstuvwxyz");
    }
}
