#!/usr/local/bin/python3

from collections import defaultdict
from parse import parse
import os


def main():
    do_small = False
    day = os.path.basename(__file__)[3:5]
    input_file = "day" + day + ".input"

    if do_small:
        input_file += ".small"

    solve(input_file)


def solve(filename='day6.input.small'):
    coords = set()
    max_x = max_y = min_x = min_y = 0

    with open(filename) as f:
        for line in f.readlines():
            x, y = map(int, line.split(", "))
            # x, y = parse('{:d}, {:d}', line)
            coords.add((x, y))
            max_x = max(max_x, x)
            max_y = max(max_y, y)
            min_x = min(min_x, x)
            min_y = min(min_y, y)

    ans1 = solve_part1(coords, max_x, max_y, min_x, min_y)
    print(ans1)

    # ans2 = solve_part2(coords, max_x, max_y, min_x, min_y)
    # print(ans2)


def solve_part2(coords, max_x, max_y, min_x, min_y):
    safe_regions = 0

    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            total_dist = 0
            for coord in coords:
                dist = get_dist(coord, (x, y))
                total_dist += dist
            if total_dist < 10000:
                safe_regions += 1

    return safe_regions


def solve_part1(coords, max_x, max_y, min_x, min_y):
    region_sizes = defaultdict(int)
    infinite_ids = set()

    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            min_coord = (0,0)
            min_dist = 100000
            for coord in coords:
                dist = get_dist(coord, (x, y))
                if dist < min_dist:
                    min_dist = dist
                    min_coord = coord
                elif dist == min_dist:
                    min_coord = (-1,-1)
            if x == max_x or x == min_x or y == max_y or y == min_y:
                infinite_ids.add(min_coord)
            region_sizes[min_coord] += 1

    max_region = 0
    for key, value in region_sizes.items():
        if value > max_region and key not in infinite_ids:
            max_region = value

    return max_region

def get_dist(coord_1, coord_2):
    return abs(coord_1[0] - coord_2[0]) + abs(coord_1[1] - coord_2[1])



def print_board(board):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in board]))

if __name__ == '__main__':
    main()
