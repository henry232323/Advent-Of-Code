f = open("input4.txt")
text = f.read()
# text = """2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8"""

sets = text.strip().split("\n")

count = 0
for entry in sets:
    if not entry:
        continue

    p1, p2 = entry.split(",")
    r1a, r1b = map(int, p1.split("-"))
    r2a, r2b = map(int, p2.split("-"))

    if r1a >= r2a and r1b <= r2b or r1a <= r2a and r1b >= r2b:
        count += 1

print(count)
