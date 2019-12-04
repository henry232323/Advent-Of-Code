mx = 765869
mn = 234208

def is_valid(n):
    n = str(n)
    for x in range(len(n)-1):
        if n[x] == n[x + 1]:
            break
    else:
        return False

    for x in range(len(n)-1):
        if int(n[x]) > int(n[x+1]):
            return False

    return True

ct = 0
for i in range(mn, mx+1):
    ct += is_valid(i)

print(ct)
