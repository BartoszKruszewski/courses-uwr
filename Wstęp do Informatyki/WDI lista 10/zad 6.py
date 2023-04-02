class ListItem:
    def __init__(self, value):
        self.val = value
        self.next = None

def add_element(L, element):
    while L.next != None:
        L = L.next
    L.next = ListItem(element)

def print_list_reversed(L):
    if L.next != None:
        print_list_reversed(L.next)
    print(L.val, end=" ")

lista = ListItem(1)
add_element(lista, 2)
add_element(lista, 3)
add_element(lista, 4)
add_element(lista, 5)
add_element(lista, 6)
add_element(lista, 7)
add_element(lista, 8)

print_list_reversed(lista)