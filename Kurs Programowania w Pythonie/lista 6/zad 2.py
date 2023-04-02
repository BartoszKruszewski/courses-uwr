file = open("popularne_slowa.txt","r", encoding="utf-8")
data = set(file.readlines())
file.close()

wypisane = set()

for slowo in data:
    if slowo not in wypisane:
        odwrocone = "".join(reversed(slowo.rstrip()))
        if odwrocone + "\n" in data:
            wypisane.add(odwrocone + "\n")
            print(slowo.rstrip() + "-" + odwrocone)

print("skonczone")