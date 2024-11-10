pub fn execute(code: &str) -> String {
    let commands = Command::parse(code);
    let mut steps: Vec<Point> = Vec::new();

    steps.push(Point::new(0, 0));

    let mut rotation = Rotation::Right;

    commands.into_iter().for_each(| command| {
        match command {
            Command::Front(steps_num) => { (0..steps_num).for_each(|_| {
                steps.push(steps.last().unwrap().step(&rotation));
            }); },
            Command::Left(steps_num) => { (0..steps_num).for_each(|_| rotation.rotate_left()); },
            Command::Right(steps_num) => { (0..steps_num).for_each(|_| rotation.rotate_right()); },
        }
    });

    let range = steps.iter().fold((0, 0, 0, 0), | acc, point| {
        (acc.0.min(point.x), acc.1.max(point.x), acc.2.min(point.y), acc.3.max(point.y))
    });
    let grid_size = ((range.1 - range.0 + 1) as usize, (range.3 - range.2 + 1) as usize);
    let grid_offset = (range.0.abs(), range.2.abs());
    let mut grid: Vec<Vec<bool>> = vec![vec![false; grid_size.0]; grid_size.1];

    steps.iter().for_each(|point| {
        grid[(point.y + grid_offset.1) as usize][(point.x + grid_offset.0) as usize] = true;
    });
    grid.reverse();

    grid_to_string(&grid)
}

fn grid_to_string(grid: &Vec<Vec<bool>>) -> String {
    grid.iter()
        .map(|row| {
            row.iter().map(|&val| if val { "*" } else { " " }).collect::<Vec<&str>>().join("")
        })
        .collect::<Vec<String>>()
        .join("\r\n")
}

struct Point {
    x: isize,
    y: isize
}

impl Point {
    fn new(x: isize, y: isize) -> Self {
        Self { x, y }
    }

    fn step(&self, rotation: &Rotation) -> Self {
        match rotation {
            Rotation::Up => Point::new(self.x, self.y + 1),
            Rotation::Down => Point::new(self.x, self.y - 1),
            Rotation::Left => Point::new(self.x - 1, self.y),
            Rotation::Right => Point::new(self.x + 1, self.y),
        }
    }
}

enum Rotation {
    Up,
    Down,
    Left,
    Right
}

impl Rotation {
    fn rotate_left(&mut self) {
        *self = match *self {
            Rotation::Up => Rotation::Left,
            Rotation::Down => Rotation::Right,
            Rotation::Left => Rotation::Down,
            Rotation::Right => Rotation::Up,
        };
    }

    fn rotate_right(&mut self) {
        *self = match *self {
            Rotation::Up => Rotation::Right,
            Rotation::Down => Rotation::Left,
            Rotation::Left => Rotation::Up,
            Rotation::Right => Rotation::Down,
        };
    }
} 

enum Command {
    Front(usize),
    Left(usize),
    Right(usize),
}

impl Command {
    fn new(symbol: char, num_str: &str) -> Self {
        let num = num_str.parse::<usize>().unwrap_or(1);
        match symbol {
            'F' => Command::Front(num),
            'L' => Command::Left(num),
            'R' => Command::Right(num),
            _ => panic!("Wrong command symbol!")
        }
    }

    fn parse(code: &str) -> Vec<Self> {
        let mut res: Vec<Self> = Vec::new();
        let mut command_buffer: Option<char> = None;
        let mut number_buffer = String::new();
        code.chars().for_each(|c| {
            if "FLR".contains(c) {
                if command_buffer != None {
                    res.push(Self::new(command_buffer.unwrap(), &number_buffer));
                }
                command_buffer = Some(c);
                number_buffer = String::new();
            }
            else {
                number_buffer.push(c);
            }
        });
        if command_buffer != None {
            res.push(Self::new(command_buffer.unwrap(), &number_buffer));
        }
        res
    }
}

#[cfg(test)]
    macro_rules! expect_equal {
    ($actual:expr, $expected:expr $(,)*) => {{
        let actual = $actual;
        let expected = $expected;
        assert_eq!(actual, expected, "\ngot:\n{}\n\nexpected:\n{}\n", actual, expected);
    }};
}

#[cfg(test)]
mod tests {
    use super::execute;
    #[test] fn test1() { expect_equal!(execute(""), "*"); }
    #[test] fn test2() { expect_equal!(execute("FFFFF"), "******"); }
    #[test] fn test3() { expect_equal!(execute("FFFFFLFFFFFLFFFFFLFFFFFL"), "******\r\n*    *\r\n*    *\r\n*    *\r\n*    *\r\n******"); }
    #[test] fn test4() { expect_equal!(execute("LFFFFFRFFFRFFFRFFFFFFF"), "    ****\r\n    *  *\r\n    *  *\r\n********\r\n    *   \r\n    *   "); }
    #[test] fn test5() { expect_equal!(execute("LF5RF3RF3RF7"), "    ****\r\n    *  *\r\n    *  *\r\n********\r\n    *   \r\n    *   "); }
}
