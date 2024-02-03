pi = 0
actual_element = 1
k = 0
while abs(actual_element) > 0.000001:
    actual_element = 4 * (1 if k % 2 == 0 else -1) / (2 * k + 1)
    pi += actual_element
    k += 1
print("pi:", pi)
print("k:", k)
    
    