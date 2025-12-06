import time
import argparse
import sys
import copy
from os.path import join
import math
import re

def partOne(data):
    grid = [line.rstrip().split() for line in data[:-1]]
    grid.append(data[-1].split())
    newGrid = {}
    for x in range(len(grid[0])):
        newGrid[x] = []
        for y in range(len(grid)):
            if y == len(grid) - 1:
                newGrid[x].append(grid[y][x])
            else:
                newGrid[x].append(int(grid[y][x]))
    totals = []
    for problem in newGrid.values():
        op = problem[-1]
        if op == '+':
            totals.append(sum(problem[:-1]))
        if op == '*':
            totals.append(math.prod(problem[:-1]))
    return sum(totals)

def partTwo(data):
    op = data[-1].split()
    splitVals = []
    x = 1
    while x < len(data[-1]):
        if data[-1][x] == '*' or data[-1][x] == '+' or data[-1][x] == '\n':
            splitVals.append(x-sum(splitVals))
        x+=1
    splitVals.append(x-sum(splitVals)+1)
    
    problems = []
    operands = len(data[:-1])
    for x in range(len(splitVals)):
        start = sum(splitVals[:x])
        end = sum(splitVals[:x])+splitVals[x]
        ops = [vals[start:end] for vals in data[:-1]]
        newops = []
        for y in range(len(ops[0])-2, -1, -1):
            newops.append(int("".join([opval[y] for opval in ops])))
        newops.append(op[x])
        problems.append(newops)
    totals = []
    for problem in problems:
        op = problem[-1]
        if op == '+':
            totals.append(sum(problem[:-1]))
        if op == '*':
            totals.append(math.prod(problem[:-1]))
    return sum(totals)



def main(fileName):
    data = []
    with open(fileName, 'r') as file:
        data = file.readlines()

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
