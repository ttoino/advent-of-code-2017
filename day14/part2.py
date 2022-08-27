import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter, deque


def add_tuples(a, b):
    return tuple(i + j for i, j in zip(a, b))


def knot_hash(inp: str):
    lengths = [ord(i) for i in inp] + [17, 31, 73, 47, 23]

    l = list(range(256))
    skip_size = 0
    index = 0

    for _ in range(64):
        for i in lengths:
            i = int(i)

            l[:i] = l[:i][::-1]

            l = l[(i + skip_size) % 256:] + l[:(i + skip_size) % 256]

            index += i + skip_size
            skip_size += 1

    index %= 256
    l = l[-index:] + l[:-index]

    return "".join(f"{ft.reduce(op.xor, c):02x}" for c in mit.chunked(l, 16))


with open("input") as inf, open("part2.out", "w+") as outf:
    inp = inf.readline().strip()
    grid = list(
        map(
            int, "".join(f"{int(x, base=16):04b}" for i in range(128)
                         for x in knot_hash(f"{inp}-{i}"))))

    used = set(
        (x, y) for x in range(128) for y in range(128) if grid[x + y * 128])
    regions = 0

    while len(used) > 0:
        regions += 1
        q = deque((next(iter(used)),))

        while len(q) > 0:
            p = q.pop()

            if p not in used:
                continue

            used.remove(p)

            for t in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                q.append(add_tuples(p, t))

    outf.write(str(regions))
