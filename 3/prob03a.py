from collections import defaultdict

with open("input.txt", 'r') as f:
    l1 = f.readline().strip()
    l2 = f.readline().strip()

pos1 = l1.split(",")
pos2 = l2.split(",")

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
for inst in pos2:
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
        if arr[cx, cy] in ("-", "X"):
            arr[cx, cy] = "+"
        else:
            arr[cx, cy] = "|"

mp = min(arr.items(), key=lambda x: (x[1] != "+", abs(x[0][0]) + abs(x[0][1])))
print(abs(mp[0][0]) + abs(mp[0][1]))
