from scipy.stats import f

with open('rpr-1406.csv', 'r') as file:
    lines = (line.rstrip().split(",") for line in file.readlines()[1:])

    data = [[[], []], [[], []]]
    for line in lines:
        data[int(line[0]) - 1][int(line[1]) - 1].append(int(line[2]))

I = 2
J = 2
K = 5

global_mean = 0
for i in range(I):
    for j in range(J):
        for k in range(K):
            global_mean += data[i][j][k]
global_mean /= I * J * K

means_k = [[0, 0], [0, 0]]
for i in range(I):
    for j in range(J):
        means_k[i][j] = sum(data[i][j]) / K

means_i = [0, 0]
for i in range(I):
    for j in range(J):
        means_i[i] += sum(data[i][j])
    means_i[i] /= J * K

means_j = [0, 0]
for j in range(J):
    for i in range(I):
        means_j[j] += sum(data[i][j])
    means_j[j] /= I * K

ss_tot = 0
for i in range(I):
    for j in range(J):
        for k in range(K):
            ss_tot += (data[i][j][k] - global_mean) ** 2

ss_e = 0
for i in range(I):
    for j in range(J):
        for k in range(K):
            ss_e += (data[i][j][k] - means_k[i][j]) ** 2

ss_ab = 0
for i in range(I):
    for j in range(J):
        ss_ab += (means_k[i][j] - means_i[i] - means_j[j] + global_mean) ** 2
ss_ab *= K

ss_a = 0
for i in range(I):
    ss_a += (means_i[i] - global_mean) ** 2
ss_a *= J * K

ss_b = 0
for j in range(J):
    ss_b += (means_j[j] - global_mean) ** 2
ss_b *= I * K

print(global_mean)
print(means_i)
print(means_j)
print(means_k)

print(ss_tot)
print(ss_e + ss_ab + ss_a + ss_b)
print(ss_e)
print(ss_ab)
print(ss_a)
print(ss_b)


print("f::::")
print(ss_a / ss_e * 16)
print(ss_b / ss_e * 16)
print(ss_ab / ss_e * 16)

print("F::::")
print(f.cdf(ss_a / ss_e * 16, 1, 16))
print(f.cdf(ss_b / ss_e * 16, 1, 16))
print(f.cdf(ss_ab / ss_e * 16, 1, 16))