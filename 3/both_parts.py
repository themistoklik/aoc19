starting_position = (0, 0)

with open('input/1.txt') as f:
    lines = [line.strip().split(',') for line in f.readlines()]

move_to = {'R': lambda x: (x[0] + 1, x[1]), 'L': lambda x: (x[0] - 1, x[1]), 'U': lambda x: (x[0], x[1] + 1),
           'D': lambda x: (x[0], x[1] - 1)}


def manhattan_dist(pair):
    return abs(pair[0]) + abs(pair[1])


def get_path(instructions):
    steps_so_far = 0
    position = starting_position
    point_to_steps_so_far = {}

    for step in instructions:

        direction = step[0]
        number_of_steps = int(step[1:])

        for _ in range(number_of_steps):
            position = move_to[direction](position)
            steps_so_far += 1
            point_to_steps_so_far[position] = steps_so_far

    return point_to_steps_so_far


path1 = get_path(lines[0])
path2 = get_path(lines[1])

intersections = set(path1.keys()) & set(path2.keys())

ans1 = min([manhattan_dist(point) for point in intersections])
# each element is sum of steps from line 1 and line 2 till the intersection
ans2 = min([path1[point] + path2[point] for point in intersections])
print(ans1, ans2)
