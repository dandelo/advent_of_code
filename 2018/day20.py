#!/usr/local/bin/python3

import os
import re
import itertools
import networkx as nx

do_small = False
starting_pos = (0, 0)

def main():
    input_file = get_input_filename(do_small)
    with open(input_file) as f:
        input = f.read().splitlines()[0]

    maze = solve(input)
    paths = nx.algorithms.shortest_path_length(maze, starting_pos)
    ans1 = max(paths.values())
    ans2 = sum(value >= 1000 for value in paths.values())

    print(f'Part 1 answer: {ans1}')
    print(f'Part 2 answer: {ans2}')


def solve(input):
    d = {
        "N": (0, 1),
        "E": (1, 0),
        "S": (0, -1),
        "W": (-1, 0)
    }
    maze = nx.Graph()
    current_pos = starting_pos
    branches = []
    for c in input[1:-2]:
        if c in 'NESW':
            new_pos = tuple(map(sum,zip(current_pos,d[c])))
            maze.add_edge(current_pos, new_pos)
            current_pos = new_pos
        elif c == '(': # Split in path
            branches.append(current_pos)
        elif c == ')': # Split ends
            current_pos = branches.pop()
        elif c == '|': # Start again at last split
            current_pos = branches[-1]
        else:
            print('ERROR')
            SystemExit

    return maze


def draw_ground(ground):
    print('\n'.join([''.join(['{}'.format(item) for item in row])
      for row in ground]))

def get_input_filename(do_small):
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    if do_small:
        input_file += ".small"

    return input_file

if __name__ == '__main__':
    main()
