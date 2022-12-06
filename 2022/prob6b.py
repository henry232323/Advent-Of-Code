f = open("input6.txt")
text = f.read()
text = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""

sets = text.strip().split("\n")

count = 0
for entry in sets:
    if not entry:
        continue

    for i in range(len(entry) - 13):
        chars = entry[i:i+14]
        if len(set(chars)) == 14:
            print(i + 14)
            break

print(count)
