with open('input/6.txt') as f:
    orbits = [line.strip() for line in f.readlines()]


def walk_and_count_steps(tree, node, steps, target):
    return steps + 1 if tree[node] == target else walk_and_count_steps(tree, tree[node], steps + 1, target)


def walk_and_keep_path(tree, node, path):
    return path + ['COM'] if tree[node] == 'COM' else walk_and_keep_path(tree, tree[node],
                                                                         path + [tree[node]])


# split into par, child tuples
orbits = [pair.split(')') for pair in orbits]

children_to_parents = {}

for orbit in orbits:
    children_to_parents[orbit[1]] = orbit[0]

ans1 = sum([walk_and_count_steps(children_to_parents, node, 0, 'COM') for node in children_to_parents.keys()])

path_from_me = walk_and_keep_path(children_to_parents, 'YOU', list())
path_from_santa = walk_and_keep_path(children_to_parents, 'SAN', list())

smol_path, big_path = sorted([path_from_santa, path_from_me], key=lambda x: len(x))

big_path = set(big_path)

# find lowest common ancestor
lca = None
for node in smol_path:
    if node in big_path:
        lca = node
        break

ans2 = path_from_me.index(lca) + path_from_santa.index(lca)
print(ans2)
