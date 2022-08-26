import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter, deque

with open("input") as inf, open("part2.out", "w+") as outf:
    graph = [[int(n) for n in i.split(" <-> ")[1].split(", ")] for i in inf]
    ng = 0
    nodes = set(range(len(graph)))

    while len(nodes) > 0:
        ng += 1

        q = deque([next(iter(nodes))])
        visited = set()

        while len(q) > 0:
            n = q.pop()

            if n in visited:
                continue

            visited.add(n)
            q.extend(graph[n])

        nodes -= visited

    outf.write(str(ng))
