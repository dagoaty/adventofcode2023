#!/usr/bin/env python3

import sys, os
from typing import List, Tuple

def loadInputs() -> List[List[str]]:
    inputs: List[List[str]] = []
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        for line in f:
            inputs.append(list(line.strip()))
    return inputs


def findSymbols(inputs: List[List[str]]) -> List[Tuple[int, int]]:
    symbols: List[Tuple[int, int]] = []
    NONSYMBOLS = [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    row = 0
    for input_line in inputs:
        col=0
        for symbol in input_line:
            if symbol not in NONSYMBOLS:
                pos = (col, row)
                symbols.append(pos)
            col += 1
        row += 1
    return symbols
        

def findNumbers(inputs: List[List[str]]) -> List[Tuple[int, List[Tuple[int, int]]]]:
    row = 0
    foundNums: List[Tuple[int, List[Tuple[int, int]]]] = []
    for input_line in inputs:
        input_line.append(".")
        num: List[str] = []
        pos = (-1, -1)
        col = 0
        for char in input_line:
            if char.isnumeric():
                num.append(char)
                if pos == (-1, -1):
                    pos = (col, row)
            else:
                if num != []:
                    boundary: List[Tuple[int, int]] = []
                    minX = pos[0]-1
                    maxX = pos[0]+len(num)
                    minY = pos[1]-1
                    maxY = pos[1]+1
                    boundary.append((minX, pos[1]))
                    boundary.append((maxX, pos[1]))
                    while minX <= maxX:
                        boundary.append((minX, minY))
                        boundary.append((minX, maxY))
                        minX += 1
                    foundNums.append((int("".join(num)), boundary))
                    num = []
                    pos = (-1, -1)
            col += 1
        row += 1
    return foundNums


def findValidNumbers(symbols: List[Tuple[int, int]], numbers: List[Tuple[int, List[Tuple[int, int]]]] ) -> List[int]:
    validNumbers: List[int] = []
    for number in numbers:
        isValid = False
        for symbol in symbols:
            if symbol in number[1]:
                isValid = True
                break
        if isValid:
            validNumbers.append(number[0])
    return validNumbers


def findGears(inputs: List[List[str]]) -> List[Tuple[int, int]]:
    gears: List[Tuple[int, int]] = []
    row = 0
    for input_line in inputs:
        col=0
        for symbol in input_line:
            if symbol == '*':
                pos = (col, row)
                gears.append(pos)
            col += 1
        row += 1
    return gears


def findGearRatios(numbers: List[Tuple[int, List[Tuple[int, int]]]], gears: List[Tuple[int, int]]) -> List[int]:
    gearRatios: List[int] = []
    for gear in gears:
        thisRatio: List[int] = []
        for number in numbers:
            if gear in number[1]:
                thisRatio.append(number[0])
        if len(thisRatio) == 2:
            gearRatios.append(thisRatio[0] * thisRatio[1])
    return gearRatios


def part1() -> int:
    inputs: List[List[str]] = loadInputs()
    symbols = findSymbols(inputs)
    numbers = findNumbers(inputs)
    validNumbers: List[int] = findValidNumbers(symbols, numbers)
    sum = 0
    for number in validNumbers:
        sum += number
    return sum


def part2() -> int:
    inputs: List[List[str]] = loadInputs()
    numbers = findNumbers(inputs)
    gears = findGears(inputs)
    gearRatios: List[int] = findGearRatios(numbers, gears)
    sum = 0
    for ratio in gearRatios:
        sum += ratio
    return sum


print("Part 1:", part1())
print("Part 2:", part2())