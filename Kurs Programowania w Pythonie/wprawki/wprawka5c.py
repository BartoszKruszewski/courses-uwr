przesuniecia = []
linie = []
for i in open("wprawka5b.txt"):
    if i[0] == "m":
        data = i.rstrip().split(" ")
        przesuniecia.append((int(data[1]),int(data[3]),int(data[5])))
    elif "[" in i:
        linia = []
        for index, x in enumerate(i):
            if index % 4 == 1 and x != " ":
                linia.append((x,index // 4))
        linie.append(linia)

skrzynie = []
for i in range(len(linie[-1])):
    skrzynie.append([])

for i in reversed(linie):
    for j in i:
        skrzynie[j[1]].append(j[0])

for i in przesuniecia:
    for j in range(i[0]):
        skrzynie[i[2] - 1].append(skrzynie[i[1] - 1].pop())


for i in skrzynie:
    print(i[-1], end="")

