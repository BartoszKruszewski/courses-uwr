def usun_w_nawiasach(text):
    nowy_text = ""
    p = False
    for i in text:
        if p:
            if i == ")":
                p = False
        else:
            if i == "(":
                p = True
            else:
                nowy_text += i
    return nowy_text

print(usun_w_nawiasach("Ala ma kota (perskiego ( bo takie lubi najbardziej) z Arabii Saudyjskiej)!"))

