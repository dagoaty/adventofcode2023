#!/usr/bin/env python3

import sys, os
from functools import reduce
from typing import List

def loadInputs() -> List[List[int]]:
    inputs: List[List[int]] = []
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        for line in f:
            inputs.append([int(x) for x in line.strip().split()])
    return inputs


def findDiffs(nums: List[int]) -> List[int]:
    diffs: List[int] = []
    for i in range(len(nums)-1):
        diffs.append(nums[i+1] - nums[i])
    return diffs


def allZeros(nums: List[int]) -> bool:
    for num in nums:
        if num != 0:
            return False
    return True


def part1() -> int:
    inputs: List[List[int]] = loadInputs()
    newNums: List[int] = []
    for nums in inputs:
        lastInt: List[int] = [nums[-1]]
        while not allZeros(nums):
            nums = findDiffs(nums)
            lastInt.append(nums[-1])
        newNums.append(reduce(lambda x,y: x+y, lastInt[::-1]))
    return reduce(lambda x,y: x+y, newNums)


def part2() -> int:
    inputs: List[List[int]] = loadInputs()
    newNums: List[int] = []
    for nums in inputs:
        firstInt: List[int] = [nums[0]]
        while not allZeros(nums):
            nums = findDiffs(nums)
            firstInt.append(nums[0])
        newNums.append(reduce(lambda x,y: (x-y)*-1, firstInt[::-1]))
    return reduce(lambda x,y: x+y, newNums)


print("Part 1:", part1())
print("Part 2:", part2())