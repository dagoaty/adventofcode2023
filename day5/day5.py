#!/usr/bin/env python3

import sys, os

def loadInputs():
    inputs = []
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        for line in f:
            inputs.append(line.strip())

    for input_line in inputs:
        # If the input line starts with "seeds" we save the values to the seeds list
        if input_line.startswith("seeds"):
            seeds = input_line.split(": ")[1:][0].split()
            seeds = [int(seed) for seed in seeds]
        # Else if the input line contains "seed-to-soil map:" we read each line into the map dict until reaching a blank line
        elif input_line.startswith("seed-to-soil map:"):
            seedToSoilMap = {}
            for line in inputs[inputs.index(input_line) + 1:]:
                if line == "":
                    break
                soil, seed, rangeLength = line.split()
                seedToSoilMap[int(seed)] = (int(soil)-int(seed), int(rangeLength))
        elif input_line.startswith("soil-to-fertilizer map:"):
            soilToFertilizerMap = {}
            for line in inputs[inputs.index(input_line) + 1:]:
                if line == "":
                    break
                fertilizer, soil, rangeLength = line.split()
                soilToFertilizerMap[int(soil)] = (int(fertilizer)-int(soil), int(rangeLength))
        elif input_line.startswith("fertilizer-to-water map:"):
            fertilizerToWaterMap = {}
            for line in inputs[inputs.index(input_line) + 1:]:
                if line == "":
                    break
                water, fertilizer, rangeLength = line.split()
                fertilizerToWaterMap[int(fertilizer)] = (int(water)-int(fertilizer), int(rangeLength))
        elif input_line.startswith("water-to-light map:"):
            waterToLightMap = {}
            for line in inputs[inputs.index(input_line) + 1:]:
                if line == "":
                    break
                light, water, rangeLength = line.split()
                waterToLightMap[int(water)] = (int(light)-int(water), int(rangeLength))
        elif input_line.startswith("light-to-temperature map:"):
            lightToTemperatureMap = {}
            for line in inputs[inputs.index(input_line) + 1:]:
                if line == "":
                    break
                temperature, light, rangeLength = line.split()
                lightToTemperatureMap[int(light)] = (int(temperature)-int(light), int(rangeLength))
        elif input_line.startswith("temperature-to-humidity map:"):
            temperatureToHumidityMap = {}
            for line in inputs[inputs.index(input_line) + 1:]:
                if line == "":
                    break
                humidity, temperature, rangeLength = line.split()
                temperatureToHumidityMap[int(temperature)] = (int(humidity)-int(temperature), int(rangeLength))
        elif input_line.startswith("humidity-to-location map:"):
            humidityToLocationMap = {}
            for line in inputs[inputs.index(input_line) + 1:]:
                if line == "":
                    break
                location, humidity, rangeLength = line.split()
                humidityToLocationMap[int(humidity)] = (int(location)-int(humidity), int(rangeLength))
    return seeds, seedToSoilMap, soilToFertilizerMap, fertilizerToWaterMap, waterToLightMap, lightToTemperatureMap, temperatureToHumidityMap, humidityToLocationMap


def seedToLocation(seed, inputs):
    seedToSoilMap, soilToFertilizerMap, fertilizerToWaterMap, waterToLightMap, lightToTemperatureMap, temperatureToHumidityMap, humidityToLocationMap = inputs[1:]
    soil = seed
    for k in seedToSoilMap:
        if seed in range(k, k+seedToSoilMap[k][1]):
            soil = seed+seedToSoilMap[k][0]
            break

    fertilizer = soil
    for k in soilToFertilizerMap:
        if soil in range(k, k+soilToFertilizerMap[k][1]):
            fertilizer = soil+soilToFertilizerMap[k][0]
            break

    water = fertilizer
    for k in fertilizerToWaterMap:
        if fertilizer in range(k, k+fertilizerToWaterMap[k][1]):
            water = fertilizer+fertilizerToWaterMap[k][0]
            break

    light = water
    for k in waterToLightMap:
        if water in range(k, k+waterToLightMap[k][1]):
            light = water+waterToLightMap[k][0]
            break

    temperature = light
    for k in lightToTemperatureMap:
        if light in range(k, k+lightToTemperatureMap[k][1]):
            temperature = light+lightToTemperatureMap[k][0]
            break

    humidity = temperature
    for k in temperatureToHumidityMap:
        if temperature in range(k, k+temperatureToHumidityMap[k][1]):
            humidity = temperature+temperatureToHumidityMap[k][0]
            break

    location = humidity
    for k in humidityToLocationMap:
        if humidity in range(k, k+humidityToLocationMap[k][1]):
            location = humidity+humidityToLocationMap[k][0]
            break

    return location

def part1():
    inputs = loadInputs()
    seeds = inputs[0]
    return min(map(lambda seed: seedToLocation(seed, inputs), seeds))


def part2():
    inputs = loadInputs()
    seeds = zip(inputs[0][::2], inputs[0][1::2])
    locations = []
    for start, end in seeds:
        locations.append(min(map(lambda seed: seedToLocation(seed, inputs), range(start, start+end))))
    return sorted(locations)[0]


print("Part 1:", part1())
print("Part 2:", part2())