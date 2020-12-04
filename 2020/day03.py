#!/usr/local/bin/python3

import os
from functools import reduce

def main():
    input_file = get_input_filename()
    map = [line.rstrip('\n') for line in open(input_file)]

    ans1 = solve(map, [(3, 1)])
    print(f'Part 1 answer: {ans1}')

    ans2 = solve(map, [ (1, 1), (3, 1), (5, 1), (7, 1), (1, 2) ] )
    print(f'Part 2 answer: {ans2}')

def solve(map, routes):
    total_trees_hit = []
    map_length = len(map)
    map_width = len(map[0])
    for right, down in routes:
        trees_hit = 0
        for y in range(0, map_length, down):
            x = y*right % map_width
            tree_or_not = map[y][x]
            if tree_or_not == '#':
                trees_hit += 1
            y += down
        total_trees_hit.append(trees_hit)
    
    return reduce(lambda x, y: x*y, total_trees_hit)

def get_input_filename():
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    return input_file

if __name__ == '__main__':
    main()
