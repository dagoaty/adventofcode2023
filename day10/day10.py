#!/usr/bin/env python3

import sys, os
from typing import List, Tuple

def loadInputs() -> List[List[str]]:
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        return [list(line.strip()) for line in f]


def findStart(inputs: List[List[str]]) -> Tuple[int, int]:
    return [(x, y) for y in range(len(inputs)) for x in range(len(inputs[y])) if inputs[y][x] == "S"][0]


def findStartBranch(inputs: List[List[str]], startCoords: Tuple[int, int]) -> Tuple[str, int, int]:
    x, y = startCoords
    branches: List[Tuple[str, int, int]] = []
    for d in 'NSEW':
        try:
            branches.append(findNextCoords(inputs, (d, x, y)))
        except ValueError:
            pass
    return branches[0]


def findDirection(inputs: List[List[str]], coords: Tuple[int, int], direction: str) -> str:
    x, y = coords
    if inputs[y][x] in '-|S':
        return direction
    try:
        return {'N': {'F': 'E', 
                      '7': 'W'}, 
                'S': {'L': 'E', 
                      'J': 'W'}, 
                'W': {'L': 'N', 
                      'F': 'S'}, 
                'E': {'J': 'N', 
                      '7': 'S'}}[direction][inputs[y][x]]
    except KeyError:
        raise ValueError("Invalid direction")
        

def findNextCoords(inputs: List[List[str]], coords: Tuple[str, int, int]) -> Tuple[str, int, int]:
    direction, x, y = coords
    if direction == 'N':
        newcoord = (x, y-1)
        newdirection = findDirection(inputs, newcoord, direction)
        return (newdirection, x, y-1)
    elif direction == 'S':
        newcoord = (x, y+1)
        newdirection = findDirection(inputs, newcoord, direction)
        return (newdirection, x, y+1)
    elif direction == 'W':
        newcoord = (x-1, y)
        newdirection = findDirection(inputs, newcoord, direction)
        return (newdirection, x-1, y)
    elif direction == 'E':
        newcoord = (x+1, y)
        newdirection = findDirection(inputs, newcoord, direction)
        return (newdirection, x+1, y)
    raise ValueError("Invalid direction")


def part1() -> int:
    inputs: List[List[str]] = loadInputs()
    startCoords: Tuple[int, int] = findStart(inputs)
    branch: Tuple[str, int, int] = findStartBranch(inputs, startCoords)
    steps: int = 1
    while branch[1:] != startCoords:
        branch = findNextCoords(inputs, branch)
        steps += 1
    return int(steps/2)


def part2() -> int:
    inputs: List[List[str]] = loadInputs()
    print(inputs)
    return 0


print("Part 1:", part1())
#print("Part 2:", part2())