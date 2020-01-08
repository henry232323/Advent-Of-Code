from fractions import Fraction
import copy
import math


def printSet(b):
    print("\n".join("".join(x) for x in b))


f = [list(x) for x in open("input.txt", "r").read().split("\n")]

for current_x, row in f:
    for current_y, col in row:
        pass