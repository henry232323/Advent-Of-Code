f = open("input3.txt")
text = f.read()
# text = """vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw"""

sets = text.split("\n")

priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priority_sum = 0
for entry in sets:
    if not entry:
        continue

    first, second = entry[:len(entry)//2], entry[len(entry)//2:]
    diff = set(first) & set(second)
    priority_sum += priorities.index(list(diff)[0]) + 1

print(priority_sum)
