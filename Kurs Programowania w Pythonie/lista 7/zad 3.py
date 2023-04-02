f = open("lalka.txt","r",encoding="UTF-8")
data = f.readlines()
f.close()

slowa = []

for line in data:
    slowa += line.rstrip().split(" ")


l = 0
s = []
max_l = 0
max_s = []


for slowo in slowa:
    if not bool([i for i in "ąćęłńóśźż" if i in slowo]):
        l += len(slowo)
        s.append(slowo)
    else:
        if l > max_l:
            max_l = l
            print(" ".join(max_s))
            max_s = s.copy()

        l = 0
        s = []

print(max_l)
print(" ".join(max_s))