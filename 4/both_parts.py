# generate increasing in range
res = []


def has_at_least_one_adjacent_digit_same(number):
    number = str(number)
    windowed = [number[i:i + 2] for i in range(len(number) - 1)]
    for window in windowed:
        if window[0] == window[1]:
            return True
    return False


def has_at_least_a_group_of_two_same_digits(number):
    number = str(number)
    groups = [[number[0]]]
    for i in range(1, len(number)):
        if number[i] == number[i - 1]:
            groups[-1].append(number[i])
        else:
            groups.append([number[i]])
    return any(map(lambda x: len(x) == 2, groups))


def generate_non_decreasing_numbers(number, digit, digits_left):
    if digits_left == 0:
        res.append(number)
        return

    for d in range(digit, 10):
        generate_non_decreasing_numbers(number * 10 + d, d, digits_left - 1)


generate_non_decreasing_numbers(0, 0, 6)  # side effecty

possible_passwords = list(filter(lambda x: x > 240920 and x < 789857, res))

ans1 = len(list(filter(has_at_least_one_adjacent_digit_same, possible_passwords)))
ans2 = len(list(filter(has_at_least_a_group_of_two_same_digits, possible_passwords)))
print(ans1, ans2)
