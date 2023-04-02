class ListItem:
    def __init__(self, value):
        self.val = value
        self.next = None


class LinkedList:
    def __init__(self, *values):
        self.head = None
        self.len = 0
        for value in values:
            self.add(value)

    def add(self, value):
        self.len += 1
        if self.head is None:
            self.head = ListItem(value)
        else:
            last_element = self.head
            while last_element.next is not None:
                last_element = last_element.next
            last_element.next = ListItem(value)

    def remove_index(self, index):
        if index == 0:
            self.head = self.head.next
        elif index >= self.len:
            raise Exception("list index out of range")
        else:
            actual_element_index = 0
            actual_element = self.head
            while index - 1 > actual_element_index:
                actual_element = actual_element.next
                actual_element_index += 1
            actual_element.next = actual_element.next.next

    def pop(self):
        self.remove_index(self.len - 1)

    def __getitem__(self, item):
        if item == 0:
            return self.head.val
        elif item >= self.len:
            raise Exception("list index out of range")
        else:
            actual_element_index = 0
            actual_element = self.head
            while item > actual_element_index:
                actual_element = actual_element.next
                actual_element_index += 1
            return actual_element.val

    def __setitem__(self, key, value):
        if key == 0:
            self.head.val = value
        elif key >= self.len:
            raise Exception("list index out of range")
        else:
            actual_element_index = 0
            actual_element = self.head
            while key > actual_element_index:
                actual_element = actual_element.next
                actual_element_index += 1
            actual_element.val = value

    def __len__(self):
        return self.len

    def __repr__(self):
        if self.len == 0:
            return "[]"
        s = "["
        actual_element = self.head
        while actual_element.next is not None:
            s += str(actual_element.val) + ", "
            actual_element = actual_element.next
        s += str(actual_element.val) + "]"
        return s


def get_graph(D):
    G = []
    for targets in D:
        if len(targets) == 0:
            G.append(None)
        else:
            first = ListItem(targets[0])
            L = first
            for t in targets[1:]:
                L.next = ListItem(t)
                L = L.next
            G.append(first)
    return G

def list_to_string(L):
    if L is None:
        return []
    s = "["
    actual_element = L
    while actual_element.next is not None:
        s += str(actual_element.val) + ", "
        actual_element = actual_element.next
    s += str(actual_element.val) + "]"
    return s