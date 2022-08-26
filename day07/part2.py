import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter


def check_weight(towers, tower):
    weight, children = towers[tower]

    if children is None:
        return int(weight)

    weights = [check_weight(towers, c) for c in children]
    counter = Counter(weights)
    for k, v in counter.items():
        if v == 1:
            for w, c in zip(weights, children):
                if w == k:
                    out(
                        str(
                            int(towers[c][0]) - k +
                            counter.most_common(1)[0][0]))
                    exit()

    return int(weight) + sum(weights)


with open("input") as inf, open("part2.out", "w+") as outf:
    p = re.compile(r"(\w+) \((\d+)\)(?: -> ((?:\w+,? ?)+))?")

    towers = [p.match(i).groups() for i in inf]

    t = list(zip(*[g for g in towers if g[2] is not None]))
    names = set(t[0])
    children = set(sum((i.split(", ") for i in t[2]), []))
    root = next(iter(names - children))

    towers = {g[0]: (g[1], g[2] and g[2].split(", ")) for g in towers}

    global out
    out = outf.write

    check_weight(towers, root)
