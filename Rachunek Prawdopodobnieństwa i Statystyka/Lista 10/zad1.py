N = 20

with open('data.csv', 'r') as f:
    data = [float(line.rstrip()) for line in f.readlines()]

print(sum(data) / len(data))