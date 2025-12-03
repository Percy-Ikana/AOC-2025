import time
import argparse
import sys
import copy
from os.path import join
import math

strints = ['9','8','7','6','5','4','3','2','1']

def partOne(data):
    total = 0
    for line in data:
        ind = -1
        for char in strints:
            try:
                ind = line.index(char, 0, len(line)-2)
                break
            except ValueError:
                pass
        ind2 = -1
        for char in strints:
            try:
                ind2 = line.index(char, ind+1)
                break
            except ValueError:
                pass
        total += sum([(int(line[ind])*10), int(line[ind2])])
    return total

def partTwo(data):
    total = 0
    for line in data:
        indexs = [] # This should be 12 long at the end. This would also work for part 1
        line = line.strip()
        for i in range(12, 0, -1):
            for char in strints:
                try:
                    ind = line.index(char, indexs[11-i]+1 if i != 12 else 0, len(line)-i+1)
                    indexs.append(ind)
                    break
                except ValueError:
                    pass
        total += int(''.join([line[ind] for ind in indexs]))
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
