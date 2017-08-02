import random

def park_randomly(low,high):
    if high - low < 1:
        return 0
    else:
        x = random.uniform(low,high - 1)
    return 1 + park_randomly(low,x) + park_randomly(x + 1,high)

s = 0
for i in range(1000):
    s += park_randomly(0,5)
print s / 1000.