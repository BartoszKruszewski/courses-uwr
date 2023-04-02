size = 8

board = []
for i in range(size):
    board.append([0] * size)


def move(x, y, counter):
    board[x][y] = counter
    if counter == size * size:
        draw_board()
    else:
        for jump in ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)):
            tx = x + jump[0]
            ty = y + jump[1]
            if 0 <= tx < size and 0 <= ty < size and board[tx][ty] == 0:
                move(tx, ty, counter + 1)
        board[x][y] = 0


def draw_board():
    for line in board:
        print(line)


move(0, 0, 1)
