use std::collections::HashSet;

struct Sudoku{
    data: Vec<Vec<u32>>,
}

impl Sudoku{
    fn is_valid(&self) -> bool {
        let n = self.data.len();
        let block_size = (n as f64).sqrt() as usize;

        // check rows
        for row in &self.data {
            if !Sudoku::check_unique(row, n) { return false; }
        }

        // check cols
        for i in 0..n {
            let mut col: Vec<u32> = Vec::new();
            for j in 0..n {
                col.push(self.data[j][i]);
            }
            if !Sudoku::check_unique(&col, n) { return false; }
        }

        // check blocks
        for i in 0..n {
            let block_row = (i / block_size) * block_size;
            let block_col = (i % block_size) * block_size;
            let mut block: Vec<u32> = Vec::new();
            for x in block_row..block_row + block_size {
                for y in block_col..block_col + block_size {
                    block.push(self.data[x][y]);
                }
            }
            if !Sudoku::check_unique(&block, n) { return false; }
        }

        true
    }

    fn check_unique(vec: &Vec<u32>, n: usize) -> bool {
        let unique_numbers: HashSet<_> = vec.into_iter().collect();
        unique_numbers.len() == n as usize && (1..=n).all(|i| unique_numbers.contains(&(i as u32)))
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test1() { 
        assert!(
            Sudoku {
                data: vec![
                    vec![7,8,4, 1,5,9, 3,2,6],
                    vec![5,3,9, 6,7,2, 8,4,1],
                    vec![6,1,2, 4,3,8, 7,5,9],

                    vec![9,2,8, 7,1,5, 4,6,3],
                    vec![3,5,7, 8,4,6, 1,9,2],
                    vec![4,6,1, 9,2,3, 5,8,7],
                    
                    vec![8,7,6, 3,9,4, 2,1,5],
                    vec![2,4,3, 5,6,1, 9,7,8],
                    vec![1,9,5, 2,8,7, 6,3,4]
                ]
            }.is_valid()
        );
    }

    #[test]
    fn test2() { 
        assert!(
            Sudoku{
                data: vec![
                        vec![1, 4,  2, 3],
                        vec![3, 2,  4, 1],
                
                        vec![4, 1,  3, 2],
                        vec![2, 3,  1, 4],
                    ]
            }.is_valid()
        );
    }

    #[test]
    fn test3() { 
        assert!(
            !Sudoku{
                data: vec![
                        vec![1,2,3, 4,5,6, 7,8,9],
                        vec![1,2,3, 4,5,6, 7,8,9],
                        vec![1,2,3, 4,5,6, 7,8,9],
    
                        vec![1,2,3, 4,5,6, 7,8,9],
                        vec![1,2,3, 4,5,6, 7,8,9],
                        vec![1,2,3, 4,5,6, 7,8,9],
                        
                        vec![1,2,3, 4,5,6, 7,8,9],
                        vec![1,2,3, 4,5,6, 7,8,9],
                        vec![1,2,3, 4,5,6, 7,8,9],
                    ]
            }.is_valid()
        );
    }

    #[test]
    fn test4() { 
        assert!(
            !Sudoku{
                data: vec![
                        vec![1,2,3,4,5],
                        vec![1,2,3,4],
                        vec![1,2,3,4],
                        vec![1],
                    ]
            }.is_valid()
        );
    }

    #[test]
    fn test5() { 
        assert!(
            Sudoku{
                data: vec![
                        vec![1, 2, 3, 4],
                        vec![3, 4, 1, 2],
                        vec![2, 3, 4, 1],
                        vec![4, 1, 2, 3],
                    ]
            }.is_valid()
        );
    }
}
