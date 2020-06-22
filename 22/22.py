inp = """cut -8737
deal with increment 36
deal into new stack
deal with increment 32
cut -3856
deal with increment 27
deal into new stack
cut 8319
deal with increment 15
deal into new stack
deal with increment 53
cut 2157
deal with increment 3
deal into new stack
cut 9112
deal with increment 59
cut 957
deal with increment 28
cut -9423
deal with increment 51
deal into new stack
deal with increment 8
cut 3168
deal with increment 16
cut 6558
deal with increment 32
deal into new stack
cut -8246
deal with increment 40
cut 4405
deal with increment 9
cut -2225
deal with increment 36
cut -5080
deal with increment 59
cut -648
deal with increment 64
cut -1845
deal into new stack
cut -7726
deal with increment 44
cut 1015
deal with increment 12
cut 960
deal with increment 30
deal into new stack
deal with increment 65
deal into new stack
deal with increment 27
cut 6877
deal with increment 5
deal into new stack
cut -3436
deal with increment 63
deal into new stack
deal with increment 71
deal into new stack
deal with increment 7
cut -9203
deal with increment 38
cut 9008
deal with increment 59
deal into new stack
deal with increment 13
cut 5979
deal with increment 55
cut 9483
deal with increment 65
cut -9250
deal with increment 75
deal into new stack
cut -1830
deal with increment 55
deal into new stack
deal with increment 67
cut -8044
deal into new stack
cut 8271
deal with increment 51
cut 6002
deal into new stack
deal with increment 47
cut 3638
deal with increment 18
cut -785
deal with increment 63
cut -2460
deal with increment 25
cut 5339
deal with increment 61
cut -5777
deal with increment 54
deal into new stack
cut 8075
deal into new stack
deal with increment 22
cut 3443
deal with increment 34
cut 5193
deal with increment 3
"""
inp = inp.splitlines()
cards = list(range(10007))
def dins(cards):
  return cards[::-1]

def cut(n,cards):
    return cards[n:]+cards[:n]


def dwin(i,cards):
  res = [None for _ in range(len(cards))]
  at = 0
  res[at] = cards.pop(0)
  count = 1
  while cards:
    at = (at+i)%len(res)
    res[at] = cards.pop(0)
    count+=1
  return res

for action in inp:
  if 'new stack' in action:
    cards = dins(cards)
  if 'increment' in action:
    cards = dwin( int(''.join(c for c in action if c.isdigit())),cards)
  if 'cut' in action:
    cards = cut(int(''.join(c for c in action if c in '-1234567890')),cards)

print(cards.index(2019))

ld = 119315717514047
card = 2020
times = 101741582076661
# q came from aq + b
a = 1
b = 0
for action in reversed(inp):
    if 'increment' in action:
        inc = int(''.join(c for c in action if c.isdigit()))
        #card = card * pow(inc, ld-2,ld) % ld
        p = pow(inc, ld-2,ld)
        a *= p
        b *= p
    elif 'cut' in action:
        inc = int(''.join(c for c in action if c in '-1234567890'))
        #card = (card - inc + ld) % ld
        b += inc
    elif 'new stack' in action:
        #card = ld - 1 - card
        b += 1
        a *= -1
        b *= -1
    else:
      continue
    a %= ld
    b %= ld
    # print(line, (a * card + b) % ld)

# q
# aq + b
# a(aq+b) + b = a^2q + ab + b
# a(a^2q + ab + b) = a^3q + a^2b + ab + b
# ...
# a^t q + b * (a^t - 1) / (a - 1)
print((
    pow(a, times, ld) * card +
    b * (pow(a, times, ld) +ld- 1)
      * (pow(a-1, ld - 2, ld))
) % ld)
print("DONE")