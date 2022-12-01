def day1_1():
    f = open("input1.txt")
    d = [int(x) for x in f.read().split("\n") if x]
    c = 0

    for i in range(len(d)-1):
        if d[i+1] > d[i]:
            c += 1

    print(c)

def day1_2():
    f = open("input1.txt")
    inp = f.read()
    alt = """199
200
208
210
200
207
240
269
260
263"""
    d = [int(x) for x in inp.split("\n") if x]
    c = 0

    for i in range(len(d) - 3):
        if sum(d[i:i+3]) < sum(d[i+1:i+4]):
            c += 1

    print(c)

def day2_1():
    f = open("input2.txt")
    inp = f.read()
    alt = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""
    d = [x for x in inp.split("\n") if x]

    f = 0
    y = 0

    for m in d:
        arg, dist = m.split()
        dist = int(dist)
        if arg == 'forward':
            f += dist
        elif arg == 'up':
            y += dist
        else:
            y -= dist

    print(abs(f * y))

def day2_2():
    f = open("input2.txt")
    inp = f.read()
    alt = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""
    d = [x for x in inp.split("\n") if x]

    f = 0
    depth = 0
    aim = 0

    for m in d:
        arg, dist = m.split()
        dist = int(dist)
        if arg == 'forward':
            f += dist
            depth += aim * dist
        elif arg == 'up':
            aim -= dist
        elif arg == 'down':
            aim += dist

    print(abs(f * depth))

from collections import Counter

def day3_1():
    f = open("input3.txt")
    inp = f.read()
    alt = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""
    d = [x for x in inp.split("\n") if x]

    gamma = ""
    epsilon = ""
    for i in range(len(d[0])):
        cs = Counter(item[i] for item in d)
        gamma += max(cs, key=cs.get)
        epsilon += min(cs, key=cs.get)

    print(int(gamma, 2) * int(epsilon, 2))

def day3_2():
    f = open("input3.txt")
    inp = f.read()
    alt = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""
    vals = [x for x in inp.split("\n") if x]
    oxy = vals.copy()
    co2 = oxy.copy()

    orating = None
    crating = None

    for i in range(len(oxy[0])):
        cs = Counter(item[i] for item in oxy)
        oval = max(cs, key=cs.get)
        k = min(cs, key=cs.get)
        if cs[oval] == cs[k]:
            oval = '1'
        oxy = [x for x in oxy if x[i] == oval]
        if len(oxy) == 1:
            orating = oxy[0]
            break

    for i in range(len(co2[0])):
        cs = Counter(item[i] for item in co2)
        cval = min(cs, key=cs.get)
        k = max(cs, key=cs.get)
        if cs[cval] == cs[k]:
            cval = '0'
        co2 = [x for x in co2 if x[i] == cval]
        
        if len(co2) == 1:
            crating = co2[0]
            break

    print(int(orating, 2) * int(crating, 2))
    
day3_2()
