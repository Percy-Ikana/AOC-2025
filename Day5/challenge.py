import time
import argparse
import sys
import copy
from os.path import join
import math

def partOne(data):
    rangeList, ingredients = data.split("\n\n")
    ranges = []
    ingredients = [int(ing) for ing in ingredients.split("\n")]
    for rangeSet in rangeList.split("\n"):
        low, high = rangeSet.split("-")
        ranges.append(range(int(low), int(high)+1))
    goodIngredients = []
    for ingredient in ingredients:
        for rng in ranges:
            if ingredient in rng:
                goodIngredients.append(ingredient)
                break
    return len(goodIngredients)

def partTwo(data):
    rangeList, ingredients = data.split("\n\n")
    ranges = []
    for rangeSet in rangeList.split("\n"):
        low, high = rangeSet.split("-")
        ranges.append([int(low), int(high)])
    #Sort Ranges
    ranges.sort()
    merged = []
    for start, end in ranges:
        if len(merged) == 0 or merged[-1][1] < start - 1:
            #This is a new range
            merged.append([start, end])
        else:
            #This range overlaps the previous, combine them. MAx to take the farthest one in case one range is wholly contained.
            merged[-1][1] = max(merged[-1][1], end)
    total = 0
    for start, end in merged:
        total += len(range(start, end+1))
    return total

#this would work, but probably take more ram than my laptop has lol. 
def partTwoOG(data):
    rangeList, ingredients = data.split("\n\n")
    ranges = set()
    for rangeSet in rangeList.split("\n"):
        low, high = rangeSet.split("-")
        ranges = ranges.union(set(range(int(low), int(high)+1)))
    
    return len(ranges)


def main(fileName):
    data = []
    with open(fileName, 'r') as file:
        data = file.read()

    start_time = time.time()
    
    print(partOne(data))
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    print(partTwo(data))
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--test', help='use the test input or not', 
                        action='store_false', required=False)
    args = parser.parse_args()
    fileName =join(sys.path[0],( "input" if args.test else "TestInput"))
    main(fileName)
