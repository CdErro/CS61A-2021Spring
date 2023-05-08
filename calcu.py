import re

total = 0
for i in range(0, 100):
    a = i ** 2
    l = str(a)
    l = l.split()
    if min(l) >= '2':
        total += 1
print(total / 100)
