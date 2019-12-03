from collections import defaultdict

with open("input.txt", 'r') as f:
    l1 = f.readline().strip()
    l2 = f.readline().strip()

pos1 = list(l1.split(","))
pos2 = list(l2.split(","))

arr =  defaultdict(lambda: ".")
arr[0, 0] = "O"

cx = 0
cy = 0
for inst in pos1:
    dir = inst[0]
    dist = int(inst[1:])
    for i in range(dist):
        if (dir == "U"):
            cy += 1
        elif dir == "D":
            cy -= 1
        elif dir == "L":
            cx -= 1
        elif dir == "R":
            cx += 1
        if arr[cx, cy] == "-":
            arr[cx, cy] = "X"
        else:
            arr[cx, cy] = "-"

cx = 0
cy = 0
ct = 0
for inst in pos2:
    dir = inst[0]
    dist = int(inst[1:])
    for i in range(dist):
        ct += 1
        if (dir == "U"):
            cy += 1
        elif dir == "D":
            cy -= 1
        elif dir == "L":
            cx -= 1
        elif dir == "R":
            cx += 1
        if arr[cx, cy] in ("-", "X"):
            arr[cx, cy] = ct
        else:
            arr[cx, cy] = "|"

cx = 0
cy = 0
ct = 0
for inst in pos1:
    dir = inst[0]
    dist = int(inst[1:])
    for i in range(dist):
        ct += 1
        if (dir == "U"):
            cy += 1
        elif dir == "D":
            cy -= 1
        elif dir == "L":
            cx -= 1
        elif dir == "R":
            cx += 1
        if isinstance(arr[cx, cy], int):
            arr[cx, cy] += ct

print([(k, v) for k, v in arr.items() if isinstance(v, int)])
print(min(arr.values(), key=lambda x: (not isinstance(x, int), x)))
