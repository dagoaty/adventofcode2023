#!/usr/bin/env python3

import sys, os
from typing import List
from functools import reduce

def loadInputs() -> List[List[int]]:
    inputs: List[List[int]] = []
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        for line in f:
            thisLine = line.strip().split()[1:]
            thisLine = [int(i) for i in thisLine]
            inputs.append(thisLine)
    return inputs


def findSlowest(length: int, target: int) -> int:
    for speed in range(1, length):
        if (length - speed) * speed > target:
            return speed
    return 0


def findFastest(length: int, target: int) -> int:
    for speed in range(length, 1, -1):
        if (length - speed) * speed > target:
            return speed
    return 0


def part1() -> int:
    inputs: List[List[int]] = loadInputs()
    inputs = list(zip(*inputs))
    waysToWin: List[int] = []
    for race in inputs:
        length, target = race
        slowest = findSlowest(length, target)
        fastest = findFastest(length, target)
        waysToWin.append(fastest-slowest+1)
    return reduce(lambda x, y: x*y, waysToWin)


def part2() -> int:
    inputs: List[List[int]] = loadInputs()
    joinedInputs = [int(''.join(map(str, n))) for n in inputs]
    slowest = findSlowest(joinedInputs[0], joinedInputs[1])
    fastest = findFastest(joinedInputs[0], joinedInputs[1])
    return fastest-slowest+1


print("Part 1:", part1())
print("Part 2:", part2())