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

    opponent, todo = entry.split()
    scores = dict(X=1, Y=2, Z=3)
    wins = dict(A='Y', B='Z', C='X')
    losses = dict(A='Z', B='X', C='Y')
    same = dict(A='X', B='Y', C='Z')
    mine = dict(X=losses[opponent], Y=same[opponent], Z=wins[opponent])[todo]

    total += scores[mine]
    if wins[opponent] == mine:
        total += 6
    elif same[opponent] == mine:
        total += 3

    # print(total)

print(total)