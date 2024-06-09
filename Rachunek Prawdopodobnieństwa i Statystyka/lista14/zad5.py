from driver import get_ss_tot, get_ss_e, get_ss_a, get_mean
from scipy.stats import f


with open('rpr-1405.csv', 'r') as file:
    lines = (line.rstrip().split(",") for line in file.readlines())

    data = {}
    for line in lines:
        if line[1] in data:
            data[line[1]].append(int(line[0]))
        else:
            data[line[1]] = [int(line[0])]

for group in data:
    print(get_mean(data[group]))

ss_tot = get_ss_tot([e for l in data.values() for e in l])
ss_e = get_ss_e(list(data.values()))
ss_a = get_ss_a(list(data.values()))
I = len(data)
J = len(list(data.values())[0])
f_stat = ss_a / ss_e * (I * J - 1) / (I - 1) 
print(ss_e)
print(ss_a)
print(ss_tot)
print(ss_e + ss_a)
print(f_stat)
print(f.cdf(f_stat, I - 1, I * J - 1))
        
