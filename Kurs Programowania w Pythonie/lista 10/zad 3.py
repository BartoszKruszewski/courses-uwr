def puzzle_solver(puzzle):
    elements = puzzle.split(" ")
    a = elements[0]
    b = elements[2]
    c = elements[4]
    letters = list(set(list(a + b + c)))
    for i in range(10 - len(letters)):
        letters.append("*")
    permutations = get_permutations(letters)
    solve = {}
    for p in permutations:
        for i in range(10):
            solve[p[i]] = i
        if solve[a[0]] != 0 and solve[b[0]] != 0 and solve[c[0]] != 0:
            if code(a, solve) + code(b, solve) == code(c, solve):
                solve.pop("*")
                return solve

def get_permutations(L):
    if len(L) == 0:
        return [[]]
    ps = get_permutations(L[1:])
    e = L[0]
    return [p[:i] + [e] + p[i:] for p in ps for i in range(len(p)+1)]

def code(a, dict):
    result = 0
    for i in a:
        result = result * 10 + dict[i]
    return result

print(puzzle_solver("send + more = money"))