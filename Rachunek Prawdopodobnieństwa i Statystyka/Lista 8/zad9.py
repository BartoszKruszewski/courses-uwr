with open('z89.csv', 'r') as f:
    data = [float(line.strip()) for line in f.readlines()]

avg = sum(data) / len(data)
print((sum((avg - x) ** 2 for x in data) / len(data)) ** 0.5)