#!/usr/local/bin/python3

from parse import parse
from operator import itemgetter
import os
from collections import deque

do_small = False
if do_small:
    minx = 494
else:
    minx = 313
debug = False
# spring = (500-minx, 0)
spring = [500-minx,0]

def main():
    input_file = get_input_filename(do_small)
    with open(input_file) as f:
        input = f.read().splitlines()
    ground = get_ground(input)

    flowing_water, static_water = solve(ground)

    print(f'Part 1 answer: {flowing_water+static_water}')
    print(f'Part 2 answer: {static_water}')

def draw_ground(ground):
    print('\n'.join([''.join(['{}'.format(item) for item in row])
      for row in ground]))

def get_ground(input):
    coords = set()

    for line in input:
        if line.startswith('y'):
            y, x1, x2 = parse('y={:d}, x={:d}..{:d}', line)
            for x in range(x1, x2 + 1):
                coords.add((x-minx,y))
        else:
            x, y1, y2 = parse('x={:d}, y={:d}..{:d}', line)
            for y in range(y1, y2 + 1):
                coords.add((x-minx,y))

    max_x = max(coords, key=itemgetter(0))[0]
    min_x = min(coords, key=itemgetter(0))[0]
    max_y = max(coords, key=itemgetter(1))[1]
    min_y = min(coords, key=itemgetter(1))[1]

    ground = [['.' for x in range(max_x + 1)] for y in range(max_y + 1)]
    for coord in coords:
        ground[coord[1]][coord[0]] = '#'
    # ground[spring[1]][spring[0]] = '+'
    return ground

def solve(ground):
    if debug:
        draw_ground(ground)
        print()

    belows = deque([spring])

    while belows:
        x, y = belows.popleft()
        orig_x = x
        # search down
        while y < len(ground) and ground[y][x] == '.':
            ground[y][x] = '|'
            y += 1
        if y == len(ground): # fall off the edge
            continue
        if ground[y][x] == '|': # already falling water
            continue
        else: # clay bottom or stable water bottom
            y -= 1
        if debug:
            draw_ground(ground)
            print()
        fall = True
        while fall:
            # search left
            while ground[y+1][x-1] != '.' and ground[y][x-1] != '#': # haven't reached a fall/wall
                x -= 1
                ground[y][x] = '|'
            if ground[y][x-1] != '#' and ground[y+1][x-1] != '#': # fall and no wall
                belows.append([x-1,y])
                fall = False
            # search left
            x = orig_x
            while ground[y+1][x+1] != '.' and ground[y][x+1] != '#': # nothing supporting, no blocking wall
                x += 1
                ground[y][x] = '|'
            if ground[y][x+1] != '#' and ground[y+1][x+1] != '#': # fall and no wall
                belows.append([x+1,y])
                fall = False
            x = orig_x
            if fall:
                while ground[y][x] in ['|', '~']: # settle water
                    ground[y][x] = '~'
                    x -= 1
                x = orig_x
                while ground[y][x] in ['|', '~']: # settle water
                    ground[y][x] = '~'
                    x += 1
                x, y = orig_x, y-1 # move up one row
                if ground[y][x] != '|': # make sure to fill it with water
                    ground[y][x] = '|'
        if debug:
            draw_ground(ground)
            print()

    if debug:
            draw_ground(ground)
            print()
    flowing_water = sum(x.count('|') for x in ground) - 3 # Don't count spring
    static_water = sum(x.count('~') for x in ground)
    return flowing_water, static_water


def get_input_filename(do_small):
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    if do_small:
        input_file += ".small"

    return input_file

if __name__ == '__main__':
    main()
