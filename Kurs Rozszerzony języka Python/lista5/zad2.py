class Exp:
    def eval(self, variables):
        pass

    def __str__(self):
        pass

    def __add__(self, other):
        return Or(self, other)

    def __mul__(self, other):
        return And(self, other)

    def get_free_variables(self):
        pass

    def is_tautology(self):
        def combinations(n):
            if n == 0:
                yield () 
            else:
                for val in (True, False):
                    for combo in combinations(n - 1):
                        yield val, *combo

        free_variables = self.get_free_variables()
        return all(
            self.eval(dict(zip(free_variables, valuation)))
            for valuation in combinations(len(free_variables))
        )
    
    def simplify(self):
        return Const(False) if isinstance(self, And) and \
            ((
                isinstance(self.exp1, Var) and \
                isinstance(self.exp2, Const) and \
                not self.exp2.val
            ) or \
            (
                isinstance(self.exp2, Var) and \
                isinstance(self.exp1, Const) and \
                not self.exp1.val
            )) else self
    

class ExpException(Exception):
    pass


class Var(Exp):
    def __init__(self, name):
        self.name = name

    def eval(self, variables):
        if self.name in variables:
            return variables[self.name]
        raise ExpException(f'No assigned value for variable "{self.name}"!')
    
    def __str__(self):
        return self.name
    
    def get_free_variables(self):
        return set(self.name)


class Const(Exp):
    def __init__(self, val):
        self.val = val

    def eval(self, variables):
        return self.val
    
    def __str__(self):
        return '⊤' if self.val else '⊥'
    
    def get_free_variables(self):
        return set()


class Not(Exp):
    def __init__(self, exp):
        self.exp = exp

    def eval(self, variables):
        return not self.exp.eval(variables)
    
    def __str__(self):
        return f'¬{self.exp}'
    
    def get_free_variables(self):
        return self.exp.get_free_variables()


class Or(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    
    def eval(self, variables):
        return self.exp1.eval(variables) or self.exp2.eval(variables)
    
    def __str__(self):
        return f'({self.exp1} ∨ {self.exp2})'
    
    def get_free_variables(self):
        return self.exp1.get_free_variables() | self.exp2.get_free_variables()


class And(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def eval(self, variables):
        return self.exp1.eval(variables) and self.exp2.eval(variables)
    
    def __str__(self):
        return f'({self.exp1} ∧ {self.exp2})'
    
    def get_free_variables(self):
        return self.exp1.get_free_variables() | self.exp2.get_free_variables()
    

