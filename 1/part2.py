# read and clear input
def calculate_fuel(mass):
    return mass // 3 - 2

with open('input/1.txt') as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = int(lines[i].strip())

# apply the formula /3 -> round down -> -2
for i in range(len(lines)):
    sum_of_current = 0
    fuel = calculate_fuel(lines[i])
    while (fuel > 0):
        sum_of_current += fuel
        fuel = calculate_fuel(fuel)

    lines[i] = sum_of_current

print(sum(lines))
