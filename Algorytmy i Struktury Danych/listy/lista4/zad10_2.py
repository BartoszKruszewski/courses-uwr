def number_of_lis(arr):
    n = len(arr)

    lenghts = [1] * n
    counts = [1] * n

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                if lenghts[j] + 1 > lenghts[i]:
                    lenghts[i] = lenghts[j] + 1
                    counts[i] = counts[j]
                elif lenghts[j] + 1 == lenghts[i]:
                    counts[i] += counts[j]

    max_length = max(lenghts)
    res = 0
    for l, c in zip(lenghts, counts):
        if l == max_length:
            res += c

    return res

print(number_of_lis([1, 3, 5, 4, 7]))
