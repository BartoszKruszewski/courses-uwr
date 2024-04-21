# Oznaczmy x punktów przecięcia pi z l' jako ai oraz pi z l'' jako bi
# Zauważmy, że odcinki aibi oraz ajbj przecinają się kiedy:
# ai < aj && bi > bj
# Posortujmy odcinki względem a.
# Wtedy warunek ai < aj jest zawsze spełniony,
# więc wystarczy sprawdzić bi > bj.
# Stąd podzbiory nieprzecinających się odcinków to:
# Dowolny zbiór odcinków, które po posortowaniu po a zachowują bi > bj.
# Chcemy uzyskać taki zbiór o maksymalnej mocy.
# Czyli szukamy najdłuższy rosnący podzbiór b. (LIS(b))

# Algorym:
# 1. Wyliczenie punktów przecięcia
# 2. Utworzenie tablicy par <ai, bi>
# 3. Sortowanie tablicy po a
# 4. Znalezenie LIS z elementów b z tablicy 

def lis(arr):
    n = len(arr)
    dp = [1] * n # lis dla arr[:i]

    for i in range(1, n):
        for j in range(i):
            # wydłużamy dp[j] o arr[i], jeżeli się opłaca
            if (arr[i] > arr[j] and dp[i] < dp[j] + 1):
                dp[i] = dp[j] + 1  

    # odzyskiwanie
    path = []
    cur_len = max(dp)
    j = dp.index(cur_len) 
    prev_val = float('inf')
    while cur_len > 0:
        if dp[j] == cur_len and arr[j] < prev_val:
            path.append(arr[j])
            prev_val = arr[j]
            cur_len -= 1
        j -= 1
    return path[::-1]

print(lis([1, 2, 3, 4, 5, 10, 7, 5, 11]))

# Złożoność O(n^2)

# Dla podpunktu b) musi zliczyć wszystkie rosnące podciągi ciągu b
# dp[i] = ilosc podciagow dla arr[:i]
# jeżeli element poprzedzający i jest mniejszy od 
# to możemy do dp[i] dodać wszystkie jego podciągi 
# (podciągi z dp[j] z dodanym arr[i] na końcu)

def count(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] += dp[j]
    return sum(dp)

print(count([1, 2, 3, 4]))

# Złożoność O(n^2)