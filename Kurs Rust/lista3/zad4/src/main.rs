// Wersja normalna:

// use std::cmp::min;

// fn zoom(n: usize) -> String {
//     let mut square = Vec::new();
//     let char1 = if (n - 1) % 4 == 0 { '■' } else { '□' };
//     let char2 = if (n - 1) % 4 == 0 { '□' } else { '■' };

//     for i in 0..n {
//         let mut row = String::new();
//         for j in 0..n {
//             let zoom_level = min(min(i, j), min(n - i - 1, n - j - 1));
//             row.push( if zoom_level % 2 == 0 { char1 } else { char2 });
//         }
//         square.push(row);
//     }

//     square.join("\n")
// }

// Wersja idiomatyczna:

fn zoom(n: i32) -> String {
    let n = n as usize;
    let char1 = if (n - 1) % 4 == 0 { '■' } else { '□' };
    let char2 = if (n - 1) % 4 == 0 { '□' } else { '■' };

    (0..n).map(|i| 
        (0..n).map(|j| 
            [char1, char2][[i, j, n - i - 1, n - j - 1].iter().min().unwrap() % 2]
        ).collect::<String>()
    ).collect::<Vec<_>>().join("\n")
}

#[cfg(test)]
mod test {
    use super::zoom;

    #[test]
    fn basic_test_1() {
        assert_eq!(zoom(1), "■");
    }

    #[test]
    fn basic_test_2() {
        assert_eq!(zoom(3), "\
□□□
□■□
□□□"
        );
    }

    #[test]
    fn basic_test_3() {
        assert_eq!(zoom(5), "\
■■■■■
■□□□■
■□■□■
■□□□■
■■■■■"
        );
    }

    #[test]
    fn basic_test_4() {
        assert_eq!(zoom(7), "\
□□□□□□□
□■■■■■□
□■□□□■□
□■□■□■□
□■□□□■□
□■■■■■□
□□□□□□□"
        );
    }

    #[test]
    fn basic_test_5() {
        assert_eq!(zoom(9), "\
■■■■■■■■■
■□□□□□□□■
■□■■■■■□■
■□■□□□■□■
■□■□■□■□■
■□■□□□■□■
■□■■■■■□■
■□□□□□□□■
■■■■■■■■■"
        );
    }
}
