with open('input/5.txt') as f:
    opcodes = list(map(lambda x: int(x), f.read().split(',')))


def op1(a, b, c, position):
    opcodes[c] = a + b
    return position + 4


def op2(a, b, c, position):
    opcodes[c] = a * b
    return position + 4


def op3(param, position):
    # opcodes[param] = 1
    opcodes[param] = 5  # part 1 get 1 as input, part 2 is 5
    return position + 2


def op4(param, position):
    print(param)  # you see 0s it's all good baby baby
    return position + 2


def op5(a, b, pos):
    return b if a != 0 else pos + 3


def op6(a, b, pos):
    return b if a == 0 else pos + 3


def op7(a, b, c, pos):
    opcodes[c] = 1 if a < b else 0
    return pos + 4


def op8(a, b, c, pos):
    opcodes[c] = 1 if a == b else 0
    return pos + 4


def decode_instruction(instruction):
    opcode = int(instruction[-2:]) if len(instruction) > 1 else int(instruction)
    c = int(instruction[-3]) if len(instruction) > 2 else 0
    b = int(instruction[-4]) if len(instruction) > 3 else 0
    a = int(instruction[-5]) if len(instruction) > 4 else 0
    return a, b, c, opcode


ops = {1: op1, 2: op2, 3: op3, 4: op4, 5: op5, 6: op6, 7: op7, 8: op8}

index = 0
while True:
    a, b, c, instruction = decode_instruction(str(opcodes[index]))  # get opcode number no matter the representation
    if instruction == 99:
        break
    elif instruction in [1, 2, 7, 8]:
        # note that cba, c is 1st param, b is 2nd param, a is 3rd according to problem statement
        c = opcodes[opcodes[index + 1]] if c == 0 else opcodes[index + 1]
        b = opcodes[opcodes[index + 2]] if b == 0 else opcodes[index + 2]
        a = opcodes[index + 3]
        index = ops[instruction](c, b, a, index)
    elif instruction == 3:
        index = ops[instruction](opcodes[index + 1], index)
    elif instruction == 4:
        c = opcodes[opcodes[index + 1]] if c == 0 else opcodes[index + 1]
        index = ops[instruction](c, index)
    elif instruction in [5, 6]:
        c = opcodes[opcodes[index + 1]] if c == 0 else opcodes[index + 1]
        b = opcodes[opcodes[index + 2]] if b == 0 else opcodes[index + 2]
        index = ops[instruction](c, b, index)
