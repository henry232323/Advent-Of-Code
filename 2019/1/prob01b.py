def fuel(m):
    f = int(m / 3) - 2
    if f > 0:
        f += fuel(f)
    return max(f, 0)


with open("input.txt", 'r') as f:
    data = f.read()

s = 0
for l in data.split():
    s += fuel(int(l))

print(s)
