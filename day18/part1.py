import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter, defaultdict

with open("input") as inf, open("part1.out", "w+") as outf:
    registers = defaultdict(lambda: 0)
    last_freq = -1
    ip = 0

    def get(r: str):
        return registers[r] if r.isalpha() else int(r)

    instructions = [a.strip().split() for a in inf]

    while len(instructions) > ip >= 0:
        match instructions[ip]:
            case ["snd", x]:
                last_freq = get(x)
            case ["set", x, y]:
                registers[x] = get(y)
            case ["add", x, y]:
                registers[x] = get(x) + get(y)
            case ["mul", x, y]:
                registers[x] = get(x) * get(y)
            case ["mod", x, y]:
                registers[x] = get(x) % get(y)
            case ["rcv", x]:
                if get(x) != 0:
                    outf.write(str(last_freq))
                    exit()
            case ["jgz", x, y]:
                if get(x) > 0:
                    ip += get(y)
                    continue
        ip += 1
