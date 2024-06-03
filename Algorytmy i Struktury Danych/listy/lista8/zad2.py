import math

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def closest_pair(points):

    # wyznaczamy d dla pierwszego punktu z każdym innym
    d, closest_points = min(
        ((dist(points[0], p), (points[0], p)) for p in points[1:]),
        key=lambda x: x[0]
    )

    # tworzymy siatkę i dodajemy punkty
    # jeżeli punkty są w tej samej kratce to są w jednej liście    
    grid = {}

    for p in points:
        gx, gy = int(p[0] // d), int(p[1] // d)
        if (gx, gy) not in grid:
            grid[(gx, gy)] = [p]
        else:
            grid[(gx, gy)].append(p)


    for p in points[1:]:
        
        # pozycja w siatce o przedziałce d
        gx, gy = int(p[0] // d), int(p[1] // d)

        # petla po wszystkich sasiadach
        neighbor_cords = ((gx + x, gy + y) for x in [-1, 0, 1] for y in [-1, 0, 1])

        for cords in neighbor_cords:
            if cords in grid:
                for neighbor in grid[cords]:
                    if neighbor != p:
                        dist_to_neighbor = dist(p, neighbor)
                        if dist_to_neighbor < d:
                            d = dist_to_neighbor
                            closest_points = (p, neighbor)
    
        if (gx, gy) not in grid:
            grid[(gx, gy)] = [p]
        else:
            grid[(gx, gy)].append(p)
    
    return d, closest_points

points = [(1, 1), (100, 2), (4, 4), (84, 5) , (13, 3), (15, 5), (5, 2), (8, 4)]
distance, (p1, p2) = closest_pair(points)
print(f"The closest pair is {p1} and {p2} with distance {distance}")

# złożoność:
# Zakładając, że punkty są równomiernie rozłożone,
# możemy ograniczyć max wielkośc listy stała a.
# Wtedy w każdym kroku wykonujemy O(1 * 8 * a) porownań.
# czyli złożoność to n * O(a) = O(an), gdzie oczekiwana wartość a to stała. 
