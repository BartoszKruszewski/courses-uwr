def krzyzyk(n):
    for i in range(n):
        print(" " * n + "*" * n)
    for i in range(n):
        print("*" * n * 3)
    for i in range(n):
        print(" " * n + "*" * n)

krzyzyk(5)