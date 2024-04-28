N = 20

with open('data.csv', 'r') as f:
    data = [float(line.rstrip()) for line in f.readlines()]

avg = sum(data[:N]) / N
print((sum((avg - x) ** 2 for x in data[:N]) / N) ** 0.5)