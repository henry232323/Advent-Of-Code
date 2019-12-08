import itertools
import collections

f = open("input.txt").read()

n = 25 * 6
layers = []

for i in range(len(f) // n):
    l = f[i * n:(i+1) * n]
    layers.append(l)

ml = min(layers, key=lambda x: x.count("0"))
print(ml.count("1") * ml.count("2"))
