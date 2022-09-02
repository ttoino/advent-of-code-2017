import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter, defaultdict, deque

with open("input") as inf, open("part2.out", "w+") as outf:
    registers = [defaultdict(lambda: 0), defaultdict(lambda: 1)]
    ip = [0, 0]
    instructions = [a.strip().split() for a in inf]
    pipes = [deque(), deque()]
    sent = [0, 0]

    def process(id: 0 | 1):
        def get(r: str):
            return registers[id][r] if r.isalpha() else int(r)

        while len(instructions) > ip[id] >= 0:
            match instructions[ip[id]]:
                case ["snd", x]:
                    pipes[id - 1].append(get(x))
                    sent[id] += 1
                case ["set", x, y]:
                    registers[id][x] = get(y)
                case ["add", x, y]:
                    registers[id][x] = get(x) + get(y)
                case ["mul", x, y]:
                    registers[id][x] = get(x) * get(y)
                case ["mod", x, y]:
                    registers[id][x] = get(x) % get(y)
                case ["rcv", x]:
                    if len(pipes[id]) == 0:
                        return False
                    else:
                        registers[id][x] = pipes[id].popleft()
                case ["jgz", x, y]:
                    if get(x) > 0:
                        ip[id] += get(y)
                        continue
            ip[id] += 1
        
        return True

    while True:
        if (process(0) & process(1)) or len(pipes[0]) == len(pipes[1]) == 0:
            outf.write(str(sent[1]))
            break
