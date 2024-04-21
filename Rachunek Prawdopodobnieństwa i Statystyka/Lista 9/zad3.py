from cdf import cdf

u = 0
while cdf(0, 1, u) < 0.9:
    u += 0.01

print(u)
    