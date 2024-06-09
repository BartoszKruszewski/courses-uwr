from math import sqrt

def get_data(file_name):

    with open(file_name, 'r') as f:
        data = [line.rstrip().split(",") for line in f.readlines()]

    data_x = [float(line[0]) for line in data]
    data_y = [float(line[1]) for line in data]

    return data_x, data_y

def get_mean(data):
    return sum(data) / len(data)

def get_z(data_x, data_y, vx2, vy2):
    return (get_mean(data_x) - get_mean(data_y)) / sqrt(vx2 / len(data_x) + vy2 / len(data_y))

def get_t(data_x, data_y, vx2, vy2):
    return (get_mean(data_x) - get_mean(data_y)) / sqrt(vx2 / len(data_x) + vy2 / len(data_y))

def get_s2(data):
    mean = get_mean(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

def get_ss_tot(data):
    mean = get_mean(data)
    return sum((x - mean) ** 2 for x in data)

def get_ss_a(data):
    global_mean = get_mean([e for l in data for e in l])
    return sum((get_mean(group) - global_mean) ** 2 for group in data) * len(data[0])

def get_ss_b(data):
    global_mean = get_mean([e for l in data for e in l])
    I = len(data)
    J = len(data[0])

    data_t = [[0] * I for _ in range(J)]
    for i in range(I):
        for j in range(J):
            data_t[j][i] = data[i][j]
    print(data_t)
    return 

def get_ss_e(data):
    s = 0
    for group in data:
        mean = get_mean(group)
        s += sum((x - mean) ** 2 for x in group)
    return s

def get_sp2(data_x, data_y):
    nx = len(data_x)
    ny = len(data_y)
    return ((nx - 1) * get_s2(data_x) + (ny - 1) * get_s2(data_y)) / (nx + ny - 2)

def get_t(data_x, data_y):
    return (get_mean(data_x) - get_mean(data_y)) / sqrt(get_sp2(data_x, data_y) * (1 / len(data_x) + 1 / len(data_y)))

def get_r(data_x, data_y):
    sx2 = get_s2(data_x)
    sy2 = get_s2(data_y)
    nx = len(data_x)
    ny = len(data_y)
    return (sx2 / nx + sy2 / ny) ** 2 / ((sx2 / nx) ** 2 * (nx - 1) / nx ** 2 + (sy2 / ny) ** 2 * (ny - 1) / ny ** 2)

def get_w(data_x, data_y):
    sx2 = get_s2(data_x)
    sy2 = get_s2(data_y)
    nx = len(data_x)
    ny = len(data_y)
    return (get_mean(data_x) - get_mean(data_y)) / sqrt(sx2 / nx + sy2 / ny)

def get_confidence_interval(za, v, data):
    mean = get_mean(data)
    n = len(data)
    return mean - za * v / sqrt(n), mean + za * v / sqrt(n)