import time
import argparse
import sys
import copy
from os.path import join
import math

def partOne(data):
    ranges = [product.split('-') for product in data[0].split(',')]
    jokeID=[]
    for start, end  in ranges:
        for id in range(int(start), int(end)+1):
            #split the int string in half and compare
            strID=str(id)
            half=len(strID)//2+len(strID)%2
            if strID[:half]==strID[half:]:
                jokeID.append(id)
    return sum(jokeID)

def partTwo(data):
    ranges = [product.split('-') for product in data[0].split(',')]
    jokeID=[]
    for start, end  in ranges:
        for id in range(int(start), int(end)+1):
            #split the int string in half and comp>
            strID=str(id)
            half=len(strID)//2+len(strID)%2
            for sub in range(half+1):
                occ= strID.count(strID[:sub])
                if occ  >= 2 and occ*sub == len(strID):
                    jokeID.append(id)
                    break
    return sum(jokeID)


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
