def convert(exp):
    def priority(operator):
        if operator in ['+', '-']:
            return 1
        if operator in ['*', '/']:
            return 2
        return 0

    result = []
    stack = []

    for ch in exp:
        if isinstance(ch, int):
            result.append(ch)
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while stack and priority(stack[-1]) >= priority(ch):
                result.append(stack.pop())
            stack.append(ch)

    while stack:
        result.append(stack.pop())

    return result

def eval(exp):
    stack = []

    for ch in exp:
        if isinstance(ch, int):
            stack.append(ch)
        else:
            n2 = stack.pop()
            n1 = stack.pop()
            if ch == '+':
                stack.append(n1 + n2)
            elif ch == '-':
                stack.append(n1 - n2)
            elif ch == '*':
                stack.append(n1 * n2)
            elif ch == '/':
                stack.append(n1 / n2)

    return stack[0]

infix_expression = ['(', 2, '+', 3, ')', '*', 4]
rpn_expression = convert(infix_expression)
print("RPN:", rpn_expression)
print("Result:", eval(rpn_expression))
