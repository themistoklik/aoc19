with open('input/1.txt') as f:
    print(sum([(int(line.strip()) // 3 - 2) for line in f.readlines()]))

