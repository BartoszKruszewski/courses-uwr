struct Interpreter {
    grid: Vec<Vec<bool>>,
    ins: Vec<char>,
    x: usize,
    y: usize,
    counter: usize,
    actual_iterations: usize,
    width: usize,
    height: usize
}

impl Interpreter {
    fn new(code: &str, width: usize, height: usize) -> Self {
        Interpreter {
            grid: vec![vec![false; width]; height],
            ins: code.chars().filter(|&c| "nesw*[]".contains(c)).collect::<Vec<char>>(),
            x: 0,
            y: 0,
            counter: 0,
            actual_iterations: 0,
            width: width,
            height: height
        }
    }

    fn exec(&mut self, iterations: usize) {
        while self.counter < self.ins.len() && self.actual_iterations < iterations {
            self.actual_iterations += 1;
            match self.ins[self.counter] {
                'n' => self.y = (self.y + self.height - 1) % self.height,
                'e' => self.x = (self.x + 1) % self.width,
                's' => self.y = (self.y + 1) % self.height,
                'w' => self.x = (self.x + self.width - 1) % self.width, 
                '*' => self.grid[self.y][self.x] = !self.grid[self.y][self.x],
                '[' => self.exec_bracket('[', ']', 1),
                ']' => self.exec_bracket(']', '[', -1),
                _ => {self.actual_iterations -= 1}
            }
            self.counter += 1;
        }
    }

    fn exec_bracket(&mut self, active: char, opposite: char, step: i32) {
        if (active == '[' && !self.grid[self.y][self.x]) || (active == ']' && self.grid[self.y][self.x]) {
            let mut brackets = 1;
            while brackets > 0 {
                self.counter = (self.counter as i32 + step) as usize;
                match self.ins[self.counter] {
                    x if x == active => brackets += 1,
                    x if x == opposite => brackets -= 1,
                    _ => {}
                }
            }
        }
    }

    fn get_grid_string(&self) -> String {
        self.grid
            .iter()
            .map(|row| {
                row
                    .iter()
                    .map(|&c| if c { "1" } else { "0" })
                    .collect::<Vec<&str>>()
                    .join("") 
            })
            .collect::<Vec<String>>()
            .join("\r\n")
    }
}

#[allow(dead_code)]
fn interpreter(code: &str, iterations: usize, width: usize, height: usize) -> String {
    let mut itp = Interpreter::new(code, width, height);
    itp.exec(iterations);
    itp.get_grid_string()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn simple_cases() {
        assert_eq!(interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 0, 6, 9), "000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000");
        assert_eq!(interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 7, 6, 9), "111100\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000");
        assert_eq!(interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 19, 6, 9), "111100\r\n000010\r\n000001\r\n000010\r\n000100\r\n000000\r\n000000\r\n000000\r\n000000");
        assert_eq!(interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 42, 6, 9), "111100\r\n100010\r\n100001\r\n100010\r\n111100\r\n100000\r\n100000\r\n100000\r\n100000");
        assert_eq!(interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 100, 6, 9), "111100\r\n100010\r\n100001\r\n100010\r\n111100\r\n100000\r\n100000\r\n100000\r\n100000");
    }
}