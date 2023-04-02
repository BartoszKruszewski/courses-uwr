def matrix_to_tab(M):
    T = [None] * len(M) * len(M)
    index = 0
    for line in range(len(M)):
        for i in range(len(M)):
            if M[line][i]:
                T[index] = (line, i)
                index += 1
    return T

def tab_to_matrix(T):
    maximum = 0
    for i in range(len(T)):
        if T[i][0] > maximum:
            maximum = T[i][0]
        if T[i][1] > maximum:
            maximum = T[i][1]

    maximum += 1

    M = [[0 for i in range(maximum)] for i in range(maximum)]

    for i in range(len(T)):

        M[T[i][0]][T[i][1]] = 1

    return M

matrix = [
    [0,0,0,0,1],
    [0,0,1,0,0],
    [0,0,0,0,1],
    [0,1,0,0,1],
    [0,0,0,0,1]
]

tab = [(0,3),(1,2),(4,1)]


print(tab_to_matrix(tab))
print(matrix_to_tab(matrix))