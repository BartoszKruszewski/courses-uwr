from zad2 import Var, Const, Not, Or, And

exp1 = Not(And(Var('x'), Or(Var('y'), Const(True)))) # ¬(x ∧ (y ∨ ⊤))
exp2 = Or(Var('x'), Const(False)) # (x ∨ ⊥)
values = {'x': True, 'y': False}

print(exp1)
print(exp2)

print(exp1.eval(values))
print(exp2.eval(values))

print(exp1 + exp2)
print(exp1 * exp2)

print(exp2.get_free_variables())
print((exp1 + exp2).get_free_variables())

print(exp1.is_tautology())
print(exp2.is_tautology())
print(Const(True).is_tautology())
print(Const(False).is_tautology())
print(Var('x').is_tautology())
print(Or(Var('x'), Not(Var('x'))).is_tautology()) # (x ∨ ¬x)
print(Not(And(Var('x'), Const(False))).is_tautology()) # ¬(x ∧ ⊥)

print(And(Var('x'), Const(False)).simplify())
print(Var('x').simplify())

try:
    print(Var('x').eval({}))
except Exception as e:
    print(e)
