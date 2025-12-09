import time
import argparse
import sys
import copy
from os.path import join
import math

def partOne(data):
    boxes = (set({(int(x),int(y), int(z)) for line in data for x, y, z in [line.strip().split(',')]}))
    cons = []
    distances = {}
    distbydist = {}
    for box in boxes:
        distances[box] = {}
        close = (-1,-1,-1)
        dist = 10000000000000000000
        for possCon in boxes:
            #calc distance
            if box == possCon:
                pass
            else:
                dist = math.sqrt((possCon[0] - box[0])**2 + (possCon[1] - box[1])**2 + (possCon[2] - box[2])**2)
                distances[box][possCon] = dist
                distbydist[dist] = (box, possCon)
                if distances[box][possCon] < dist:
                    dist = distances[box][possCon]
                    close = possCon
    sortDistances = sorted(distbydist.keys())
    closedist = 0
    for x in range(1000):
        boxes = distbydist[sortDistances[x]]
        added = 0
        for connections in cons:
                if boxes[0] in connections or boxes[1] in connections:
                    connections.add(boxes[0])
                    connections.add(boxes[1])
                    added = 1
                    break
        if not added:
            cons.append(set({boxes[0], boxes[1]}))
        closedist = dist
    oldcons = 0
    changed = 1
    while changed:
        changed = 0
        for con in cons:
            #see if it belongs in another set
            for subcon in cons:
                if con != subcon:
                    if len(con.intersection(subcon)) != 0:
                        changed = 1
                        break
            if changed:
                break
        if changed:
            cons[cons.index(con)] = con.union(subcon)
            cons.remove(subcon)
        oldcons = len(cons)

    lens = sorted([len(connection) for connection in cons])

    return math.prod(lens[-3:])


def partTwo(data):
    boxes = (set({(int(x),int(y), int(z)) for line in data for x, y, z in [line.strip().split(',')]}))
    cons = []
    distances = {}
    distbydist = {}
    for box in boxes:
        distances[box] = {}
        close = (-1,-1,-1)
        dist = 10000000000000000000
        for possCon in boxes:
            #calc distance
            if box == possCon:
                pass
            else:
                dist = math.sqrt((possCon[0] - box[0])**2 + (possCon[1] - box[1])**2 + (possCon[2] - box[2])**2)
                distances[box][possCon] = dist
                distbydist[dist] = (box, possCon)
                if distances[box][possCon] < dist:
                    dist = distances[box][possCon]
                    close = possCon
    sortDistances = sorted(distbydist.keys())
    closedist = 0
    for x in range(len(distbydist)):
        boxes = distbydist[sortDistances[x]]
        added = 0
        for connections in cons:
                if boxes[0] in connections or boxes[1] in connections:
                    connections.add(boxes[0])
                    connections.add(boxes[1])
                    added = 1
                    break
        if not added:
            cons.append(set({boxes[0], boxes[1]}))
        closedist = dist
        changed = 1
        while changed:
            changed = 0
            for con in cons:
                #see if it belongs in another set
                for subcon in cons:
                    if con != subcon:
                        if len(con.intersection(subcon)) != 0:
                            changed = 1
                            break
                if changed:
                    break
            if changed:
                cons[cons.index(con)] = con.union(subcon)
                cons.remove(subcon)
            oldcons = len(cons)
        if len(cons) == 1 and len(cons[0]) == 1000:
            break

    return boxes[1][0]*boxes[0][0]

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
