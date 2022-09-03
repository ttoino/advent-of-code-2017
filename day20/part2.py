import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter


def add_tuples(a, b):
    return tuple(i + j for i, j in zip(a, b))


with open("input") as inf, open("part2.out", "w+") as outf:
    p = re.compile(
        r"p=<(-?\d+,-?\d+,-?\d+)>, v=<(-?\d+,-?\d+,-?\d+)>, a=<(-?\d+,-?\d+,-?\d+)>"
    )
    particles = [
        list(tuple(int(n)
                   for n in g.split(","))
             for g in p.match(l).groups())
        for l in inf
    ]

    for i in range(10000):
        print(i, end="\r")
        pos = Counter()
        for p in particles:
            p[1] = add_tuples(p[1], p[2])
            p[0] = add_tuples(p[0], p[1])
            pos[p[0]] += 1

        particles = [p for p in particles if pos[p[0]] == 1]

    outf.write(str(len(particles)))
