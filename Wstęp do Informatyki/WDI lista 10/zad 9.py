class ListItem:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None


def add_element(L, element):
    while L.next != None:
        L = L.next
    item = ListItem(element)
    item.prev = L
    L.next = item


def pop_first_element(L):
    L.val = L.next.val
    L.prev = None
    L.next = L.next.next


def pop_last_element(L):
    while L.next != None:
        L = L.next
    L.prev.next = None
    del L


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
pop_first_element(lista)
print_list(lista)
