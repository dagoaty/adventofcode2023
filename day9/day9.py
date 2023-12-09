#!/usr/bin/env python3

import sys, os
from functools import reduce
from typing import List

def loadInputs() -> List[List[int]]:
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        return [[int(x) for x in line.strip().split()] for line in f]


def findDiffs(nums: List[int]) -> List[int]:
    return [nums[i+1] - nums[i] for i in range(len(nums)-1)]


def allZeros(nums: List[int]) -> bool:
    return all(num == 0 for num in nums)


def part1() -> int:
    inputs: List[List[int]] = loadInputs()
    newNums: List[int] = []
    for nums in inputs:
        lastInt: List[int] = [nums[-1]]
        while not allZeros(nums):
            nums = findDiffs(nums)
            lastInt.append(nums[-1])
        newNums.append(sum(lastInt))
    return sum(newNums)


def part2() -> int:
    inputs: List[List[int]] = loadInputs()
    newNums: List[int] = []
    for nums in inputs:
        firstInt: List[int] = [nums[0]]
        while not allZeros(nums):
            nums = findDiffs(nums)
            firstInt.append(nums[0])
        newNums.append(reduce(lambda x,y: (x-y)*-1, firstInt[::-1]))
    return sum(newNums)


print("Part 1:", part1())
print("Part 2:", part2())