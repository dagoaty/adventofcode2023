#!/usr/bin/env python3

import sys, os
from typing import List, Dict

def part1() -> int:
    # Read input file into inputs variable
    inputs: List[str] = []
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        for line in f:
            inputs.append(line.strip())

    # Loop through inputs. Find the first and last number on each line
    # and add it to an array called values
    values: List[int] = []
    for input in inputs:
        number: List[str] = []
        for letter in input:
            if letter.isnumeric():
                number.append(letter)
                break
        for letter in reversed(input):
            if letter.isnumeric():
                number.append(letter)
                break
        
        # Join the two numbers in number, convert it to an integer
        # and add it to values
        values.append(int("".join([number[0], number[1]])))
        

    # Loop through values and sum all the numbers
    sum = 0
    for value in values:
        sum += value
    return sum


def part2() -> int:
    # Read input file into inputs variable
    inputs: List[str] = []
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        for line in f:
            inputs.append(line.strip())

    wordNumbers = [
        "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
    ]
    numbers = [
        1, 2, 3, 4, 5, 6, 7, 8, 9
    ]
    values: List[int] = []

    # For each line in inputs, loop through and find the index position of
    # and wordNumbers or numbers in the line.
    # Return the lowest and highest index position for each line
    for input in inputs:
        nums: Dict[int, int] = {}
        for wordNumber in wordNumbers:
            if wordNumber in input:
                # Add all the positions of wordNumber in input to nums
                i = 0
                while i < len(input):

                    pos = input.find(wordNumber, i)
                    if pos > -1:
                        nums[pos] = numbers[wordNumbers.index(wordNumber)]
                        i = pos + len(wordNumber)
                    else:
                        break

        for number in numbers:
            if str(number) in input:
                # Add all positions of number in input to nums
                i = 0
                while i < len(input):
                    pos = input.find(str(number), i)
                    if pos > -1:
                        nums[pos] = int(number)
                        i = pos + 1
                    else:
                        break
        

        # Join the value of the lowest and highest index in nums
        # and add as an into to values
        values.append(int("".join([str(nums[min(nums)]), str(nums[max(nums)])])))

    # Loop through values and sum all the numbers
    sum = 0
    for value in values:
        sum += value
    return sum
        

print("Part 1:", part1())
print("Part 2:", part2())