#niezrobione


n = 6
tab = [
    [10, 53, 65, 6, 4, 3],
    [7, 4, 7, 4, 5, 69],
    [2, 1, 1, 5, 6, 9],
    [65, 8, 5, 44, 67, 90],
    [21, 45, 23, 87, 5, 4],
    [1, 0, 45, 3, 76, 5]
]

for line in tab:
    print(line)

minimum = 9999999
path = [0] * (n-1) * 2
def move(x, y, s):
    global minimum, path
    if x == n - 1 and y == n - 1:
        if s < minimum:
            minimum = s

    if x < n - 1 and s + tab[x + 1][y] < minimum:
        path[x + y] = tab[x + 1][y]
        move(x + 1, y, s + tab[x + 1][y])
    if y < n - 1 and s + tab[x][y + 1] < minimum:
        path[x + y] = tab[x][y + 1]
        move(x, y + 1, s + tab[x][y + 1])



move(0, 0, -1)
print(minimum)
print(path,sum(path))
