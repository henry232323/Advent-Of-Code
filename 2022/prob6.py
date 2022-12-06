f = open("input6.txt")
text = f.read()
# text = """bvwbjplbgvbhsrlpgdmjqwftvncz"""

sets = text.strip().split("\n")

count = 0
for entry in sets:
    if not entry:
        continue

    for i in range(len(entry) - 3):
        chars = entry[i:i+4]
        if len(set(chars)) == 4:
            print(i + 4)
            break

print(count)
