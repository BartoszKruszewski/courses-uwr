class ListItem:
    def __init__(self, value):
        self.val = value
        self.next = None


def add_element(L, element):
    while L.next != None:
        L = L.next
    L.next = ListItem(element)


def split_list(L):
    first_positive = None
    first_negative = None
    positive = None
    negative = None

    while L.next != None:
        if L.val >= 0:
            if positive == None:
                first_positive = L
            else:
                positive.next = L
            positive = L
        else:
            if negative == None:
                first_negative = L
            else:
                negative.next = L
            negative = L
        L = L.next

    negative.next = None
    positive.next = None

    return first_positive, first_negative


def print_list(L):
    while L.next != None:
        print(L.val, end=" ")
        L = L.next
    print(L.val)


lista = ListItem(1)
add_element(lista, -2)
add_element(lista, 3)
add_element(lista, 4)
add_element(lista, -5)
add_element(lista, -6)
add_element(lista, 7)
add_element(lista, 8)

lista1, lista2 = split_list(lista)

print_list(lista1)
print_list(lista2)
