with open('z89.csv', 'r') as f:
    data = [float(line.strip()) for line in f.readlines()]

print(sum(data) / len(data))