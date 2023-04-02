from struct import get_graph
from struct import ListItem
from struct import list_to_string

graph = get_graph([
    [1],
    [2],
    [3],
    [4],
    [],
])



def find_path(G, U, V):
    def find_path_r(u):
        if u == V:
            return ListItem(V)
        L = G[u]
        while L != None:
            p = ListItem(L.val)
            p.next = find_path_r(L.val)
            return p
            L = L.next
        return False
    return find_path_r(U)

print(list_to_string(find_path(graph, 0, 4)))
