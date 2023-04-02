def podziel(s):
    tab = []
    slowo = ""
    for i in s:
        if i != " ":
            slowo += i
        else:
            if slowo != "":
                tab.append(slowo)
                slowo = ""
    if slowo != "":
        tab.append(slowo)
    return tab

print(podziel("Ala   ma   kota"))