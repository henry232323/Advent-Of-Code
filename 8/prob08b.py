import itertools
import collections

f = open("input.txt").read()

n = 25 * 6
layers = []

for i in range(len(f) // n):
    l = f[i * n:(i+1) * n]
    layers.append(l)
final = []
for pixels in zip(*layers):
    for p in pixels:
        if p != "2":
            final.append(p)
            break
    else:
        final.append(p)
print(len(final))
for i, c in enumerate(final):
    print("#" if c == '1' else " ", end="")
    if (i+1) % 25 == 0:
        print()
