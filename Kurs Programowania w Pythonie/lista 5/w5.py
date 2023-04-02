
####################################
# Program:  najdluzsze_slowo.py
####################################

slowa_z_lalki = set(open('lalka-tom-pierwszy.txt').read().split())
litery = set('aąbcćdeęfghijklłmnńoópqrsśtuwxyzźż')

zacne_slowa = [slowo for slowo in slowa_z_lalki if set(slowo) <= litery]

K = 10

posortowane = sorted(zacne_slowa, key=len)

for w in posortowane[-K:]:
    print (w)        


####################################
# Program:  najdluzsze_slowo.py
####################################

slowa_z_lalki = set(open('lalka-tom-pierwszy.txt').read().split())
litery = set('aąbcćdeęfghijklłmnńoópqrsśtuwxyzźż')

zacne_slowa = [slowo for slowo in slowa_z_lalki if set(slowo) <= litery]

rekordowe = max(zacne_slowa, key=len)
        
print('Najdluzsze slowo to', rekordowe)



####################################
# Program:  najdluzsze_slowo.py
####################################

slowa_z_lalki = set(open('lalka-tom-pierwszy.txt').read().split())
litery = set('aąbcćdeęfghijklłmnńoópqrsśtuwxyzźż')

zacne_slowa = [slowo for slowo in slowa_z_lalki if set(slowo) <= litery]

rekordowe = ''

for w in zacne_slowa:
    if len(w) > len(rekordowe):
        print(w)
        rekordowe = w
        
print('Najdluzsze slowo to', rekordowe)



####################################
# Program:  posortuj.py
####################################

def wstaw(L, e, klucz):
    for i in range(len(L)):
        if klucz(e) < klucz(L[i]):
            return L[:i] + [e] + L[i:]
    return L + [e]        

def posortowana(L, klucz):
    wynik = []
    for e in L:
        wynik = wstaw(wynik, e, klucz)
    return wynik
        
    
def identycznosc(x):
    return x
    
        
L = [5,4,3,2,1,8,9,10,0]

print (posortowana(L, identycznosc))  

L2 = 'ala ma kota i 22 kanarki brazylijskie, które kocha bez pamięci'.split()

print (posortowana(L2, identycznosc))  
print (posortowana(L2, lambda x:x))  

print (posortowana(L2, len))  




######################################
#  rysuj_tablice.py
######################################

from turtle import *
import numpy as np
from math import sin, cos

tracer(0,1)

def move(x, y):
    pu()
    goto(x, y)
    pd()
    
def kwadrat(bok, kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(4):
        fd(bok)
        rt(90)
    end_fill()

kolor_jasny = np.array( [1,0.5,0.5] )
kolor_jasny = np.array( [1,1,0] )
    
DX = DY = 15
BOK = 20

def rysuj_tablice(sx, sy, tab):
    for y in range(DY):
        for x in range(DX):
            move(sx + x*BOK, sy + y*BOK)
            kwadrat(BOK, kolor_jasny * tab[y,x])

def generuj_sin():
    tab = np.zeros( (DY, DX) )
    for y in range(DY):
        for x in range(DX):
            tab[y, x] = sin(0.1 * x + 0.3 * y)
    minimum = tab.min()
    tab -= minimum  
    tab /= tab.max()      
    return tab
               
tab = np.random.rand(DY,DX)


tab[:,3] = 0.1
tab[3,:] = 1

rysuj_tablice(-300, -100, tab)
rysuj_tablice(100, -100, 0.7 * tab)
rysuj_tablice(-300, 300, generuj_sin())

input() 




######################################
#  rysuj_wykresy.py
######################################

from turtle import *
import numpy as np
from math import sin, cos

tracer(0,1)

def move(x, y):
    pu()
    goto(x, y)
    pd()
    
def kwadrat(bok, kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(4):
        fd(bok)
        rt(90)
    end_fill()

kolor_jasny = np.array( [1,1,0.5] )
    
DX = DY = 15
BOK = 20

def rysuj_tablice(sx, sy, tab):
    for y in range(DY):
        for x in range(DX):
            move(sx + x*BOK, sy + y*BOK)
            kwadrat(BOK, kolor_jasny * tab[y,x])

def rysuj_wykres(sx, sy, f):
    tab = np.zeros( (DY, DX) )
    for y in range(DY):
        for x in range(DX):
            tab[y, x] = f(x, y)
    minimum = tab.min()
    tab -= minimum  
    tab /= tab.max()
    rysuj_tablice(sx, sy, tab)      


f1 = lambda x, y: x + 2*y
f2 = lambda x, y: x**2 + y**2
f3 = lambda x, y: (x-DX/2)**2 + (y-DY/2) ** 2
f4 = lambda x, y: sin(0.3*x) + cos(0.7*y)
f5 = lambda x, y: x + sin(0.3*x) + cos(0.7*y)
f6 = lambda x, y: 10 if (x+y) % 2 == 0 else x+y

lista_f = [f1,f2,f3,f4,f5,f6]
for i in range(len(lista_f)):
    sx = -400 + 310 * (i % 3)
    sy = -200 + 310 * (i // 3)
    rysuj_wykres(sx, sy, lista_f[i])
    
input()    
    
