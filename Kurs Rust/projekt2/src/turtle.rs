use core::f64;
use std::collections::HashMap;
use crate::syntax::{Ins, Num, Op};
use crate::utils::{to_bool, to_f64};
use rand::Rng;
use rand::thread_rng;

enum SvgData {
    Text(TextData),
    Line(LineData)
}

struct TextData {
    x: f64,
    y: f64,
    angle: f64,
    size: usize,
    text: String,
}

struct LineData {
    x1: f64,
    y1: f64,
    x2: f64,
    y2: f64,
}

pub struct Turtle {
    x: f64,
    y: f64,
    angle: f64,
    pen_down: bool,
    svg_data: Vec<SvgData>,
    fn_env: HashMap<String, (Vec<String>, Vec<Ins>)>,
    min_x: f64,
    min_y: f64,
    max_x: f64,
    max_y: f64,
}

impl Turtle {
    pub fn new() -> Self {
        Turtle {
            x: 0.0,
            y: 0.0,
            angle: 0.0,
            pen_down: true,
            svg_data: Vec::new(),
            fn_env: HashMap::new(),
            min_x: f64::INFINITY,
            min_y: f64::INFINITY,
            max_x: -f64::INFINITY,
            max_y: -f64::INFINITY
        }
    }

    pub fn run(&mut self, instructions: &Vec<Ins>) {
        self.exec(instructions, &mut HashMap::new());
    }

    pub fn get_svg(&self) -> String {
        let mut res = format!(
            "<svg viewBox=\"{} {} {} {}\" xmlns=\"http://www.w3.org/2000/svg\">\n",
            self.min_x, self.min_y, self.max_x - self.min_x, self.max_y - self.min_y
        );
        for _svg_data in self.svg_data.iter() {
            match _svg_data {
                SvgData::Line(line) => { 
                    res.push_str(&format!(
                        "<line stroke=\"black\" stroke-width=\"1\" x1=\"{}\" x2=\"{}\" y1=\"{}\" y2=\"{}\"/>\n",
                        line.x1, line.x2, line.y1, line.y2
                    ));
                }
                SvgData::Text(text) => {
                    res.push_str(&format!(
                        "<text x=\"{}\" y=\"{}\" font-size=\"{}px\" transform=\"rotate({} {} {})\">{}</text>\n",
                        text.x, text.y, text.size, text.angle, text.x, text.y, text.text
                    ));
                }
            }
            
        }
        res.push_str("</svg>\n");
        res
    }

    fn exec(&mut self, instructions: &Vec<Ins>, var_env: &mut HashMap<String, f64>) {
        for instruction in instructions {
            match instruction {
                Ins::Forward(num) => self.move_forward(self.eval(num, var_env)),
                Ins::Backward(num) => self.move_forward(-self.eval(num, var_env)),
                Ins::Left(num) => self.angle = (self.angle + self.eval(num, var_env)) % 360.0,
                Ins::Right(num) => self.angle = (self.angle - self.eval(num, var_env)) % 360.0,
                Ins::PenUp => self.pen_down = false,
                Ins::PenDown => self.pen_down = true,
                Ins::Text(size, text) => self.draw_text(text, self.eval(size, var_env) as usize),
                Ins::Repeat(num, ins) => for _ in 0..self.eval(num, var_env) as usize { self.exec(ins, var_env); }
                Ins::If(num, ins) => if self.eval(num, var_env) != 0.0 { self.exec(ins, var_env); }
                Ins::Let(name, val) => { var_env.insert(name.clone(), self.eval(val, var_env)); }
                Ins::Define(name, vars , ins) => { self.fn_env.insert(name.clone(), (vars.clone(), ins.clone())); },
                Ins::Call(name, values) => {
                    let (var_names, ins) = self.fn_env.get(name).unwrap();
                    let mut new_var_env = var_env.clone();
                    for (var, val) in var_names.iter().zip(values) {
                        new_var_env.insert(var.clone(), self.eval(val, var_env));
                    }
                    self.exec(&ins.clone(), &mut new_var_env);
                }
            }
        }
    }

    fn eval(&self, num: &Num, var_env: &HashMap<String, f64>) -> f64 {
        match num {
            Num::Value(val) => *val,
            Num::Variable(name) => {
                if name == "random" {
                    thread_rng().gen()
                }
                else {
                    *var_env.get(name).expect(&format!("Variable: {name} not in scope!"))
                }  
            },
            Num::Op(op, left, right) => self.call_op(op, self.eval(&**left, var_env), self.eval(&**right, var_env))
        }
    }

    fn call_op(&self, op: &Op, left: f64, right: f64) -> f64 {
        match op {
            Op::Add => left + right,
            Op::Sub => left - right,
            Op::Mul => left * right,
            Op::Div => left / right,
            Op::And => to_f64(to_bool(left) && to_bool(right)),
            Op::Or => to_f64(to_bool(left) || to_bool(right)),
            Op::Eq => to_f64(left == right),
            Op::Gt => to_f64(left > right),
            Op::Lt => to_f64(left < right),
        }
    }

    fn move_forward(&mut self, dist: f64) {
        {
            let rad = self.angle.to_radians();
            let new_x = self.x + dist * rad.cos();
            let new_y = self.y - dist * rad.sin();

            if self.pen_down {
                self.svg_data.push(SvgData::Line(LineData{
                    x1: self.x,
                    y1: self.y,
                    x2: new_x,
                    y2: new_y,
                }));
            }

            self.x = new_x;
            self.y = new_y;

            self.min_x = self.min_x.min(new_x);
            self.min_y = self.min_y.min(new_y);
            self.max_x = self.max_x.max(new_x);
            self.max_y = self.max_y.max(new_y);
        }
    }

    fn draw_text(&mut self, text: &str, size: usize) {
        self.svg_data.push(SvgData::Text(TextData{
            x: self.x,
            y: self.y,
            angle: -self.angle,
            size: size,
            text: text.to_string()
        }));
    }
}
