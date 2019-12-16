from collections import Counter, deque
from math import ceil

with open('input/14.txt') as f:
    materials = {}
    material_amount = {}
    for reaction in [line.strip() for line in f.readlines()]:
        requirements, product = reaction.split('=>')
        product_amount, product_type = product.strip().split(' ')
        requirements = [(int(requirement.strip().split(' ')[0]), requirement.strip().split(' ')[1]) for requirement in
                        requirements.split(',')]
        materials[product_type] = requirements
        material_amount[product_type] = int(product_amount)

dependencies = Counter(
    [mat for m in materials for amount, mat in materials[m]])  # how many times has it got to be processed


def ores_for_fuel_amount(amount):
    deps = dependencies.copy()  # need that for part 2 otherwise deps get reused and corrupted
    bucket = {'FUEL': amount}
    done = deque(['FUEL'])
    while deps['ORE']:
        mat = done.pop()
        amount = ceil(bucket[mat] / material_amount[mat])
        for a, m in materials[mat]:
            try:
                bucket[m] += a * amount
            except KeyError:
                bucket[m] = a * amount
            deps[m] -= 1
            if not deps[m]:
                done.append(m)
    return bucket['ORE']


print(ores_for_fuel_amount(1))  # ans1

# part2
lo = 1
hi = 10 ** 12

while lo < hi:
    fuel = lo + (hi - lo) // 2
    ores = ores_for_fuel_amount(fuel)
    if ores > 10 ** 12:
        hi = fuel - 1
    elif ores == 10 ** 12:
        print("EXACT")
        print(ores)  # are we lucky?
        break
    else:
        lo = fuel

print(lo)  # best approx

graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['d'],
    'd': ['e'],
    'e': []
}

def iterative_topological_sort(graph, start):
    seen = set()
    stack = []    # path variable is gone, stack and order are new
    order = []    # order will be in reverse order at first
    q = [start]
    while q:
        v = q.pop()
        if v not in seen:
            seen.add(v) # no need to append to path any more
            q.extend(graph[v])

            while stack and v not in graph[stack[-1]]: # new stuff here!
                order.append(stack.pop())
            stack.append(v)

    return stack + order[::-1]   # new return value!

print(graph)
print(iterative_topological_sort(graph,'a'))