#!/usr/local/bin/python3

import os, sys
import operator

do_small = False


def main():
    input_file = get_input_filename(do_small)

    with open(input_file) as f:
        wire1, wire2 = [x.split(',') for x in f.read().splitlines()]

    coords1 = parse_wire_path(wire1)
    coords2 = parse_wire_path(wire2)
    intersections, ans1 = find_clostest_intersection(coords1, coords2)
    print(f'Part 1: {ans1}')

    ans2 = solve2(wire1, wire2, intersections)
    print(f'Part 2: {ans2}')

def find_clostest_intersection(coords1, coords2):
    meeting_points = set()
    for coord1 in coords1:
        if coord1 in coords2:
            meeting_points.add(coord1)

    closest_meeting_point = 99999
    for meeting_point in meeting_points:
        dist_from_zero = abs(meeting_point[0]) + abs(meeting_point[1])
        if dist_from_zero < closest_meeting_point and dist_from_zero > 0:
            closest_meeting_point = dist_from_zero

    return meeting_points, closest_meeting_point

def solve2(wire1, wire2, intersections):
    min_dist = 99999999
    for intersection in intersections:
        dist = get_dist_to_intersection(wire1, intersection) + get_dist_to_intersection(wire2, intersection)
        if dist < min_dist:
            min_dist = dist
    return min_dist

def get_dist_to_intersection(wire_path, intersection):
    total_dist = 0
    last_x = 0
    last_y = 0

    for vel in wire_path:
        dir = vel[0]
        dist = int(vel[1:])

        if dir == 'R':
            for i in range(last_x + 1, last_x + dist + 1):
                total_dist += 1
                if (i, last_y) == intersection:
                    return total_dist
                last_x = i
        elif dir == 'L':
            for i in reversed(range(last_x - dist, last_x)):
                total_dist += 1
                if (i, last_y) == intersection:
                    return total_dist
                last_x = i
        elif dir == 'U':
            for i in range(last_y + 1, last_y + dist + 1):
                total_dist += 1
                if (last_x, i) == intersection:
                    return total_dist
                last_y = i
        elif dir == 'D':
            for i in reversed(range(last_y - dist, last_y)):
                total_dist += 1
                if (last_x, i) == intersection:
                    return total_dist
                last_y = i

def parse_wire_path(input):
    path = set()
    last_x = 0
    last_y = 0
    for vel in input:
        dir = vel[0]
        dist = int(vel[1:])

        if dir == 'R':
            for i in range(last_x + 1, last_x + dist + 1):
                path.add((i, last_y))
                last_x = i
        elif dir == 'L':
            for i in reversed(range(last_x - dist, last_x)):
                path.add((i, last_y))
                last_x = i
        elif dir == 'U':
            for i in range(last_y + 1, last_y + dist + 1):
                path.add((last_x, i))
                last_y = i
        elif dir == 'D':
            for i in reversed(range(last_y - dist, last_y)):
                path.add((last_x, i))
                last_y = i

    return path

def get_input_filename(do_small):
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    if do_small:
        input_file += ".small"

    return input_file

if __name__ == '__main__':
    main()
