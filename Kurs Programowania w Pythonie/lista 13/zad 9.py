# zad 2 2017

import turtle as t

I = [("repeat", 10, [("fd", 50), ("repeat", 4, [("fd", 40), ("rt", 90)]), ("bk", 50), ("lt", 36)])]

def do_instructions(L):
    for instruction in L:
        if instruction[0] == "repeat":
            for i in range(instruction[1]):
                do_instructions(instruction[2])
        elif instruction[0] == "fd":
            t.fd(instruction[1])
        elif instruction[0] == "bk":
            t.bk(instruction[1])
        elif instruction[0] == "rt":
            t.rt(instruction[1])
        elif instruction[0] == "lt":
            t.lt(instruction[1])

def compile(L, depth=0):
    output = []
    for instruction in L:
        line = "    " * depth
        if instruction[0] == "repeat":
            line += "for i in range(" + str(instruction[1]) + "):"
            output.append(line)
            for l in compile(instruction[2], depth+1):
                output.append(l)
        else:
            line += "turtle." + instruction[0] + "(" + str(instruction[1]) + ")"
            output.append(line)
    return output

for i in compile(I):
    print(i)
do_instructions(I)