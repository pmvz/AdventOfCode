import numpy as np
from numba import njit
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


# Part 1
points = np.loadtxt("Day 9/input", delimiter=',', dtype=np.int64)
diffs = np.abs(points[np.newaxis,:,:] - points[:,np.newaxis,:])
diffs += 1  # include endpoints
areas = np.prod(diffs, axis=-1)
print(areas.max())


# Part 2
# Testing revealed that lines are defined by sequential points in the array, so no need for sorting/searching
polygon = Polygon(points)

# Takes a bit more than a minute, numba parallelization will probably help
max_area = 0
for i, row in enumerate(areas):
    print(f"{i+1}/{areas.shape[0]}")
    for j, area in enumerate(row):
        # Only consider areas in the upper triangle, except the
        # main diagonal (1x1 areas) and the next one (1xn, nx1 areas)
        if i > j-2:
            continue

        # Find rectangle points, check if all points are on/in the polygon 
        p1 = Point(points[i])  # Part of polygon border
        p3 = Point(points[j])  # Part of polygon border
        rectangle = Polygon([p1, Point(p1.x, p3.y), p3, Point(p3.x, p1.y)])

        if polygon.covers(rectangle) and area > max_area:
            max_area = area

print(max_area)
