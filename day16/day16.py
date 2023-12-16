#!/usr/bin/env python3

import sys, os
from typing import List, Tuple, Dict

def loadInputs() -> List[List[str]]:
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        return [list(line.strip()) for line in f]


def getNewLocation(inputs: List[List[str]], beam: Tuple[int, int, str]) -> List[Tuple[int, int, str]]:
    x, y, direction = beam
    if direction == 'E':
        if x + 1 >= len(inputs[0]):
            return []
        if inputs[y][x + 1] == '/':
            direction = 'N'
        elif inputs[y][x + 1] == '\\':
            direction = 'S'
        elif inputs[y][x + 1] == '|':
            direction = 'NS'
        if len(direction) == 2:
            return [(x + 1, y, direction[0]), (x + 1, y, direction[1])]
        else:
            return [(x + 1, y, direction)]
    elif direction == 'W':
        if x - 1 < 0:
            return []
        if inputs[y][x - 1] == '/':
            direction = 'S'
        elif inputs[y][x - 1] == '\\':
            direction = 'N'
        elif inputs[y][x - 1] == '|':
            direction = 'NS'
        if len(direction) == 2:
            return [(x - 1, y, direction[0]), (x - 1, y, direction[1])]
        else:
            return [(x - 1, y, direction)]
    elif direction == 'N':
        if y - 1 < 0:
            return []
        if inputs[y - 1][x] == '/':
            direction = 'E'
        elif inputs[y - 1][x] == '\\':
            direction = 'W'
        elif inputs[y - 1][x] == '-':
            direction = 'EW'
        if len(direction) == 2:
            return [(x, y - 1, direction[0]), (x, y - 1, direction[1])]
        else:
            return [(x, y - 1, direction)]
    elif direction == 'S':
        if y + 1 >= len(inputs):
            return []
        if inputs[y + 1][x] == '/':
            direction = 'W'
        elif inputs[y + 1][x] == '\\':
            direction = 'E'
        elif inputs[y + 1][x] == '-':
            direction = 'EW'
        if len(direction) == 2:
            return [(x, y + 1, direction[0]), (x, y + 1, direction[1])]
        else:
            return [(x, y + 1, direction)]
    return []


def getStartPositions(inputs: List[List[str]]) -> List[Tuple[int, int, str]]:
    startPositions: List[Tuple[int, int, str]] = []
    for y in range(len(inputs)):
        startPositions.append((-1, y, 'E'))
        startPositions.append((len(inputs[0]), y, 'W'))
    for x in range(len(inputs[0])):
        startPositions.append((x, -1, 'S'))
        startPositions.append((x, len(inputs), 'N'))
    return startPositions


def part1() -> int:
    inputs: List[List[str]] = loadInputs()
    beams: List[Tuple[int, int, str]] = [(-1, 0, 'E')]
    energised: Dict[Tuple[int, int, str], int] = {}
    while beams:
        newLocations = getNewLocation(inputs, beams.pop(0))
        for loc in newLocations:
            if loc not in energised:
                beams.append(loc)
                energised[loc] = 1
    return len(set([x[:2] for x in energised.keys()]))


def part2() -> int:
    inputs: List[List[str]] = loadInputs()
    pathLengths: List[int] = []
    startPositions: List[Tuple[int, int, str]] = getStartPositions(inputs)
    for startPos in startPositions:
        beams: List[Tuple[int, int, str]] = [startPos]
        energised: Dict[Tuple[int, int, str], int] = {}
        while beams:
            newLocations = getNewLocation(inputs, beams.pop(0))
            for loc in newLocations:
                if loc not in energised:
                    beams.append(loc)
                    energised[loc] = 1
        pathLengths.append(len(set([x[:2] for x in energised.keys()])))
    return max(pathLengths)


print("Part 1:", part1())
print("Part 2:", part2())