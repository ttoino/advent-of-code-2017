import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter


def rotate_and_flip(pattern):
    for p in rotate(pattern):
        yield tuple("".join(l) for l in p)
        yield tuple("".join(l) for l in reversed(p))
        yield tuple("".join(reversed(l)) for l in p)


def rotate(pattern):
    yield pattern

    for i in range(3):
        pattern = list(zip(*reversed(pattern)))
        yield pattern


with open("input") as inf, open("part2.out", "w+") as outf:
    instructions = {
        k: tuple(i.strip().split(" => ")[1].split("/")) for i in inf
        for k in rotate_and_flip(i.split(" => ")[0].split("/"))
    }

    pattern = ".#...####"
    size = 3

    for i in range(18):
        t = 2 + (size % 2)
        a = size // t
        pieces = (
            tuple("".join(i)
                  for i in l)
            for l in sum((list(zip(*mit.chunked(l, a)))
                          for l in mit.chunked(mit.chunked(pattern, t), size)),
                         start=[]))

        new_pieces = list(instructions[p] for p in pieces)
        size += size // t

        pattern = "".join(
            "".join(i) for l in mit.chunked(new_pieces, a) for i in zip(*l))

        assert len(pattern) == size * size

    outf.write(str(pattern.count("#")))
