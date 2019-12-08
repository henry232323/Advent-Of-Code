import itertools
import collections
import asyncio

f = open("input.txt")
tpos = [int(x.strip()) for x in f.read().split(",")]


async def run_program(id, inq, outq):
    # print("starting new!")
    pos = tpos[:]
    i = 0
    while True:
        # print(i, pos[i])
        inst = pos[i] % 100

        cmode = pos[i] // 100 % 2
        bmode = pos[i] // 1000 % 2
        amode = pos[i] // 10000 % 2

        if inst == 99:
            break
        if inst in (1, 2, 5, 6, 7, 8):
            cval = pos[i + 1] if cmode else pos[pos[i + 1]]
            bval = pos[i + 2] if bmode else pos[pos[i + 2]]
            # posa = i + 3 if amode else pos[i + 3]

        if inst == 1:
            # print(f"set pos {i + 3} to {cval} + {bval} = {cval + bval}")
            pos[pos[i + 3]] = cval + bval
            i += 4
        elif inst == 2:
            # print(f"set pos {i + 3} to {cval} * {bval} = {cval * bval}")
            pos[pos[i + 3]] = cval * bval
            i += 4
        elif inst == 3:
            print(id, inq._queue, outq._queue, "get b")
            pos[pos[i + 1]] = int(await inq.get())
            print(id, inq._queue, outq._queue, "get a")
            # print(f"set pos {pos[i + 1]} to {pos[pos[i + 1]]}")
            i += 2
        elif inst == 4:
            print(id, inq._queue, outq._queue, "put b")
            await outq.put(pos[pos[i + 1]])
            print(id, inq._queue, outq._queue, "put a")
            i += 2
        elif inst == 5:
            # print(cval, bval)
            # print("CTR: ", cval)
            if cval != 0:
                i = bval
            else:
                i += 3
        elif inst == 6:
            if cval == 0:
                i = bval
            else:
                i += 3
        elif inst == 7:
            pos[pos[i + 3]] = cval < bval
            i += 4
        elif inst == 8:
            pos[pos[i + 3]] = cval == bval
            i += 4
        else:
            raise ValueError("Invalid instruction: " + str(inst))

    if id == 4:
        print("DONE!")
        results.append(outq.get_nowait())
    print(len(tasks), len(results))


results = collections.deque()
tasks = []

async def main():
    for val in itertools.permutations([5, 6, 7, 8, 9], 5):
        # print("NEXT ITER!")
        qs = []
        for i in range(5):
            qs.append(asyncio.Queue())
            await qs[i].put(val[i])
            if i == 0:
                await qs[i].put(0)
            print(qs[i]._queue)
        for i in range(5):
            t = asyncio.create_task(run_program(i, qs[i - 1 % 5], qs[i]))
            #if i == 4:
            tasks.append(t)

    await asyncio.gather(*tasks)
    print(max(results))


asyncio.run(main())
