import math

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def closest_pair(points):

    # wyznaczamy d dla pierwszego punktu z każdym innym
    d, closest_points = min(
        ((dist(points[0], p), (points[0], p)) for p in points[1:]),
        key=lambda x: x[0]
    )

    grid = {(0, 0): points[0]}

    for p in points[1:]:
        
        # pozycja w siatce o przedziałce d
        gx, gy = int(p[0] // d), int(p[1] // d)

        print(p, gx, gy, d)

        # petla po wszystkich sasiadach
        neighbors = ((gx + x, gy + y) for x in [-1, 0, 1] for y in [-1, 0, 1])

        for neighbor in neighbors:
            if neighbor in grid:
                dist_to_neighbor = dist(p, grid[neighbor])
                if dist_to_neighbor < d:
                    d = dist_to_neighbor
                    closest_points = (p, grid[neighbor])
        
        grid[(gx, gy)] = p
    
    return d, closest_points

points = [(100, 2), (0, 0), (1, 2), (4, 4), (1, 1)]
distance, (p1, p2) = closest_pair(points)
print(f"The closest pair is {p1} and {p2} with distance {distance}")
