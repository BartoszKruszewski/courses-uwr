def scs(a, b): 
	m = len(a)
	n = len(b)
	dp = [[0] * (n + 1) for i in range(m + 1)] 
	
	for i in range(0, m + 1): 
		for j in range(0, n + 1): 
			if not i: 
				dp[i][j] = j; 
			elif not j: 
				dp[i][j] = i; 
			elif (a[i - 1] == b[j - 1]): 
				dp[i][j] = 1 + dp[i - 1][j - 1]; 
			else:
				dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])

	res = ""
	i = m
	j = n; 
	while (i > 0 and j > 0):
		if (a[i - 1] == b[j - 1]): 
			res = a[i - 1] + res; 
			i -= 1
			j -= 1
		elif (dp[i - 1][j] < dp[i][j - 1]):
			res = a[i - 1] + res
			i -= 1
		else:
			res = b[j - 1] + res
			j -= 1
			
	while (i > 0): 
		res = a[i - 1] + res
		i -= 1

	while (j > 0): 
		res = b[j - 1] + res
		j -= 1

	return res

if __name__ == '__main__': 
	a = "AGGTAB"
	b = "GXTXAYB"
	print(scs(a, b))
