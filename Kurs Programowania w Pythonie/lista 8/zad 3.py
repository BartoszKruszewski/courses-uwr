
def policz_litery(a):
    litery = {}
    for i in a:
        if i not in litery:
            litery[i] = 1
        else:
            litery[i] += 1
    return litery

slowa = []

def wczytaj_slowa():
    for x in open('slowa.txt',"r",encoding="UTF-8"):
        litery = policz_litery(x.rstrip())
        slowa.append((litery,x.rstrip()))

def szukaj_permutacji(a):
    permutacje = []
    litery = policz_litery(a.replace(" ",""))
    for i in slowa:
        for j in slowa:
            para = {}
            para.update(i[0])
            para.update(j[0])
            if litery == para:
                permutacje.append(i + " " + j)
    return permutacje

wczytaj_slowa()
print(szukaj_permutacji("Barto"))
