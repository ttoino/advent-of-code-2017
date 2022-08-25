import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    state = tuple(int(i) for i in inf.readline().strip().split())
    states = {}

    for step in it.count():
        if state in states:
            outf.write(str(step - states[state]))
            break
        states[state] = step

        i, n = max(enumerate(state), key=lambda x: (x[1], -x[0]))

        state = list(state)
        state[i] = 0

        for j in range(1, n + 1):
            state[(i + j) % len(state)] += 1

        state = tuple(state)
