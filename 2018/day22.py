#!/usr/local/bin/python3

import networkx as nx
from copy import deepcopy
# import matplotlib.pyplot as plt

# Tools:
none, climbing_gear, torch = 0, 1, 2
# Regions:
rock, wet, narrow = 0, 1, 2

# 1087
do_small = debug = False
if do_small:
    depth = 510
    target_coords = (10,10)
    extra_surrounding = 10
else:
    depth = 6969
    target_coords = (9,796)
    extra_surrounding = 100
erosion_levels = [[0 for i in range(target_coords[0] + 1 + extra_surrounding)] for j in range(target_coords[1] + 1 + extra_surrounding)]
region_types = [[0 for i in range(target_coords[0] + 1 + extra_surrounding)] for j in range(target_coords[1] + 1 + extra_surrounding)]

def main():
    solve_part1()

    ans1 = 0
    for x in range (target_coords[0] + 1):
        for y in range(target_coords[1] + 1):
            ans1 += region_types[y][x]
    if debug:
        draw_cavern()
    print(f'Part 1 answer: {ans1}')

    ans2 = solve_part2()
    if debug:
        draw_cavern()
    print(f'Part 2 answer: {ans2}')

def solve_part2():
    width = len(region_types[1])
    height = len(region_types)
    for y in range(height):
        for x in range(width):
            erosion_level = get_erosion_level(x,y)
            erosion_levels[y][x] = erosion_level
            region_type = erosion_level % 3
            region_types[y][x] = region_type
    
    # Create wieghted graph for cost of moving
    G = nx.Graph()
    for y in range(height):
        for x in range(width):
            # Add cost for switchig tools (and staying still)
            required_tools = get_required_tools(region_types[y][x])
            G.add_edge((x,y,required_tools[0]), (x,y,required_tools[1]), weight=7)

            # Add cost for all movements
            for x2, y2 in ((x,y-1), (x,y+1), (x+1,y), (x-1,y)):
                if 0 <= x2 < width and 0 <= y2 < height:
                    next_required_tools = get_required_tools(region_types[y2][x2])
                    for next_required_tool in set(required_tools).intersection(set(next_required_tools)):
                    # for next_required_tool in next_required_tools:
                        G.add_edge((x,y,next_required_tool), (x2,y2,next_required_tool), weight=1)

    ans = nx.dijkstra_path_length(G, (0, 0, torch), (target_coords[0], target_coords[1], torch))
    return ans


def solve_part1():
    width = len(region_types[1])
    height = len(region_types)
    for y in range(height):
        for x in range(width):
            erosion_level = get_erosion_level(x,y)
            erosion_levels[y][x] = erosion_level
            region_type = erosion_level % 3
            region_types[y][x] = region_type

def get_erosion_level(x,y):
    geologic_index = get_geologic_index(x,y)
    erosion_level = (geologic_index + depth) % 20183
    return erosion_level

def get_geologic_index(x,y):
    if (x,y) in [(0,0),target_coords]:
        return 0
    elif x == 0:
        return y * 48271
    elif y == 0:
        return x * 16807
    else:
        return erosion_levels[y][x-1] * erosion_levels[y-1][x]

def get_required_tools(region):
    if region  == rock:
        return [climbing_gear, torch]
    if region == wet:
        return [none, climbing_gear]
    if region == narrow:
        return [none, torch]

def draw_cavern():
    region_types_pretty = [[0 for i in range(target_coords[0] + 1)] for j in range(target_coords[1] + 1)] #deepcopy(region_types)
    for y in range(target_coords[1] + 1):
        for x in range(target_coords[0] + 1):
            region_type = region_types[y][x]
            if (x,y) == (0,0):
                region_type = 'M'
            elif (x,y) == target_coords:
                region_type = 'T'
            elif region_type == rock:
                region_type = '.'
            elif region_type == wet:
                region_type = '='
            elif region_type == narrow:
                region_type = '|'
            else:
                print('ERROR')
                SystemExit
            region_types_pretty[y][x] = region_type
    print('\n'.join([''.join(['{}'.format(item) for item in row])
      for row in region_types_pretty]))
    print()

if __name__ == '__main__':
    main()
