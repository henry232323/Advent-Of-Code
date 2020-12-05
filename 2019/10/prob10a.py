from fractions import Fraction
import copy
import math


def printSet(b):
    print("\n".join("".join(x) for x in b))


f = [list(x) for x in open("input.txt", "r").read().split("\n")]

counts = {}
for y, l in enumerate(f):
    for x, c in enumerate(l):
        if c != "#":
            continue

        cf = copy.deepcopy(f)
        count = 0
        for j, ls in enumerate(cf):
            for i, cs in enumerate(ls):
                if (x == i and y == j) or (cs != "#"):
                    continue
                count += 1
                try:
                    slope = Fraction(y - j, x - i)
                    n, d = int(math.copysign(y - j if y != j else 1, slope.numerator)), int(math.copysign(x - i if x != i else 1, slope.denominator))
                except ZeroDivisionError:
                    n, d = int(math.copysign(y - j, 1)), 0

                cx, cy = x + d, y + n

                while (0 <= cy < len(cf)) and (0 <= cx < len(ls)):
                    cf[cy][cx] = "."
                    print(x, y, i, j, cx, cy, n, d)
                    cy += n
                    cx += d

                cf[j][i] = "#"

        counts[x, y] = sum(z.count("#") for z in cf) - 1
        print(x, y)
        print("\n".join("".join(x) for x in cf))

print(counts)
print(max(counts.items(), key=lambda b: b[1]))
