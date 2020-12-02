#!/usr/local/bin/python3

from parse import parse
from operator import itemgetter
from collections import Counter
from collections import defaultdict
import itertools
import os

do_small = False


def main():
    input_file = get_input_filename(do_small)
    nanobots = {}
    with open(input_file) as f:
        for line in f.readlines():
            x, y, z, r = parse('pos=<{:d},{:d},{:d}>, r={:d}', line)
            nanobots[x,y,z] = r
    ans1 = solve_part1(nanobots)
    print(f'Part 1 answer: {ans1}')

    ans2 = solve_part2(nanobots)
    print(f'Part 2 answer: {ans2}')

def solve_part2(nanobots):
    ranges = []
    for coord, radius in nanobots.items():
        dist_from_zero = abs(coord[0]) + abs(coord[1]) + abs(coord[2])
        # range_from_zero = range(dist_from_zero - radius, dist_from_zero + radius)
        ranges.append([dist_from_zero - radius, dist_from_zero + radius])
    # flattened_list = [elem for sublist in ranges for elem in sublist]
    # flattened_list = list(itertools.chain(*ranges))
    # counter = Counter(flattened_list)
    # counter.most_common(1)
    # ans = max((Counter(el).most_common(1)[0] for el in ranges), key=itemgetter(1))[0]
    START, END = 1, -1
    events = sorted(event for r in ranges  for event in zip(r, (START, END)))
    max_seen = curr_seen = max_seen_dist = 0
    for dist, start_or_end in events:
        curr_seen += start_or_end
        if curr_seen > max_seen:
            max_seen = curr_seen
            max_seen_dist = dist

    # print(events[max_seen + events[max_seen][1]])
    # print(events[max_seen-2:max_seen+2])
    # print(events[max_seen-1])
    # print(max_seen_dist)

    return max_seen_dist


def solve_part2_bak(nanobots):
    max_x = max([k[0] for k in nanobots.keys()])
    max_y = max([k[1] for k in nanobots.keys()])
    max_z = max([k[2] for k in nanobots.keys()])
    min_x = min([k[0] for k in nanobots.keys()])
    min_y = min([k[1] for k in nanobots.keys()])
    min_z = min([k[2] for k in nanobots.keys()])
    # print(f'{max_x}, {max_y}, {max_z}')
    # print(f'{min_x}, {min_y}, {min_z}')
    # print(f'{abs(max_x - min_x) * abs(max_y - min_y) * abs(max_x - min_y)}')

    ranges = defaultdict(list)
    ranges[0] = [(0,0,0)]
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            for z in range(min_z, max_z + 1):
                max_in_range = max(ranges.keys())
                nanbots_in_range = 0
                for coord, radius in nanobots.items():
                    if in_range(coord, (x,y,z), radius):
                        nanbots_in_range += 1
                if nanbots_in_range >= max_in_range:
                    ranges[nanbots_in_range].append((x,y,z))

    max_in_range = max(ranges.keys())
    print(f'Max nanobots in range = {max_in_range}, at coords:')
    for v in ranges[max_in_range]:
        print(v)

    ans = min([sum(map(abs,v)) for v in ranges[max_in_range]])
    return ans

def solve_part1(nanobots):
    strongest_nanobot = max(nanobots.items(), key=itemgetter(1))[0]
    max_radius = nanobots[strongest_nanobot]
    in_range_nanobots = 0
    for coord, radius in nanobots.items():
        if in_range(coord, strongest_nanobot, max_radius):
            in_range_nanobots += 1

    return in_range_nanobots

def in_range(a, b, radius):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2]) <= radius

def get_input_filename(do_small):
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    if do_small:
        input_file += ".small"

    return input_file

if __name__ == '__main__':
    main()
