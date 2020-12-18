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

def day10_1():
    nums = sorted(int(x.strip()) for x in open("input10.txt") if x.strip())
    nums.insert(0, 0)
    nums.append(nums[-1] + 3)
    sets = zip(nums[:-1], nums[1:])
    ac, bc = 0, 0
    for a, b in sets:
        if b - a == 1:
            ac += 1
        if b - a == 3:
            bc += 1

    return ac * bc


def day10_2_traverse(index, opts, account):
    if index in account:
        return account[index]
    if index >= len(opts) - 1:
        return 1
    count = 0
    dindex = index + 1
    while dindex != len(opts) and opts[dindex] - opts[index] in (1, 2, 3):
        count += day10_2_traverse(dindex, opts, account)
        dindex += 1

    if index not in account:
        account[index] = count

    return count

def day10_2():
    nums = sorted(int(x.strip()) for x in open("input10.txt") if x.strip())
    nums.insert(0, 0)
    nums.append(nums[-1] + 3)
    return day10_2_traverse(0, nums, {})

import numpy as np

def adj(i, j, m, n):
    adjacent_indices = []
    if i > 0:
        adjacent_indices.append((i-1,j))
    if i+1 < m:
        adjacent_indices.append((i+1,j))
    if j > 0:
        adjacent_indices.append((i,j-1))
    if j+1 < n:
        adjacent_indices.append((i,j+1))
    return adjacent_indices

def pr(*args):
    print(*args)
    return args

def day11_1():
    k = {".": 0, "L": 1, "#": 2}
    maps = np.array([[k[y] for y in x] for x in open("input11.txt").read().split("\n") if x])
    last = None
    current = maps
    while not np.array_equal(last, current):
        last = current
        current = current.copy()
        for i in range(len(maps)):
            for j in range(len(maps[i])):
                if last[i][j] == 1:
                    if (last[max(0, i-1):i+2, max(0, j-1):j+2] == 2).sum() == 0:
                        current[i][j] = 2
                elif last[i][j] == 2:
                    if (last[max(0, i-1):i+2, max(0, j-1):j+2] == 2).sum() >= 5:
                        current[i][j] = 1
        
    return (last == 2).sum()

def vindex(index, arr):
    return 0 <= index[0] < len(arr) and 0 <= index[1] < len(arr[0])

def day11_2():
    dirs = [(0,1), (1,1), (1,0), (1,-1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    k = {".": 0, "L": 1, "#": 2}
    maps = np.array([[k[y] for y in x] for x in open("input11.txt").read().split("\n") if x])
    last = None
    current = maps
    while not np.array_equal(last, current):
        last = current
        current = current.copy()
        for i in range(len(maps)):
            for j in range(len(maps[i])):
                if last[i, j] == 2:
                    ct = 0
                    for dir in dirs:
                        cp = np.array([i, j]) + dir
                        while vindex(cp, maps) and last[tuple(cp)] not in (1, 2):
                            cp += dir
                        if vindex(cp, maps) and last[tuple(cp)] == 2:
                            ct += 1
                    if ct >= 5:
                        current[i, j] = 1
                if last[i, j] == 1:
                    ct = 0
                    for dir in dirs:
                        cp = np.array([i, j]) + dir
                        while vindex(cp, maps) and last[tuple(cp)] not in (1, 2):
                            cp += dir
                        if vindex(cp, maps) and last[tuple(cp)] == 2:
                            ct += 1
                    if ct == 0:
                        current[i, j] = 2
                        
        
    return (current == 2).sum()

def day12_1():
    instructions = open("input12.txt").read().split()
    cpos = np.array([0,0])
    dir = np.e**(1j * np.pi)
    for (inst, *rest) in instructions:
        if inst == "W":
            cpos[0] += int("".join(rest))
        elif inst == "E":
            cpos[0] -= int("".join(rest))
        elif inst == "N":
            cpos[1] += int("".join(rest))
        elif inst == "S":
            cpos[1] -= int("".join(rest))

        elif inst == "F":
            amt = int("".join(rest))
            cpos += [int(dir.real) * amt, int(dir.imag) * amt]
        elif inst == "L":
            dir /= np.e**(1j * int("".join(rest)) / 180 * np.pi)
        elif inst == "R":
            dir *= np.e**(1j * int("".join(rest)) / 180 * np.pi)

    return abs(int(cpos[0])) + abs(int(cpos[1]))

import math
def day12_2():
    instructions = [x for x in open("input12.txt").read().split() if x]
    ship = np.array([0.,0.])
    wayp = np.array([-10.,1.])
    for (inst, *rest) in instructions:
        if inst == "W":
            wayp[0] += int("".join(rest))
        elif inst == "E":
            wayp[0] -= int("".join(rest))
        elif inst == "N":
            wayp[1] += int("".join(rest))
        elif inst == "S":
            wayp[1] -= int("".join(rest))

        elif inst == "F":
            amt = int("".join(rest))
            ship += amt * wayp
        elif inst == "L":
            ang = -int("".join(rest)) * np.pi / 180
            dp = np.linalg.norm(wayp) * np.e**(1j * (ang + math.atan2(wayp[1], wayp[0])))
            wayp[:] = round(dp.real), round(dp.imag)
        elif inst == "R":
            ang = int("".join(rest)) * np.pi / 180
            dp = np.linalg.norm(wayp) * np.e**(1j * (ang + math.atan2(wayp[1], wayp[0])))
            wayp[:] = round(dp.real), round(dp.imag)

    return abs(int(ship[0])) + abs(int(ship[1]))

def day13_1():
    inst = [x for x in open("input13.txt").read().split() if x]
    ctime = int(inst[0])
    rest = inst[1].split(',')
    es = []
    for bus in rest:
        if bus == 'x':
            continue
        else:
            bid = int(bus)
            e = (ctime//(bid) + 1) * bid
            es.append((e, bid))
            
    mes = min(es)
    return (mes[0] - ctime) * mes[1]

from functools import reduce

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n,a):
        p=prod / n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1

def day13_2():
    inst = [x for x in open("input13.txt").read().split() if x]
    ctime = int(inst[0])
    rest = inst[1].split(',')

    nums = []
    for i, r in enumerate(rest):
        if r != 'x':
            nums.append((int(r), len(rest) - i + 1))

    d = list(zip(*nums))
    return chinese_remainder(*d) - len(rest)

import re
def day14_1():
    inst = [x for x in open("input14.txt").read().split("\n") if x]
    mem = dict()
    for line in inst:
        if line.startswith("mask"):
            mask = line.split("= ")[1]
            continue
        m = re.match(r"mem\[(\d+)\] = (\d+)", line)
        memid, value = m.groups()
        nv = list(bin(int(value))[2:].zfill(len(mask)))
        for i in range(len(mask)-1, -1, -1):
            if mask[i] == 'X':
                continue
            nv[i] = mask[i]

        mem[memid] = int("".join(nv), 2)

    return sum(mem.values())

def day14_2():
    inst = [x for x in open("input14.txt").read().split("\n") if x]
    mem = dict()
    for line in inst:
        if line.startswith("mask"):
            mask = line.split("= ")[1]
            dmasks = list(mask)
            xs = mask.count('X')
            masks = []
            #print("MK" + mask)
            for i in range(2**xs):
                vs = list(bin(i)[2:].zfill(xs))
                #print("".join(vs))
                dupe = dmasks.copy()
                for j, c in enumerate(dupe):
                    if c == 'X':
                        dupe[j] = str( int(vs.pop(0)) + 2)

                #print("".join(dupe))
                masks.append("".join(dupe))
                
            continue
        
        m = re.match(r"mem\[(\d+)\] = (\d+)", line)
        memid, value = m.groups()
        #print('M', bin(int(memid))[2:].zfill(len(mask)))
        for dmask in masks:
            nv = list(bin(int(memid))[2:].zfill(len(dmask)))
            for ir in range(len(dmask)-1, -1, -1):
                if dmask[ir] == '0':
                    continue
                if dmask[ir] == '1':
                    nv[ir] = dmask[ir]
                if dmask[ir] == '2':
                    nv[ir] = '0'
                if dmask[ir] == '3':
                    nv[ir] = '1'
                
            #print('V', "".join(nv))
            mem[int("".join(nv), 2)] = int(value)

    #print(mem)
    return sum(mem.values())

def day15_1():
    inst = [int(x) for x in open("input15.txt").read().split(',') if x]
    inst.reverse()
    tc = len(inst) - 1
    while tc < 2020:
        try:
            inst.insert(0, inst[1:].index(inst[0]) + 1)
        except:
            inst.insert(0, 0)
        tc += 1

    return inst[1]

def day15_2():
    inst = [int(x) for x in open("input15.txt").read().split(',') if x]
    pos = {x: y for y, x in enumerate(inst[:-1])}
    tc = len(inst) - 1
    while tc < 30000000:
        inst.append(tc - pos.get(inst[-1], tc))
        pos[inst[-2]] = tc
        tc += 1

    return inst[-2]

def day16_1():
    inst = open("input16.txt").read().split('\n')

    fields = dict()
    i = 0
    
    r = "(.+): (\d+)-(\d+) or (\d+)-(\d+)"
    while (line := inst[i]):
        m = re.match(r, line)
        g = m.groups()

        fields[g[0]] = [
            range(int(g[1]),
                  int(g[2]) + 1
            ),
            range(
                int(g[3]),
                int(g[4]) + 1
            )
        ]
        i += 1

    i += 2
    while (line := inst[i]):
        i += 1

    i += 2
    ival = list()
    while (line := inst[i]):
        vals = [int(x) for x in line.split(",")]
        for val in vals:
            if all(val not in v[0] and val not in v[1] for v in fields.values()):
                ival.append(val)

        i += 1

    return sum(ival)
            
    
import functools
def day16_2():
    inst = open("input16.txt").read().split('\n')

    fields = dict()
    i = 0
    
    r = "(.+): (\d+)-(\d+) or (\d+)-(\d+)"
    while (line := inst[i]):
        m = re.match(r, line)
        g = m.groups()

        fields[g[0]] = [
            range(int(g[1]),
                  int(g[2]) + 1
            ),
            range(
                int(g[3]),
                int(g[4]) + 1
            )
        ]
        i += 1

    i += 2
    
    vvals = [set(fields.keys()) for i in range(len(fields))]
    def do_line(line):
        vals = [int(x) for x in line.split(",")]
        kvv = []
        for r, val in enumerate(vals):
            vv = set()
            for f, (range1, range2) in fields.items():
                if val in range1 or val in range2:
                    vv.add(f)

            kvv.append(vv)

            if not vv:
                return
            
        else:
            for d, s2 in enumerate(kvv):
                vvals[d] = vvals[d] & s2

            checked = []
            while any(((len(vvals[r]) == 1) and (r not in checked)) for r in range(len(vvals))):
                xd = next(r for r in range(len(vvals)) if len(vvals[r]) == 1 and (r not in checked))
                checked.append(xd)
                for r in range(len(vvals)):
                    if r == xd:
                        continue
                    vvals[r] -= vvals[xd]
                

    
    while (line := inst[i]):
        mt = [int(x) for x in line.split(',')]
        do_line(line)
        i += 1

    i += 2

    while (line := inst[i]):
        do_line(line)
        
        i += 1

    myvals = [mt[i] for i, fields in enumerate(vvals) if next(iter(fields)).startswith('departure')]
    return functools.reduce((lambda x, y: x * y), myvals)

def mhd(p1, p2):
    return (np.array(p1) - np.array(p2)).abs().sum()

def day17_1():
    inst = [x for x in open("input17.txt").read().split('\n') if x]
    gmap = {}
    gmap = np.zeros((len(inst), len(inst[0]), 1))
    for i in range(len(inst)):
        for j in range(len(inst[i])):
            gmap[j,i,0] = 0 if inst[i][j] == '.' else 1

    for b in range(6):
        ngm = np.pad(gmap, ((1,1),(1,1),(1,1)), mode='constant', constant_values=0)
        
        for coord in np.ndindex(ngm.shape):
            nearby = gmap[tuple(slice(max(0, x-2), min(x+1, gmap.shape[i])) for i, x in enumerate(coord))]
            nearby = nearby.sum()
            
            try:
                nearby -= gmap[tuple(slice(x-1, x) for x in coord)][0][0][0]
            except:
                pass
            
            if nearby == 3:
                ngm[coord] = 1
            else:
                if nearby not in (2,3):
                    ngm[coord] = 0

        gmap = ngm

    return gmap.sum()

def day17_2():
    inst = [x for x in open("input17.txt").read().split('\n') if x]
    gmap = {}
    gmap = np.zeros((len(inst), len(inst[0]), 1, 1))
    for i in range(len(inst)):
        for j in range(len(inst[i])):
            gmap[j,i,0,0] = 0 if inst[i][j] == '.' else 1

    for b in range(6):
        ngm = np.pad(gmap, ((1,1),(1,1),(1,1),(1,1)), mode='constant', constant_values=0)
        
        for coord in np.ndindex(ngm.shape):
            nearby = gmap[tuple(slice(max(0, x-2), min(x+1, gmap.shape[i])) for i, x in enumerate(coord))]
            nearby = nearby.sum()
            
            try:
                nearby -= gmap[tuple(slice(x-1, x) for x in coord)][0][0][0][0]
            except:
                pass
            
            if nearby == 3:
                ngm[coord] = 1
            else:
                if nearby not in (2,3):
                    ngm[coord] = 0

        gmap = ngm

    return gmap.sum()

def evaluate(expr):
    expr = expr.strip()
    stack = []
    cval = None
    expr = expr.replace("(", "( ").replace(")", " )")
    tokens = expr.split()
    operator = None
    for token in tokens:
        if token.isdigit():
            if cval is None:
                cval = int(token)
                continue
            if operator == "*":
                cval *= int(token)
            else:
                cval += int(token)
        elif token == "(":
            stack.append((cval, operator))
            cval = None
        elif token == ")":
            nc, nop = stack.pop()
            if nop == "*":
                cval = (nc if nc is not None else 1) * cval
            else:
                cval = (nc if nc is not None else 0) + cval

        else:
            operator = token

    return cval

def day18_1():
    exprs = [x for x in open("input18.txt").read().split("\n") if x]
    return sum(evaluate(x) for x in exprs)

def evaluate2(expr): # shunting-yard algorithm http://www.martinbroadhurst.com/shunting-yard-algorithm-in-python.html
    ops = {"*": lambda x, y: int(x) * int(y), "+": lambda x, y: int(x) + int(y)}
    prec = {"+": 1, "*": 0}
    expr = expr.strip()
    stack = []
    output = []
    expr = expr.replace("(", "( ").replace(")", " )")
    tokens = expr.split()
    for token in tokens:
        if token.isdigit():
            output.append(int(token))
        elif token == '(':
            stack.append(token)
        elif token == ')':
            top = stack[-1] if stack else None
            while top is not None and top != '(':
                operator = stack.pop()
                right = output.pop()
                left = output.pop()
                output.append(ops[operator](left, right))
                              
                top = stack[-1] if stack else None
                
            stack.pop()
        else:
            top = stack[-1] if stack else None
            while top is not None and top not in "()" and prec.get(top) > prec.get(token):
                operator = stack.pop()
                right = output.pop()
                left = output.pop()
                output.append(ops[operator](left, right))
                
                top = stack[-1] if stack else None
            stack.append(token)
    while stack:
        operator = stack.pop()
        right = output.pop()
        left = output.pop()
        output.append(ops[operator](left, right))

    return output[0]

def day18_2():
    exprs = [x for x in open("input18.txt").read().split("\n") if x]
    return sum(evaluate2(x) for x in exprs)
            
print(day17_2())
