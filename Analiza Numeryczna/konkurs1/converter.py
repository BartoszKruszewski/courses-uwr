'''
Program converts points.txt from main.py
to txt data desribed in exercise 8.7
'''

PATH = 'points.txt'

xs = []
ys = []
ts = []
us = []

with open(PATH, 'r') as file:
    data = (line.rstrip() for line in file.readlines())

xs_group = []
ys_group = []

for line in data:
    if line == ';':
        xs.append(xs_group)
        ys.append(ys_group)
        ts.append([k / len(xs_group) for k in range(len(xs_group))])
        us.append([k / 1000 for k in range(1000)])
        xs_group = []
        ys_group = []
    else:
        cords = line.split(',')
        xs_group.append(cords[0])
        ys_group.append(cords[1])

def save(path, list):
    with open(path, 'w') as file:
        for group in list:
            for value in group:
                file.write(f'{value}\n')
            file.write('\n')

save('x.txt', xs)
save('y.txt', ys)
save('t.txt', ts)
save('u.txt', us)
                