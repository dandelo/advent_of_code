#!/usr/local/bin/python3

import os, sys
from dataclasses import dataclass
import collections
from copy import deepcopy
import re


debug = False

def main():
    do_small = False

    input_file = get_input_filename(do_small)
    with open(input_file) as f:
        landscape = list(map(list, f.read().splitlines()))

    woods, lumberards = solve(landscape)
    print(f'Part 1 answer: {woods} woods and {lumberards} lumberards. Answer = {woods * lumberards}')

    # ans = solve(landscape, True)
    # print(f'Part 2 answer: {ans}')
    woods, lumberards = solve(landscape, True)
    print(f'Part 2 answer: {woods} woods and {lumberards} lumberards. Answer = {woods * lumberards}')


def solve(landscape, part2 = False):
    landscape = deepcopy(landscape)
    if debug:
        draw_landscape(landscape)
    if part2:
        mins = 1000
    else:
        mins = 11
    snapshots = []
    for min in range(1,mins):
        prev_landspace = deepcopy(landscape)
        for i,row in enumerate(landscape):
                for j,char in enumerate(row):
                    surroundings = get_surroundings((i,j), prev_landspace)
                    if char == '.' and surroundings.count('|') >=3:
                        landscape[i][j] = '|'
                    elif char == '|' and surroundings.count('#') >=3:
                        landscape[i][j] = '#'
                    elif char == '#':
                        if not (surroundings.count('#') >=1 and surroundings.count('|') >=1):
                            landscape[i][j] = '.'
        # current_score = sum(x.count('|') for x in landscape) * sum(x.count('#') for x in landscape)

        snapshot = '\n'.join(''.join(row) for row in landscape)
        if snapshot in snapshots:
            idx = snapshots.index(snapshot)
            print("Found %d as a repeat of %d" % (min, 1+idx))
            period = min - (1+idx)
            while (idx+1) % period != 1000000000 % period:
                idx += 1
            # print(snapshots[idx])
            count1 = len(re.findall('[|]', snapshots[idx]))
            count2 = len(re.findall('[#]', snapshots[idx]))
            print((idx+1, count1, count2))
            print(count1 * count2)
            return sum(x.count('|') for x in  snapshots[idx]), sum(x.count('#') for x in  snapshots[idx])
        snapshots.append(snapshot)

    if debug:
        draw_landscape(landscape)


    return sum(x.count('|') for x in landscape), sum(x.count('#') for x in landscape)

def get_surroundings(coords, landscape):
    x = coords[0]
    y = coords[1]
    width = len(landscape)
    height = len(landscape[0])
    surroundings = []
    for x2, y2 in ((x-1,y-1), (x-1,y), (x-1,y+1), (x,y-1), (x,y+1), (x+1, y-1), (x+1,y), (x+1, y+1)):
        if 0 <= x2 < width and 0 <= y2 < height:
            surroundings.append(landscape[x2][y2])
    return surroundings

def draw_landscape(landscape):
    print('\n'.join([''.join(['{}'.format(item) for item in row])
      for row in landscape]))
    print()

def get_input_filename(do_small):
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    if do_small:
        input_file += ".small"

    return input_file

if __name__ == '__main__':
    main()
