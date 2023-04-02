class ListItem:
    def __init__(self, value):
        self.val = value
        self.next = None

def matrix_to_tab(M):
    n = len(M)
    T = [None] * n
    index = 0
    for line in range(n):
        first = None
        for i in range(n):
            if M[line][i] == 1:
                if first is None:
                    L = ListItem(i)
                    first = L
                else:
                    L.next = ListItem(i)
                    L = L.next
        T[index] = first
        index += 1
    return T

def tab_to_matrix(T):
    n = len(T)
    M = [[0 for i in range(n)] for i in range(n)]

    for i in range(n):
        L = T[i]
        while L is not None:
            M[i][L.val] = 1
            L = L.next
    return M

mat = [
    [0,0,0,0],
    [0,1,0,1],
    [0,0,1,0],
    [1,0,1,0]
]
print(tab_to_matrix(matrix_to_tab(mat)))
