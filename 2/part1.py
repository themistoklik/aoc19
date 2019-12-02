with open('input/1.txt') as f:
    opcodes = list(map(lambda x: int(x), f.read().split(',')))

ops = {1: lambda x, y: x + y, 2: lambda x, y: x * y}

index = 0

while index < len(opcodes):
    if opcodes[index] == 99:
        break
    opcodes[opcodes[index + 3]] = ops[opcodes[index]](opcodes[opcodes[index + 2]], opcodes[opcodes[index + 1]])
    index += 4

print(opcodes)
