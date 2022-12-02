f = open("input2.txt")
text = f.read()
# text = """A Y
# B X
# C Z"""

sets = text.split("\n")

total = 0
for entry in sets:
    if not entry:
        continue

    opponent, mine = entry.split()
    scores = dict(X=1, Y=2, Z=3)
    choices = dict(A='Y', B='Z', C='X')
    same = dict(A='X', B='Y', C='Z')

    total += scores[mine]
    if choices[opponent] == mine:
        total += 6
    elif same[opponent] == mine:
        total += 3

    #print(total)

print(total)