def kolko(n,r):
    wspolrzedne = []
    srodek = n//2 + n%2
    for y in range(n):
        linia = []
        for x in range(n):
            if pow((x-srodek),2) + pow((y-srodek),2) <= pow(r,2):
                linia.append("#")
            else:
                linia.append(" ")
        if "#" in linia:
            wspolrzedne.append(linia)

    for y in range(len(wspolrzedne)):
        for x in range(n):
            print(wspolrzedne[y][x],end="")
        print()

def balwanek(n):
    for i in range(3,n + 3):
        kolko(50,i)

balwanek(3)

print()
print()
print()
print()
print()
print()

kolko(150,30)
