import re
from collections import defaultdict

f = open("input5.txt")
text = f.read()
# text = """    [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3
#
# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2"""

crates, moves = text.split("\n\n")

split = re.split(r"\s|\n", crates.replace("    ", " "))
stacks = defaultdict(list)
split, n = split[:-27], "".join(split[-27:])
print(split, n)


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


for row in chunker(split, len(n)):
    for i, crate in enumerate(row):
        if not crate:
            stacks[i]
        else:
            stacks[i].append(crate)

for col in stacks:
    print(stacks[col])

for row in moves.split("\n"):
    if not row:
        continue
    _, count, _, stack1, _, stack2 = row.split()
    for i in range(int(count)):
        stacks[int(stack2) - 1].insert(0, stacks[int(stack1) - 1].pop(0))

for key, value in stacks.items():
    print(value[0][1], end="")
print()
