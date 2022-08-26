import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter, deque

with open("input") as inf, open("part1.out", "w+") as outf:
    graph = [[int(n) for n in i.split(" <-> ")[1].split(", ")] for i in inf]

    q = deque([0])
    visited = set()

    while len(q) > 0:
        n = q.pop()

        if n in visited:
            continue

        visited.add(n)
        q.extend(graph[n])

    outf.write(str(len(visited)))
