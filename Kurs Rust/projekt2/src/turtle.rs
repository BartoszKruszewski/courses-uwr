use crate::parser::Instruction;
use svg::node::element::{Group, Line};

pub struct Turtle {
    x: f64,
    y: f64,
    angle: f64,
    pen_down: bool,
    doc_group: Group
}

impl Turtle {
    pub fn new() -> Self {
        Turtle {
            x: 0.0,
            y: 0.0,
            angle: 0.0,
            pen_down: true,
            doc_group: Group::new()
        }
    }

    pub fn exec(&mut self, instructions: &Vec<Instruction>) {
        for instruction in instructions {
            match instruction {
                Instruction::Forward(dist) => self.move_forward(*dist),
                Instruction::Backward(dist) => self.move_forward(-*dist),
                Instruction::Left(degrees) => self.angle = (self.angle + degrees) % 360.0,
                Instruction::Right(degrees) => self.angle = (self.angle - degrees) % 360.0,
                Instruction::PenUp => self.pen_down = false,
                Instruction::PenDown => self.pen_down = true,
                Instruction::Repeat(n, ins) => for _ in 0..*n { self.exec(ins); }
            }
        }
    }

    pub fn get_doc_group(&self) -> Group {
        self.doc_group.clone()
    }

    fn move_forward(&mut self, dist: f64) {
        {
            let rad = self.angle.to_radians();
            let new_x = self.x + dist * rad.cos();
            let new_y = self.y - dist * rad.sin();

            if self.pen_down {
                let line = Line::new()
                    .set("x1", self.x)
                    .set("y1", self.y)
                    .set("x2", new_x)
                    .set("y2", new_y)
                    .set("stroke", "black")
                    .set("stroke-width", 2);
                self.doc_group = self.doc_group.clone().add(line);
            }

            self.x = new_x;
            self.y = new_y;
        }
    }
}
