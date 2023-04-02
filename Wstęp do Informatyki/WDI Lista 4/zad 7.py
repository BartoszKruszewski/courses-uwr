def ile_roznych_cyfr(n):
    ile_cyfr = [False] * 10
    while n > 0:
        ile_cyfr[n % 10] = True
        n //= 10

    licznik = 0
    for i in range(10):
        if ile_cyfr[i]:
            licznik += 1
    return licznik


print(ile_roznych_cyfr(5656563565))
