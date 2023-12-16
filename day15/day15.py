#!/usr/bin/env python3

import sys, os, re
from functools import reduce
from typing import List, Dict

def loadInputs() -> List[str]:
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        return [line.strip().split(',') for line in f][0]


def hashChar(n: int, c: str) -> int:
    return ((n + ord(c)) * 17) % 256


def updateBucket(buckets: Dict[int, Dict[str,str]], action: str, string: str, number: str) -> Dict[int, Dict[str,str]]:
    bucket = reduce(hashChar, string, 0)
    if action == "=":
        if bucket not in buckets:
            buckets[bucket] = {string: number}
        else:
            buckets[bucket][string] = number
    elif action == "-" and bucket in buckets and string in buckets[bucket]:
        del buckets[bucket][string]
        if len(buckets[bucket]) == 0:
            del buckets[bucket]
    return buckets


def calcFocusPower(buckets: Dict[int, Dict[str,str]]) -> int:
    focusPower: List[int] = []
    for bucket in buckets:
        for n, v in enumerate(buckets[bucket]):
            thisScore = bucket+1
            thisScore *= int(buckets[bucket][v]) * (n + 1)
            focusPower.append(thisScore)
    return sum(focusPower)
        


def part1() -> int:
    inputs: List[str] = loadInputs()
    results: List[int] = []
    for inputStr in inputs:
        results.append(reduce(hashChar, inputStr, 0))
    return sum(results)


def part2() -> int:
    inputs: List[str] = loadInputs()
    buckets = {}
    for inputStr in inputs:
        match = re.search(r"[=-]", inputStr)
        assert match is not None
        (start, end) = match.span()
        buckets = updateBucket(buckets, inputStr[start:end], inputStr[0:start], inputStr[end:])
    return calcFocusPower(buckets)


print("Part 1:", part1())
print("Part 2:", part2())