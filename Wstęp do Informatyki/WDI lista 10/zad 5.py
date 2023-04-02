class ListItem:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.last = self # tylko pierwszy przechowuje

def add_first_element(L, element):
    item = ListItem(L.val)
    L.val = element
    item.next = L.next
    L.next = item

def pop_first_element(L):
    L.val = L.next.val
    L.next = L.next.next

def add_last_element(L, element):
    item = ListItem(element)
    L.last.next = item
    L.last = item

def extend(L1,L2):
    last = L2.last
    L2.last = None
    L1.last.next = L2
    L1.last = last

def print_list(L):
    while L.next != None:
        print(L.val, end=" ")
        L = L.next
    print(L.val)

lista1 = ListItem(5)
add_last_element(lista1, 6)
add_last_element(lista1, 7)
print_list(lista1)

add_first_element(lista1, 6)
add_first_element(lista1, 10)
print_list(lista1)

pop_first_element(lista1)
print_list(lista1)


lista2 = ListItem(100)
add_last_element(lista2, 101)
add_last_element(lista2, 102)
print_list(lista2)
extend(lista1, lista2)
print_list(lista1)