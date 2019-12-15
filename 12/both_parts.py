import re
from itertools import combinations
from math import gcd
from functools import reduce

with open('input/12.txt') as f:
    positions = [[int(x) for x in re.sub('[^0-9,-]', '', line.strip()).split(',')] for line in f.readlines()]

velocities = [[0, 0, 0] for _ in range(4)]


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


# changes velocities based on positions
def apply_gravity(i1, i2, velocities, positions):
    for x in range(3):
        if positions[i1][x] > positions[i2][x]:
            velocities[i1][x] -= 1
            velocities[i2][x] += 1
        elif positions[i1][x] < positions[i2][x]:
            velocities[i1][x] += 1
            velocities[i2][x] -= 1


def apply_velocity(at_moon, velocities, positions):
    for x in range(3):
        positions[at_moon][x] += velocities[at_moon][x]
    return positions[:]


def run_simulation():
    for pair in combinations(range(4), 2):
        apply_gravity(pair[0], pair[1], velocities, positions)
    for i in range(4):
        apply_velocity(i, velocities, positions)


for _ in range(1000):
    run_simulation()

potentials = [sum([abs(coord) for coord in position]) for position in positions]
kinetics = [sum([abs(coord) for coord in velocity]) for velocity in velocities]
totals = [x[0] * x[1] for x in zip(potentials, kinetics)]
print(sum(totals))  # ans1

# each axis is independet, so get period of each and lcm it for part 2
periods = [0, 0, 0]
with open('input/12.txt') as f:
    positions = [[int(x) for x in re.sub('[^0-9,-]', '', line.strip()).split(',')] for line in f.readlines()]

velocities = [[0, 0, 0] for _ in range(4)]

for axis in range(3):
    states = set()
    steps = 0
    while True:
        run_simulation()
        state = []
        for j in range(len(positions)):
            state.append(positions[j][axis])
            state.append(velocities[j][axis])
        state = str(state)
        if state not in states:
            states.add(state)
        else:
            periods[axis] = steps
            break

        steps += 1

print(reduce(lcm, periods))
