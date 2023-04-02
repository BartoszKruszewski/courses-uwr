class ListItem:
    def __init__(self, value):
        self.val = value
        self.next = None


def add_element(L, element):
    while L.next != None:
        L = L.next
    L.next = ListItem(element)


def pop_element(L):
    previous = None
    while L.next != None:
        previous = L
        L = L.next
    del L
    previous.next = None

def remove_elements(L, n):
    previous = None
    while L.next != None:
        previous = L
        L = L.next
        if L.val == n:
            previous.next = L.next


def extend(L1, L2):
    while L1.next != None:
        L1 = L1.next
    L1.next = L2


def print_list(L):
    while L.next != None:
        print(L.val, end=" ")
        L = L.next
    print(L.val)


lista1 = ListItem(5)
add_element(lista1, 6)
add_element(lista1, 7)
add_element(lista1, 6)
add_element(lista1, 10)
add_element(lista1, 6)
add_element(lista1, 8)
add_element(lista1, 10)
pop_element(lista1)
pop_element(lista1)
add_element(lista1, 10)
print_list(lista1)
lista2 = ListItem(100)
add_element(lista2, 101)
add_element(lista2, 102)
print_list(lista2)
extend(lista1, lista2)

print_list(lista1)
remove_elements(lista1, 6)
print_list(lista1)