from math import pi
 
def find_farthest_orbit(orbits):
    return max([orbit for orbit in orbits if orbit[0] != orbit[1]], key=lambda x: pi * x[0] * x[1]) 
 
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

print(*find_farthest_orbit(orbits))
