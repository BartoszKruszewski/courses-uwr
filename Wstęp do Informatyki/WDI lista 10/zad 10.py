class ListItem:
    def __init__(self, value):
        self.val = value
        self.next = None


def add_element(L, element):
    while L.next != None:
        L = L.next
    L.next = ListItem(element)


def merge_list(L1,L2):
    first = None
    actual = None
    end_of_list = False

    while not end_of_list:
        if L1.val <= L2.val:
            if first == None:
                first = L1
            else:
                actual.next = L1
            actual = L1
            if L1.next == None:
                end_of_list = True
                actual.next = L2
            else:
                L1 = L1.next
        else:
            if first == None:
                first = L2
            else:
                actual.next = L2
            actual = L2
            if L2.next == None:
                end_of_list = True
                actual.next = L1
            else:
                L2 = L2.next

    return first

def print_list(L):
    while L.next != None:
        print(L.val, end=" ")
        L = L.next
    print(L.val)


lista1 = ListItem(1)
add_element(lista1, 11)
add_element(lista1, 18)
add_element(lista1, 23)
add_element(lista1, 57)
add_element(lista1, 98)
add_element(lista1, 101)
add_element(lista1, 203)


lista2 = ListItem(4)
add_element(lista2, 5)
add_element(lista2, 12)
add_element(lista2, 56)
add_element(lista2, 68)
add_element(lista2, 72)
add_element(lista2, 105)
add_element(lista2, 207)
add_element(lista2, 210)
add_element(lista2, 215)

print_list(lista1)
print_list(lista2)

lista = merge_list(lista1, lista2)

print_list(lista)


