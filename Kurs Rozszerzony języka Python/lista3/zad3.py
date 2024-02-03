from collections import deque
from random import random, randint

# .=======================.
# ===== MAIN FUNCTION =====
# '======================='

def find_path(maze, start):
    if not maze or not maze[0]:
        return []

    def is_valid_move(x, y):
        return 0 <= x < len(maze[0]) and 0 <= y < len(maze) and maze[y][x] != "X"

    def neighbors(x, y):
        possible_moves = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        return [(nx, ny) for nx, ny in possible_moves if is_valid_move(nx, ny)]

    queue = deque([(start, [start])])
    visited = set()

    while queue:
        (x, y), path = queue.popleft()
        if maze[y][x] == "E":
            return path

        elif (x, y) not in visited:
            visited.add((x, y))

            for neighbor in neighbors(x, y):
                queue.append((neighbor, path + [neighbor]))

    return []

# .=====================.
# ===== RANDOM MAZE =====
# '====================='

def generate_random_maze():
    ROWS = 10
    COLS = 20
    OBSTACLE_PROB = 0.3
    
    maze = [[" " for _ in range(ROWS)] for _ in range(COLS)]
    for y in range(COLS):
        for x in range(ROWS):
            if random() < OBSTACLE_PROB:
                maze[y][x] = "X"

    start = (randint(0, ROWS - 1), randint(0, COLS - 1))
    end = (randint(0, ROWS - 1), randint(0, COLS - 1))
    while end == start:
        end = (randint(0, ROWS - 1), randint(0, COLS - 1))

    maze[start[1]][start[0]] = "S"
    maze[end[1]][end[0]] = "E"
    return maze

# .========================.
# ===== HELP FUNCTIONS =====
# '========================'

def print_maze(maze):
    for row in maze:
        print("".join(row))

def get_start_point(maze):
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == 'S':
                return x, y 
            
def get_end_point(maze):
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == 'E':
                return x, y 


# .===============.
# ===== TESTS =====
# '==============='

def single_test(maze = None):
    FULL_INFO = False

    if maze is None:
        maze = generate_random_maze()

    path = find_path(maze, get_start_point(maze))

    if FULL_INFO:
        print_maze(maze)
        print(path)
    
    return not path or get_end_point(maze) == path[-1]

def test():
    TESTS = 100

    all = 0
    correct = 0
    for _ in range(TESTS):
        all += 1
        if single_test():
            correct += 1

    print(str(int(round(correct / all, 2) * 100)) + '%')

example_maze = [
    ["X", "X", "X", "X", "X", "X", "X", "X"],
    ["X", "S", " ", " ", "X", " ", " ", "X"],
    ["X", " ", "X", " ", "X", " ", "X", "X"],
    ["X", " ", "X", " ", "X", " ", " ", "X"],
    ["X", " ", "X", "X", "X", "X", "X", "X"],
    ["X", " ", " ", " ", " ", " ", " ", " "],
    ["X", "X", "X", "X", "X", "X", "X", "E"]
]

print('Example test:')
print_maze(example_maze)
single_test(example_maze)
print(find_path(example_maze, get_start_point(example_maze)))

test()

