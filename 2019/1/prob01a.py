def fuel(m):
    return int(m / 3) - 2


with open("input.txt", 'r') as f:
    s = 0
    for l in f.read().split():
        s += fuel(int(l))

print(s)
