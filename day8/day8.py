#!/usr/bin/env python3

import sys, os, math, functools
from typing import List, Dict

def loadInputs() -> List[str]:
    inputs: List[str] = []
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        inputs = f.read().strip().split("\n\n")
    return inputs


def lcm(a: int, b:int ):
    print(abs(a*b), math.gcd(a, b), abs(a*b) // math.gcd(a, b))
    return abs(a*b) // math.gcd(a, b)


def part1() -> int:
    inputs: List[str] = loadInputs()
    instructions: List[str] = list(inputs[0].replace('L', '0').replace('R', '1'))
                                   
    locations: Dict[str, tuple[str]] = {}
    for loc in [el.split(" = ") for el in inputs[1].split("\n")]:
        locations[loc[0]] = tuple(loc[1].replace(')','').replace('(','').split(", "))

    myPos = "AAA"
    count = 0
    while myPos != "ZZZ":
        thisInst = instructions.pop(0)
        myPos = locations[myPos][int(thisInst)]
        count += 1
        instructions.append(thisInst)
    return count


def part2() -> int:
    inputs: List[str] = loadInputs()
    instructions: List[str] = list(inputs[0].replace('L', '0').replace('R', '1'))
                                   
    locations: Dict[str, tuple[str]] = {}
    for loc in [el.split(" = ") for el in inputs[1].split("\n")]:
        locations[loc[0]] = tuple(loc[1].replace(')','').replace('(','').split(", "))

    myPoss: List[str] = [p for p in locations if p.endswith('A')]
    posSteps: List[int] = []
    for myPos in myPoss:
        count = 0
        while not myPos.endswith('Z'):
            thisInst = instructions.pop(0)
            myPos = locations[myPos][int(thisInst)]
            count += 1
            instructions.append(thisInst)
        posSteps.append(count)
    return functools.reduce(lcm, posSteps)


print("Part 1:", part1())
print("Part 2:", part2())