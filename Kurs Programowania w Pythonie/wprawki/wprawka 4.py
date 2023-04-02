import math

def crop(minmax,list):
    return [x for x in list if minmax[0] <= x <= minmax[1]]

def in_rectangle(p1,p2,list):
    return [x for x in list if p1[0] <= x[0] <= p2[0] and p1[1] <= x[1] <= p2[1]]

def dist(p,list):
    return [math.sqrt(pow((x[0] - p[0]),2) + pow((x[1] - p[1]),2)) for x in list]

def somesum(main_list):
    return [sum(transformed_list) for transformed_list in [list for list in main_list]]

def sortpts(p,list):
    return sorted([(x, math.sqrt(pow((x[0] - p[0]), 2) + pow((x[1] - p[1]), 2))) for x in list],key=lambda x: x[1])

print(crop([1,4],[6,4,57,5,3,4,5,5,2,3,-100]))
print(in_rectangle((2,4),(7,6),[(1,1),(1,10),(3,5),(4,6)]))
print(dist((2,2),[(4,4),(5,2),(2,5),(6,8),(100,80),(15,3)]))
print(sortpts((2,2),[(4,4),(5,2),(2,5),(6,8),(100,80),(15,3)]))




