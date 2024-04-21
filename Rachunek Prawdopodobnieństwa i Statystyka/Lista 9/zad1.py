N = 40

with open('data.csv', 'r') as f:
    data = [float(line.rstrip()) for line in f.readlines()]

print(sum(data[:N]) / N)