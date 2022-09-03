import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter


def brute_force(components: set[tuple[int, int]],
                n: int = 0,
                total: int = 0,
                length: int = 0) -> tuple[int, int]:
    available = {c for c in components if n in c}

    if len(available) == 0:
        return (length, total)

    return max(
        brute_force(components - {c}, c[0] if c[1] == n else c[1], total +
                    sum(c), length + 1) for c in available)


with open("input") as inf, open("part2.out", "w+") as outf:
    components = {tuple(int(p) for p in i.strip().split("/")) for i in inf}

    outf.write(str(brute_force(components)[1]))
