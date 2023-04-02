def bubble_sort(tab,n):
    for i in range(n):
        for j in range(1,n):
            if tab[j] < tab[j - 1]:
                p = tab[j - 1]
                tab[j - 1] = tab[j]
                tab[j] = p
    return tab

tab = [5,7,3,4,5,3,4,67,5,3,34,6,6,4,6,67,6,5,5,5]
print(bubble_sort(tab,len(tab)))