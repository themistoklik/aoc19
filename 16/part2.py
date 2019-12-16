from functools import reduce

with open('input/16.txt') as f:
    digits = [int(d) for d in f.readline().strip()]
offset = int(reduce(lambda x, y: str(x) + str(y), digits[:7]))

nums = (digits * 10000)[offset:]

for step in range(100):
    for i in range(len(nums) - 2, -1, -1):
        nums[i] += nums[i + 1]
        nums[i] %= 10

print(''.join(map(str, nums[:8])))  # ans2
