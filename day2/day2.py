#!/usr/bin/env python3

import sys, os
from typing import List, Dict

def loadInputs() -> List[str]:
    inputs: List[str] = []
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        for line in f:
            inputs.append(line.strip())
    return inputs


def processCubes(inputLine: str) -> Dict[str, int]:
    cubes: Dict[str, int] = {}
    inputLine = inputLine.replace(";", ",")

    for cube in inputLine.split(": ")[1].split(", "):
        colour = cube.split()[1]
        number = int(cube.split()[0])

        if colour not in cubes:
            cubes[colour] = number
        elif number > cubes[colour]:
            cubes[colour] = number
    return cubes


def part1() -> int:
    inputs: List[str] = loadInputs()
    MAXCUBES = {'red': 12, 'green': 13, 'blue': 14}
    score: int = 0
    for inputLine in inputs:
        gameNumber = int(inputLine.split()[1][:-1])
        cubes: Dict[str, int] = processCubes(inputLine)
        if all(cubes[colour] <= MAXCUBES[colour] for colour in cubes):
            score += gameNumber
    return score
        

def part2() -> int:
    inputs: List[str] = loadInputs()
    score: int = 0
    for inputLine in inputs:
        cubes: Dict[str, int] = processCubes(inputLine)
        product = 1
        for colour in cubes:
            product *= cubes[colour]
        score += product
    return score


print("Part 1:", part1())
print("Part 2:", part2())