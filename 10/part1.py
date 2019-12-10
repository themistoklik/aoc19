with open('input/10.txt') as f:
    board = [line.strip() for line in f.readlines()]

from math import atan2


def part_1(board):
    points = {}

    for x, row in enumerate(board):
        for y, char in enumerate(row):
            if char == '#':
                points[(x, y)] = {}

    for point in points.keys():
        for other_point in points.keys():
            if point == other_point: continue
            # colinear? they'll have the same angle with the axes
            slope_between_two_points = atan2(other_point[1] - point[1], other_point[0] - point[0])
            slope_between_two_points = int(slope_between_two_points * 1000000)
            try:
                points[point][slope_between_two_points].append(other_point)
            except KeyError:
                points[point][slope_between_two_points] = []

    max_point = max(points, key=lambda x: len(points[x].values()))

    return len(points[max_point].values())


ans1 = part_1(board)
print(ans1)
