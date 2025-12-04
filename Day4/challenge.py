import time
import argparse
import sys
import copy
from os.path import join
import math

def partOne(data):
    grid = {(x,y):"@"  for y in range(len(data)) for x in range(len(data[y])) if data[y][x] == "@"}
    total = 0
    for point in grid.keys():
        count = 0
        for x in [point[0]-1,point[0],point[0]+1]:
            for y in [point[1]-1,point[1],point[1]+1]:
                if x != point[0] or y!=point[1]:
                    if (x,y) in grid.keys():
                        count +=1
        if count < 4:
            total+=1
    return total



def partTwo(data):
    grid = {(x,y):"@"  for y in range(len(data)) for x in range(len(data[y])) if data[y][x] == "@"}
    total = 0
    rolls = len(grid.keys())-1
    while len(grid.keys()) != rolls:
        toremove = []
        rolls = len(grid.keys())
        for point in grid.keys():
            count = 0
            for x in [point[0]-1,point[0],point[0]+1]:
                for y in [point[1]-1,point[1],point[1]+1]:
                    if x != point[0] or y!=point[1]:
                        if (x,y) in grid.keys():
                            count +=1
            if count < 4:
                toremove.append(point)
        for point in toremove:
            del(grid[point])
        total += len(toremove)
        
    return total


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
