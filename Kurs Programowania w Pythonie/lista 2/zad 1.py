def szachownica(n,k):
    for i in range(2 * n):
        for j in range(k):
            if i % 2 == 0:
                print(" " * k, end="")
            for p in range(2 * n):
                if p % 2 != 0:
                    print(" " * k, end="")
                else:
                    print("#" * k, end="")
            print()

szachownica(4,3)
