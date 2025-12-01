import time
import argparse
import sys
import copy
from os.path import join

def partOne(data):
    inputs = data
    position = 50
    count = 0
    for line in inputs:
        if line[0] == "L":
            position = (position - int(line[1:]))%100
        else:
            position = (position + int(line[1:]))%100
        if position == 0:
            count += 1
    return count

def partTwo(data):
    inputs = data
    position = 50
    oldpos = 50
    count = 0
    for line in inputs:
        mod = 1
        if line[0] == "L":
            mod = -1
        for click in range(int(line[1:])):
            position = position + mod
            position = position % 100
            if position == 0: count += 1

    return count

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