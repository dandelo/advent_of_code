#!/usr/local/bin/python3

import os

# 53183


def main():
    instructions = [(line[0], int(line[1:].rstrip('\n')))
                    for line in open(get_input_filename())]

    print(f'Part 1 answer: {solve_part1(instructions)}')
    print(f'Part 2 answer: {solve_part2(instructions)}')


def solve_part1(instructions):
    x = y = 0
    dir = 0  # 0=E, 1=S, 2=W, 3=N
    for instruction in instructions:
        action = instruction[0]
        value = instruction[1]
        if action == 'N':
            y += value
        elif action == 'S':
            y -= value
        elif action == 'E':
            x += value
        elif action == 'W':
            x -= value
        elif action == 'L':
            dir = int((dir - value/90) % 4)
        elif action == 'R':
            dir = int((dir + value/90) % 4)
        elif action == 'F':
            if dir == 0:
                x += value
            elif dir == 1:
                y -= value
            elif dir == 2:
                x -= value
            elif dir == 3:
                y += value
    return(abs(x) + abs(y))


def solve_part2(instructions):
    waypoint = (10, 1)
    boat_location = (0, 0)
    for instruction in instructions:
        action = instruction[0]
        value = instruction[1]
        if action == 'N':
            waypoint = (waypoint[0], waypoint[1]+value)
        elif action == 'S':
            waypoint = (waypoint[0], waypoint[1]-value)
        elif action == 'E':
            waypoint = (waypoint[0]+value, waypoint[1])
        elif action == 'W':
            waypoint = (waypoint[0]-value, waypoint[1])
        elif action == 'R':
            value = value/90 % 4
            if value == 1:
                waypoint = (waypoint[1], -1*waypoint[0])
            elif value == 2:
                waypoint = (-1*waypoint[0], -1*waypoint[1])
            elif value == 3:
                waypoint = (-1*waypoint[1], waypoint[0])
        elif action == 'L':
            value = value/90 % 4
            if value == 1:
                waypoint = (-1*waypoint[1], waypoint[0])
            elif value == 2:
                waypoint = (-1*waypoint[0], -1*waypoint[1])
            elif value == 3:
                waypoint = (waypoint[1], -1*waypoint[0])
        elif action == 'F':
            boat_location = (boat_location[0]+value*waypoint[0], boat_location[1]+value*waypoint[1])
        # print((boat_location),waypoint)
    return(abs(boat_location[0]) + abs(boat_location[1]))


def get_input_filename():
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    return input_file


if __name__ == '__main__':
    main()
