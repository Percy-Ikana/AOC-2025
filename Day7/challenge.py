import time
import argparse
import sys
import copy
from os.path import join
import math
import re
from collections import defaultdict

def partOne(data):
    grid = {(x,y):"^" for y in range(len(data)) for x in range(len(data[0])) if data[y][x] == "^"}
    lasers = set([data[0].index("S")])
    splits = 0
    #For each row
    for y in range(len(data)):
        newLasers = copy.deepcopy(lasers)
        for laser in lasers:
            if (laser,y) in grid.keys():
                newLasers.remove(laser)
                newLasers.add(laser - 1)
                newLasers.add(laser + 1)
                splits+=1
        lasers = newLasers
    return splits

#Part 1 and 2 could easily be combined, but.... oh well. 
def partTwo(data):
    grid = {(x,y):"^" for y in range(len(data)) for x in range(len(data[0])) if data[y][x] == "^"}
    lasers = defaultdict(int)
    #Keep a count of how often each square is entered by other lasers.
    lasers[data[0].index("S")] = 1
    splits = 0
    #For each row
    for y in range(len(data)):
        newLasers = copy.deepcopy(lasers)
        for laser in lasers:
            if (laser,y) in grid.keys():
                del(newLasers[laser])
                newLasers[laser - 1] += lasers[laser]
                newLasers[laser + 1] += lasers[laser]
                splits+=1
        lasers = newLasers
    return sum(lasers.values())

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
    fileName = join(sys.path[0],( "input" if args.test else "TestInput"))
    main(fileName)
