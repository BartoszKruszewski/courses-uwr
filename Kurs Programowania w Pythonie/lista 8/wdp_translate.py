import random
from collections import defaultdict as dd

pol_ang = dd(lambda:[])

for x in open('pol_ang.txt',"r",encoding="UTF-8"):
    x = x.strip()
    L = x.split('=')
    if len(L) != 2:
        continue    
    pol, ang = L
    pol_ang[pol].append(ang)

czestotliwosc_slow = {}
l = 0
for x in open('brown.txt',"r",encoding="UTF-8"):
    l += 1
    for i in x.strip().split(" "):
        if i not in czestotliwosc_slow:
            czestotliwosc_slow[i] = 1
        else:
            czestotliwosc_slow[i] += 1
def tlumacz(polskie):
    wynik = []
    for s in polskie:
        if s in pol_ang:
            najlepsze_tlumaczenie = []
            m = 0
            for x in pol_ang[s]:
                if x in czestotliwosc_slow:
                    if czestotliwosc_slow[x] > m:
                        najlepsze_tlumaczenie = [x]
                        m = czestotliwosc_slow[x]
                    elif czestotliwosc_slow[x] == m:
                        najlepsze_tlumaczenie.append(x)
            wynik.append(random.choice(najlepsze_tlumaczenie))
        else:
            wynik.append('[?]')
    return ' '.join(wynik)
    
zdanie = 'chłopiec z dziewczyna pójść do kino'.split()

print (tlumacz(zdanie))
            
