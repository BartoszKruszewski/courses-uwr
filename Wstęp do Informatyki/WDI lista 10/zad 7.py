class ListItem:
    def __init__(self, value):
        self.val = value
        self.next = None

def add_element(L, element):
    while L.next != None:
        L = L.next
    L.next = ListItem(element)

def reverse_list(L):
    def reverse_part(a, n):
        first = a
        for i in range(n-1):
            a = a.next
        last = a
        first.val, last.val = last.val, first.val
    f = L
    l = 1
    while L.next != None:
        L = L.next
        l += 1
    for i in range(0,l,2):
        reverse_part(f, l - i)
        f = f.next

def print_list(L):
    while L.next != None:
        print(L.val, end=" ")
        L = L.next
    print(L.val)

lista = ListItem(1)
add_element(lista, 2)
add_element(lista, 3)
add_element(lista, 4)
add_element(lista, 5)
add_element(lista, 6)
add_element(lista, 7)
add_element(lista, 8)

reverse_list(lista)
print_list(lista)