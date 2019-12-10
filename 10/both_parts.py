from itertools import cycle
from math import atan2, degrees, pi, radians

with open('input/10.txt') as f:
    board = [line.strip() for line in f.readlines()]


def part_1(board):
    points = {}

    for y, row in enumerate(board):
        for x, char in enumerate(row):
            if char == '#':
                points[(x, y)] = {}

    for point in points.keys():
        for other_point in points.keys():
            if point == other_point: continue
            # colinear? they'll have the same angle with the axes
            slope_between_two_points = atan2(other_point[1] - point[1], other_point[0] - point[0])
            # https://gamedev.stackexchange.com/a/69678
            if slope_between_two_points < radians(-90):
                slope_between_two_points = abs(slope_between_two_points+2*pi)
            slope_between_two_points = degrees(slope_between_two_points)
            try:
                points[point][slope_between_two_points].append(other_point)
            except KeyError:
                points[point][slope_between_two_points] = [other_point]

    max_point = max(points, key=lambda x: len(
        points[x].values()))  # how many slopes you got is how many points fall in same line
    return points, max_point


points, max_point = part_1(board)
# ans1
print(len(points[max_point].values()))

# part2
evaporation = 0

for point in points.keys():
    for slope in points[point].keys():
        points[point][slope].sort(key=lambda other_point: abs(point[0] - other_point[0]) + abs(point[1] - other_point[1]))
#now each point for all its slopes "sees" the other points in order

evaporations = 0
pop = True

while pop:
    pop = False
    for slope in sorted(points[max_point].keys()):
        if points[max_point][slope]:
            evaporations += 1
            target = points[max_point][slope].pop(0) #pop gets the last one (most far out) so they need to be sorted asc
        if evaporations == 200:
            pop = True
            print(target)
            break

