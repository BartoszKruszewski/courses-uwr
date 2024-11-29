use core::f64;
use std::collections::HashMap;
use crate::syntax::{Ins, Num, Op};
use svg::node::element::{Group, Line};

pub struct Turtle {
    x: f64,
    y: f64,
    angle: f64,
    pen_down: bool,
    doc_group: Group,
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
            doc_group: Group::new(),
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

    pub fn get_bounds(&self) -> (f64, f64, f64, f64) {
        (self.min_x, self.min_y, self.max_x, self.max_y)
    }

    fn exec(&mut self, instructions: &Vec<Ins>, var_env: &HashMap<String, f64>) {
        for instruction in instructions {
            match instruction {
                Ins::Forward(num) => self.move_forward(self.eval(num, var_env)),
                Ins::Backward(num) => self.move_forward(-self.eval(num, var_env)),
                Ins::Left(num) => self.angle = (self.angle + self.eval(num, var_env)) % 360.0,
                Ins::Right(num) => self.angle = (self.angle - self.eval(num, var_env)) % 360.0,
                Ins::PenUp => self.pen_down = false,
                Ins::PenDown => self.pen_down = true,
                Ins::Repeat(num, ins) => for _ in 0..self.eval(num, var_env) as usize { self.exec(ins, var_env); }
                Ins::If(num, ins) => if self.eval(num, var_env) != 0.0 { self.exec(ins, var_env); }
                Ins::Define(name, vars , ins) => { self.fn_env.insert(name.clone(), (vars.clone(), ins.clone())); },
                Ins::Call(name, values) => {
                    let (var_names, ins) = self.fn_env.get(name).unwrap();
                    self.exec(&ins.clone(), &self.add_vars(var_env, var_names, values));
                }
            }
        }
    }

    fn add_vars(&self, var_env: &HashMap<String, f64>, var_names: &Vec<String>, var_values: &Vec<Num>) -> HashMap<String, f64>{
        let mut res = var_env.clone();
        for (var, val) in var_names.iter().zip(var_values) {
            res.insert(var.clone(), self.eval(val, var_env));
        }
        res
    }

    fn eval(&self, num: &Num, var_env: &HashMap<String, f64>) -> f64 {
        match num {
            Num::Value(val) => *val,
            Num::Variable(name) => {*var_env.get(name).expect(&format!("Variable: {name} not in scope!"))},
            Num::Op(op, left, right) => self.call_op(op, self.eval(&**left, var_env), self.eval(&**right, var_env))
        }
    }

    fn call_op(&self, op: &Op, left: f64, right: f64) -> f64 {
        match op {
            Op::Add => left + right,
            Op::Sub => left - right,
            Op::Mul => left * right,
            Op::Div => left / right,
            Op::And => self.to_f64(self.to_bool(left) && self.to_bool(right)),
            Op::Or => self.to_f64(self.to_bool(left) || self.to_bool(right)),
            Op::Eq => self.to_f64(left == right),
            Op::Gt => self.to_f64(left > right),
            Op::Lt => self.to_f64(left < right),
        }
    }

    fn to_bool(&self, input: f64) -> bool {
        if input != 0.0 { true } else { false }
    }

    fn to_f64(&self, input: bool) -> f64 {
        if input { 1.0 } else { 0.0 }
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

            self.min_x = self.min_x.min(new_x);
            self.min_y = self.min_y.min(new_y);
            self.max_x = self.max_x.max(new_x);
            self.max_y = self.max_y.max(new_y);
        }
    }
}
