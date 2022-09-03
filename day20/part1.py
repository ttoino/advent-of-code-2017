import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    p = re.compile(
        r"p=<(-?\d+,-?\d+,-?\d+)>, v=<(-?\d+,-?\d+,-?\d+)>, a=<(-?\d+,-?\d+,-?\d+)>"
    )
    particles = [
        tuple(tuple(int(n)
                    for n in g.split(","))
              for g in p.match(i).groups())
        for i in inf
    ]

    t = 1000000
    particles = [
        tuple(p + v * t + a / 2 * t * t
              for p, v, a in zip(p, v, a))
        for p, v, a in particles
    ]

    outf.write(
        str(min((sum(map(abs, p)), i) for i, p in enumerate(particles))[1]))
