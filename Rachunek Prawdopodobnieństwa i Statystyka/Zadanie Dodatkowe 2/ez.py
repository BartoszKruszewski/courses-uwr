with open('data.txt', 'r') as f:
    data = [line.rstrip().replace(" ", "").split("\t") for line in f.readlines()]

with open('weights.txt', 'w') as f:
    [f.write(f'{line[1]}\n') for line in data]

with open('nodes.txt', 'w') as f:
    [f.write(f'{line[2]}\n') for line in data]