f = open("input3.txt")
text = f.read()
# text = """vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw"""

sets = text.strip().split("\n")

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priority_sum = 0
for sacks in chunker(sets, 3):
    if not sacks:
        continue

    items = set(sacks[0])
    for sack in sacks:
        items = set(items) & set(sack)

    priority_sum += priorities.index(list(items)[0]) + 1

print(priority_sum)