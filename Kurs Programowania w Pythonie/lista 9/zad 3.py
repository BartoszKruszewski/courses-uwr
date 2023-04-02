def do(a,b,op):
    if op == "*":
        return a * b
    elif op == "//":
        return a // b
    elif op == "+":
        return a + b
    elif op == "-":
        return a - b

def eval_string(expr):
    elements = expr.split(" ")

    operators = ["*","//","+","-"]
    for o in operators:
        i = 0
        while o in elements:
            if elements[i] == o:
                elements[i] = do(int(elements[i - 1]), int(elements[i + 1]), o)
                elements.pop(i - 1)
                elements.pop(i)
                i = 0
                print(elements)
            i += 1
    return elements[0]

print(eval_string("-3 + 4 * 2 // 6 + 9 - 1"))