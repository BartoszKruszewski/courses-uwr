# Pamiętamy jedną kolumną oraz dwie wartości (po lewej oraz po przekątnej).
# W momencie aktualizowania kolumny, wartości które mają zostać nadpisane 
# przenosimy do zmiennych dp[i] -> next -> diagonal.

# Odtwarzanie robimy na podstawie dp, które otrzymamy na końcu. 
# Wystraczy, ze sprawdzimy dla jakich indeksow, dlugosc lcs 
# zostala zwiekszona i otrzymamy nasz podciag. Działa to poniewaz cofając się
# od dp[m] do wartosci wiekszych trafimy na lcs, a w dp po zakonceniu algorytmu
# są wieksze wartosci, inaczjej nie bylyby max i nie zostałyby wzięte.

def lcs(x, y): 
	n = len(x) 
	m = len(y) 

	dp = [0] * (m + 1)
	diagonal = 0
	next = 0
	res = ""

	for i in range(1, n + 1):
		next = 0
		for j in range(1, m + 1):
			diagonal = next
			next = dp[j]
			if x[i - 1] == y[j - 1]:
				dp[j] = diagonal + 1
			else:
				if dp[j - 1] > next:
					dp[j] = dp[j - 1]
				else:
					dp[j] = next

	for j in range(1, m + 1):
		if dp[j - 1] != dp[j]:
			res += y[j - 1]
	return res

print(lcs("AGGTAB", "GXTXAYB")) 
