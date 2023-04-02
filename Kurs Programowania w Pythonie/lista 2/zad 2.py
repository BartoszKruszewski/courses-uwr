def koperta(n):
    x = 2 * n + 1
    print("*" * x)

    for i in range(n - 1):
        print("*" + " " * i + "*" + " " * ((n - i) * 2 - 3) + "*" + " " * i + "*")

    print("*" + " " * (n-1) + "*" + " " * (n-1) + "*")

    for i in range(n - 2,-1,-1):
        print("*" + " " * i + "*" + " " * ((n - i) * 2 - 3) + "*" + " " * i + "*")

    print("*" * x)

koperta(4)