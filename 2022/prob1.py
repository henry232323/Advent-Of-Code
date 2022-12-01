f = open("input1.txt")
text = f.read()

sets = text.split("\n\n")

nums = sorted(sum(int(x) for x in s.split()) for s in sets)

print(nums[-1])
print(sum(nums[-3:]))
