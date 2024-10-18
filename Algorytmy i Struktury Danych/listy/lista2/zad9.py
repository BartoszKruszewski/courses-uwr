P1 = [1, 2, 6, 3, 4, 5]
P2 = [6, 4, 5, 3, 2, 1]
n = len(P1)
Q = [0] * n

def swap(i, j):
    p = P1[i]
    P1[i] = P1[j]
    P1[j] = p

for i in range(n):
    Q[P2[i] - 1] = i

# for _ in range(n):
#     r = 0 
#     for j in range(n):
#         if Q[P1[j] - 1] > j: # sprawdzanie czy P1[j] należy przesunąć w prawo
#             r = j
#         elif Q[P1[j] - 1] < j: # sprawdzanie czy P1[j] należy przesunąć w lewo
#             print(P1[r], P1[j])
#             swap(r, j)
#             r = j


#######

for i in range(n):
    l = n - 1
    r = n - 2
    while r >= i:
        if Q[P1[r] - 1] <= r:
            if Q[P1[l - 1] - 1] < l - 1:
                l = r
            r -= 1
        else:
            if Q[P1[l] - 1] < l:
                print(P1[r], P1[l])
                swap(r, l)
            else:
                r -= 1

print(P1)