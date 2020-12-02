#!/usr/local/bin/python3

import os
import re
import networkx as nx

do_small = False


def main():
    input_file = get_input_filename(do_small)

    coords = set()
    with open(input_file) as f:
        for line in f.readlines():
            w,x,y,z = map(int, re.findall('-?\d+', line))
            coords.add((w,x,y,z))

    ans1 = solve_part1(coords)
    print(f'Part 1 answer: {ans1}')

def solve_part1(coords):
    G = nx.Graph()
    for coord1 in coords:
        for coord2 in coords:
            dist = get_dist(coord1, coord2)
            if dist <= 3:
                G.add_edge(coord1, coord2)
    return nx.number_connected_components(G)

def get_dist(coord_1, coord_2):
    dist = 0
    for i in range(len(coord_1)):
        dist += abs(coord_1[i] - coord_2[i])
    return dist

def get_input_filename(do_small):
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    if do_small:
        input_file += ".small"

    return input_file

if __name__ == '__main__':
    main()
