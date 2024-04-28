# zwykly bin search, ponieważ
# elementy w arr[min_id] są rosnące
def bin_r(arr, T, l, r, key):
	while r - l > 1:
		m = l + (r - l)//2
		if arr[T[m]] >= key: r = m
		else: l = m
	return r

def lis(arr):
    n = len(arr)
	
    # indeksy najmniejszego elementu który kończy lis o długości (i + 1)
    min_id = [0] * (n + 1)

    # tablica do odtwarzania 
    # (indeksy poprzedniego elementu rozwiazania w arr)
    prev = [-1] * (n + 1)
	
    # aktualna długość rozwiązania
    l = 1

    for i in range(1, n):
        # ustawiamy min_id[0] na min z arr
        if arr[i] <= arr[min_id[0]]:
            min_id[0] = i

        # dokładamy arr[i] jeżeli to możliwe
        elif arr[i] > arr[min_id[l - 1]]:
            prev[i] = min_id[l - 1]
            min_id[l] = i
            l += 1

        # znajdowanie pozycji najmniejszego elementu wiekszego od arr[i] w min_id
        # i dodanie go do rozwiazania na wyliczona pozycje
        else:
            pos = bin_r(arr, min_id, -1, l - 1, arr[i])
            prev[i] = min_id[pos - 1]
            min_id[pos] = i
        print(min_id)
	
    # odtwarzanie od konca
    i = min_id[l - 1]
    while i >= 0:
        print(arr[i], " ", end ="")
        i = prev[i]

lis([2, 5, 4, 3, 7, 8])

# Dowód:
# Iteracja zachowuje właściwości min_id i prev.
# 1. arr[i] <= arr[min_id[0]]
#   Zauważmy, że arr[min_id[0]] to po prostu minimum ciągu.
#   Więc aktualizujemy je jak standardowe minimum.
# 2. arr[i] > arr[min_id[l - 1]]
#   Zauważmy, że wtedy arr[i] jest większe niż ostatni element,
#   naszego aktualnie najdłuższego podciągu,
#   więc możemy go dodać na koniec podciągu.      
# 3. binsearch
#   Znaleziony przez binsearch element jest 
#   najmniejszym większym lub równym elementem od a.
#   Czyli jeszcze mniejszy element jest mniejszy od a,
#   Czyli po zamianie ciąg jest dalej rosnący.
#   Jeżeli w poprzedniej iteracji min_id było prawidłowe,
#   to jedyna zmiana jaką zrobiliśmy dalej je zachowuje.
# 
# Jeżeli iteracje poprawnie zachowują właściwości min_id prev to
# wypisując wyniki otrzymamy optymalne rozwiązanie.
