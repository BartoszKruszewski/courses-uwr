arr = [1, 1, 4, 2, 3]
N = len(arr)
dp = {} 

# dp[(sm1, sm2)] = czy da się podzielić, 
# jeżeli dwa pierwsze zbiory sumują się do sm1 i sm2

# j = od którego indeksu tablicy rozważamy zbiór

def rec(sm1, sm2, sm3, j):
    if j == N:
        return sm1 == sm2 == sm3
    
    if (sm1, sm2) in dp: return dp[(sm1, sm2)]
    if (sm2, sm1) in dp: return dp[(sm2, sm1)]

    dp[(sm1, sm2)] = max(
	    rec(sm1 + arr[j], sm2, sm3, j + 1),
	    rec(sm1, sm2 + arr[j], sm3, j + 1),
	    rec(sm1, sm2, sm3 + arr[j], j + 1),
	)
	
    return dp[(sm1, sm2)]

print(rec(0, 0, 0, 0))
print(dp)

# złożoność O(NK^2), ponieważ dla każdego elementu tablicy
# spradzamy wszystkie możliwości sumowania dla sm1 i sm2