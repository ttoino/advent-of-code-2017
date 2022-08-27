import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter


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


with open("input") as inf, open("part1.out", "w+") as outf:
    inp = inf.readline().strip()
    outf.write(
        str(
            sum(
                map(
                    int, "".join(f"{int(x, base=16):04b}" for i in range(128)
                                 for x in knot_hash(f"{inp}-{i}"))))))
