# dp[i][j] = długość LCIS stworzonego z elementów a[0..i-1] i zakończonych b[j-1]

def lcis2(a, b):
    n = len(a)
    m = len(b)
    dp = [[0] * m for _ in range(n + 1)] 

    for i in range(1, n + 1):
        lenmax = 0 # największa długość podciągu kończącego się liczbą mniejszą od a[i-1] dotychczas znalezionego w poprzednim wierszu
        for j in range(m):
            # kopiujemy wartość z poprzedniego wiersza (ona może się później zmienić na większą)
            dp[i][j] = dp[i - 1][j]
            # jeżeli liczby są takie same, to postępujemy jak wcześniej w sumie
            if a[i - 1] == b[j]:
                dp[i][j] = max(dp[i][j], lenmax + 1)
            # jeżeli spotkaliśmy mniejszą liczbę od a[i-1], być może musimy zaktualizować lenmax 
            # intuicja: dodać a[i-1] na koniec ciągu, którego długość jest przechowywana w dp[i-1][j]
            elif b[j] < a[i - 1]:
                lenmax = max(lenmax, dp[i - 1][j])

    res = []                   # stos do odtwarzania listy od tyłu
    cur_len = max(dp[n])
    j = dp[n].index(cur_len) 
    prev_val = float('inf')
    while cur_len > 0:
        if dp[n][j] == cur_len and b[j] < prev_val:
            res.append(b[j])
            prev_val = b[j]
            cur_len -= 1
        j -= 1

    return res[::-1]

print(lcis2([1, 2, 7, 10, 4, 5, 6, 9], [2, 7, 8, 4, 10, 3, 5, 6])) 