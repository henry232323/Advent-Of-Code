with open("input.txt") as f:
    data = [int(x) for x in f.read().split(",")]

for j in range(100):
    for k in range(100):
        pos = data[::]
        
        pos[1] = j
        pos[2] = k

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

        if pos[0] == 19690720:
            print(100 * j + k)
            break
