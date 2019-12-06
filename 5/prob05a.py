f = open("input0.txt")

pos = [int(x.strip()) for x in f.read().split(",")]

store = None
i = 0
while True:
    #print(i, pos[i])
    inst = pos[i] % 100

    cmode = pos[i] // 100 % 2
    bmode = pos[i] // 1000 % 2
    amode = pos[i] // 10000 % 2

    if inst == 99:
        break
    if inst in (1, 2, 5, 6, 7, 8):
        cval = pos[i + 1] if cmode else pos[pos[i + 1]]
        bval = pos[i + 2] if bmode else pos[pos[i + 2]]
        #posa = i + 3 if amode else pos[i + 3]

    if inst == 1:
        #print(f"set pos {i + 3} to {cval} + {bval} = {cval + bval}")
        pos[pos[i + 3]] = cval + bval
        i += 4
    elif inst == 2:
        #print(f"set pos {i + 3} to {cval} * {bval} = {cval * bval}")
        pos[pos[i + 3]] = cval * bval
        i += 4
    elif inst == 3:
        pos[pos[i + 1]] = int(input())
        #print(f"set pos {pos[i + 1]} to {pos[pos[i + 1]]}")
        i += 2
    elif inst == 4:
        print(pos[pos[i + 1]])
        i += 2
    elif inst == 5:
        #print(cval, bval)
        #print("CTR: ", cval)
        if cval != 0:
            i = bval
        else:
            i += 3
    elif inst == 6:
        if cval == 0:
            i = bval
        else:
            i += 3
    elif inst == 7:
        pos[pos[i + 3]] = cval < bval
        i += 4
    elif inst == 8:
        pos[pos[i + 3]] = cval == bval
        i += 4
    else:
        raise ValueError("Invalid instruction: " + str(inst))
