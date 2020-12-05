f = open("input.txt")

pos = [int(x) for x in f.read().split(",")]
pos[1] = 12
pos[2] = 2

i = 0
while i < len(pos):
    if pos[i] == 1:
        pos[pos[i + 3]] = pos[pos[i + 1]] + pos[pos[i + 2]]
        i += 4
    elif pos[i] == 2:
        pos[pos[i + 3]] = pos[pos[i + 1]] * pos[pos[i + 2]]
        i += 4
    elif pos[i] == 99:
        break

print(pos[0])
