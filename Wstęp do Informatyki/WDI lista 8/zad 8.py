def hanoi(src, dst, n):
    helper = 6 - (src + dst)
    if n == 1:
        print(src, dst)
    else:
        hanoi(src, helper, n - 1)
        hanoi(src, dst, 1)
        hanoi(helper, dst, n - 1)


hanoi(1, 3, 6)