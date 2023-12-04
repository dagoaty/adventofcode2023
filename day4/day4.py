#!/usr/bin/env python3

import sys, os
from typing import List, Dict

def loadInputs() -> List[str]:
    inputs: List[str] = []
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        for line in f:
            inputs.append(line.strip())
    return inputs


def processInputs(inputs: List[str]) -> Dict[int, List[List[int]]]:
    processedInputs: Dict[int, List[List[int]]] = {}
    for line in inputs:
        lineParts: List[str] = line.split(": ")
        cardNo: int = int(lineParts[0].split()[1])
        lineSides = lineParts[1].split(" | ")
        winningNos: List[int] = [int(x) for x in lineSides[0].split()]
        myNos: List[int] = [int(x) for x in lineSides[1].split()]
        processedInputs[cardNo] = [winningNos, myNos]
    return processedInputs


def perCardWinners(games: Dict[int, List[List[int]]]) -> Dict[int, List[int]]:
    scores: Dict[int, List[int]] = {}
    for game in games:
        winningNos: List[int] = games[game][0]
        myNos: List[int] = games[game][1]
        intersection: List[int] = [int(x) for x in winningNos if x in myNos]
        scores[game] = intersection
    return scores


def part1() -> int:
    inputs: List[str] = loadInputs()
    processedInputs: Dict[int, List[List[int]]] = processInputs(inputs)
    gameScores = perCardWinners(processedInputs)
    score = 0
    for game in gameScores:
        thisScore = 0
        if len(gameScores[game]) > 0:
            thisScore = 1
            thisScore = thisScore << len(gameScores[game])-1
        score += thisScore
    return score


def part2() -> int:
    inputs: List[str] = loadInputs()
    processedInputs: Dict[int, List[List[int]]] = processInputs(inputs)
    gameWinners: Dict[int, List[int]] = perCardWinners(processedInputs)

    gameScores: Dict[int, int] = {}
    for game in gameWinners:
        gameScores[game] = len(gameWinners[game])
    
    gameCardCount: Dict[int, int] = {}
    for game in processedInputs:
        gameCardCount[game] = 1

    for i in range(1,len(gameScores)+1):
        for n in range(1,gameScores[i]+1):
            gameCardCount[i+n] += gameCardCount[i]

    score = 0
    for game in gameCardCount:
        score += gameCardCount[game]
    return score


print("Part 1:", part1())
print("Part 2:", part2())