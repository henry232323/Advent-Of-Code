import itertools

def day1_1():
    f = open("input1.txt")
    d = [int(x) for x in f.read().split("\n") if x]
    return next(x * y for x, y in itertools.product(d, d) if x + y == 2020)

def day1_2():
    f = open("input1.txt")
    d = [int(x) for x in f.read().split("\n") if x]
    return next(x * y * z for x, y, z in itertools.product(d, d, d) if x + y +z == 2020)


def day1_1opt():
    return
"""
    f = open("input1.txt")
    nums = []
    for i, l in enumerate(f): # n
        n = int(l.strip())
        while True: # log2(n)
            if not nums:
                nums.append(n)
                break
            k = nums[i//2]
            if k == n:
        

    for i in d: # n
        if 2020 - i in d: # log2(n)
            return i * (2020 - i)
"""

def day2_1():
    c = 0
    for row in open("input2.txt"):
        nums, letter, p = row.split()
        p = p.strip()
        letter = letter[:-1]
        lb, ub = [int(x) for x in nums.split("-")]
        if lb <= p.count(letter) <= ub:
            c += 1
    return c

def day2_2():
    c = 0
    for row in open("input2.txt"):
        nums, letter, p = row.split()
        p = p.strip()
        letter = letter[:-1]
        lb, ub = [int(x) - 1 for x in nums.split("-")]
        if (p[lb] == letter or p[ub] == letter) and not (p[lb] == letter and p[ub] == letter):
            c += 1
    return c

def day3_1():
    m = open("input3.txt").read().split("\n")
    cx, cy = 0, 0
    count = 0
    while cy < len(m) - 1:
        if m[cy][cx % len(m[cy])] == "#":
            count += 1
        cx += 3
        cy += 1
    return count

def day3_2():
    m = open("input3.txt").read().split("\n")
    def do_run(dx, dy):
        cx, cy = 0, 0
        count = 0
        while cy < len(m) - 1:
            if m[cy][cx % len(m[cy])] == "#":
                count += 1
            cx += dx
            cy += dy
        return count

    r = 1
    for dx, dy in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
        r *= do_run(dx, dy)
    return r

def day4_1():
    f = open("input4.txt")
    c = 0
    while True:
        entries = {}
        while (line := f.readline().strip()):
            e = [ent.split(":") for ent in line.split()]
            #print(e)
            entries.update(e)
        if not entries:
            break
        if all(x in entries for x in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]):
            c += 1
    return c

def intify(x):
    try:
        return int(x)
    except:
        return 0

def ishex(x):
    try:
        int(x, 16)
        return True
    except:
        return False

def day4_2():
    f = open("input4.txt")
    c = 0
    while True:
        entries = {}
        while (line := f.readline().strip()):
            e = [ent.split(":") for ent in line.split()]
            #print(e)
            entries.update(e)
        if not entries:
            break
        # (150 <= int(x[:-2] or 0) <= 193) if (x := entries.get("hgt", '0cm')).endswith('cm') else ((59 <= int(x[:-2] or 0) <= 76) and x[:-2] == 'in'),
        he = entries.get("hgt", '0cm')
        if he.endswith('cm'):
            height_check = 150 <= int(he[:-2] or 0) <= 193
        elif he.endswith('in'):
            height_check = (59 <= int(he[:-2] or 0) <= 76)
        else:
            height_check = False
        
        cond = [
            1920 <= intify(entries.get("byr", 0)) <= 2002,
            2010 <= intify(entries.get("iyr", 0)) <= 2020,
            2020 <= intify(entries.get("eyr", 0)) <= 2030,
            height_check,
            ishex(entries.get("hcl", '#J')[1:]) and entries.get("hcl", '#J').startswith("#"),
            entries.get("ecl") in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
            entries.get("pid", "a").isdigit() and len(entries.get("pid", "a")) == 9
        ]
            
        if all(cond):
            c += 1
    return c

def day5_1():
    f = open("input5.txt").read().split("\n")
    m = 0
    for line in f:
        if not line:
            continue
        r, c = line[:7], line[7:]
        r = r.replace("B", "1").replace("F", "0")
        c = c.replace("R", "1").replace("L", "0")
        sid = int(r, 2) * 8 + int(c, 2)
        if sid > m:
            m = sid
    return m

def day5_2():
    f = open("input5.txt").read().split("\n")
    ids = []
    for line in f:
        if not line:
            continue
        r, c = line[:7], line[7:]
        r = r.replace("B", "1").replace("F", "0")
        c = c.replace("R", "1").replace("L", "0")
        sid = int(r, 2) * 8 + int(c, 2)
        ids.append(sid)

    return set(range(min(ids), max(ids) + 1)) - set(ids)

def day6_1():
    f = open("input6.txt")
    c = 0
    while True:
        entries = set()
        while (line := f.readline().strip()):
            entries.update(line)
        if not entries:
            break
        c += len(entries)
    return c

def day6_2():
    f = open("input6.txt")
    c = 0
    while True:
        entries = None
        while (line := (cline := f.readline()).strip()):
            if entries is None:
                entries = set(line)
            else:
                entries = entries & set(line)
        c += len(entries)
        if not cline:
            break
    return c

from collections import defaultdict

def day7_1_traverse(bags, fc, bagsdict):
    for bag in bags:
        if bag in fc:
            continue
        else:
            fc.add(bag)
            day7_1_traverse(bagsdict[bag], fc, bagsdict)
            

def day7_1():
    f = open("input7.txt").read().split("\n")
    bags = defaultdict(list)
    for line in f:
        if not line: continue
        
        k, vs = line.split("contain")
        k = k.strip()
        vs = [v.strip().strip(".") for v in vs.split(",")]
        res = []
        for v in vs:
            if v[0].isdigit():
                n, b = v.split(' ', 1)
                bags[b.rstrip('s')].append(k.rstrip('s'))

    fc = set()
    day7_1_traverse(bags['shiny gold bag'], fc, bags)

    return len(fc)

def day7_2_traverse(bagsdict, bagdata):
    count = 1
    for n, bag in bagdata:
        count += n * day7_2_traverse(bagsdict, bagsdict[bag])
    return count

def day7_2():
    f = open("input7.txt").read().split("\n")
    bags = {}
    for line in f:
        if not line: continue
        
        k, vs = line.split("contain")
        k = k.strip()
        vs = [v.strip().strip(".") for v in vs.split(",")]
        res = []
        for v in vs:
            if v[0].isdigit():
                n, b = v.split(' ', 1)
                res.append((int(n), b.rstrip('s')))
        bags[k.rstrip('s')] = res

    return day7_2_traverse(bags, bags['shiny gold bag']) - 1

def day8_1():
    f = open("input8.txt").read().split("\n")
    args = [line.split(" ") for line in f]
    acc = 0
    pt = 0
    run = set()
    while pt < len(args):
        inst, arg = args[pt]
        if pt in run:
            return acc
        run.add(pt)
        if inst == "acc":
            acc += int(arg)
            pt += 1
        elif inst == "nop":
            pt += 1
        elif inst == "jmp":
            pt += int(arg)

    return acc

import copy
def day8_2():
    f = open("input8.txt").read().split("\n")
    args = [line.split(" ") for line in f if line]
    for i, (ninst, narg) in enumerate(args):
        nargs = copy.deepcopy(args)
        if ninst == "acc":
            continue
        elif ninst == "nop":
            nargs[i][0] = "jmp"
        elif ninst == "jmp":
            nargs[i][0] = "nop"
            
        acc = 0
        pt = 0
        run = set()
        while pt < len(nargs):
            inst, arg = nargs[pt]
            if pt in run:
                break
            run.add(pt)
            if inst == "acc":
                acc += int(arg)
                pt += 1
            elif inst == "nop":
                pt += 1
            elif inst == "jmp":
                pt += int(arg)
        else:
            return acc

def day9_1():
    nums = [int(x) for x in open("input9.txt").read().split("\n") if x]
    for i in range(25, len(nums)):
        pn = set(nums[i-25:i])
        for num in pn:
            if nums[i] - num in pn:
                break
        else:
            return nums[i]

def day9_2():
    cn = day9_1()
    nums = [int(x) for x in open("input9.txt").read().split("\n") if x]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            pn = nums[i:j]
            if sum(pn) == cn:
                return max(pn) + min(pn)
