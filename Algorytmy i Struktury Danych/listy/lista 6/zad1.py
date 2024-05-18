from random import randint

def partition(arr, p, r):
    x = arr[p]
    i = p
    j = r
    while i < j:
        while arr[j] > x:
            j -= 1
        while arr[i] < x: 
            i += 1 
        if i < j:
            swap(arr, i, j)
        else:
            return j

def swap(arr, i, j):
    p = arr[j]
    arr[j] = arr[i]
    arr[i] = p

def choosepivot(arr, p, r):
    swap(arr, p, randint(p, r))

def quicksort(arr, p, r):
    n = r - p
    while n > 0:
        choosepivot(arr, p, r)
        q = partition(arr, p, r)
        
    if r - p > 1:
        
        
        quicksort(arr, p, q)
        quicksort(arr, q + 1, r)
        
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
quicksort(arr, 0, len(arr) - 1)
print(arr)