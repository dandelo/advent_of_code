#!/usr/local/bin/python3

import os
from numpy import array, count_nonzero, copy, ndindex

neibhour_offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def main():
    global rows, cols
    seats = [[x for x in line.strip()] for line in open(get_input_filename())]
    seats_array = array(seats)
    rows, cols = seats_array.shape

    print(f'Part 1 answer: {solve(seats_array)}')
    print(f'Part 2 answer: {solve(seats_array, False)}')


def solve(seats, is_part1=True):
    comparison = array(False)
    while not comparison.all():
        prev_seats = copy(seats)
        seats = step(seats, is_part1)
        comparison = seats == prev_seats

    return count_nonzero(seats == '#')


def step(seats, is_part1):
    next_steps = copy(seats)
    for ix, iy in ndindex(seats.shape):
        seat = seats[ix, iy]
        if seat == ".":
            continue
        if is_part1:
            ocyupied_near_count = get_ocyupied_surrounding_seat_count(seats, ix, iy)
        else:
            ocyupied_near_count = get_ocyupied_in_view_seat_count(seats, ix, iy)
        if seat == "L" and ocyupied_near_count == 0:
            next_steps[ix][iy] = "#"
        if seat == "#" and ocyupied_near_count > 4:
            next_steps[ix][iy] = "L"

    # print(next_steps)
    # print()
    return next_steps


def get_ocyupied_surrounding_seat_count(array, x, y):
    surrounding_seats = array[max(0, x-1):min(rows, x+2), max(0, y-1):min(cols, y+2)]
    return count_nonzero(surrounding_seats == '#')


def get_ocyupied_in_view_seat_count(array, x, y):
    seats_in_view = 0
    for dx, dy in neibhour_offsets:
        cx, cy = x + dx, y + dy
        while 0 <= cx < rows and 0 <= cy < cols and array[cx][cy] == '.':
            cx += dx
            cy += dy
        seats_in_view += 0 <= cx < rows and 0 <= cy < cols and array[cx][cy] == '#'
    
    return seats_in_view


def next_seat_is_ocyupied(seat_line):
    removed_floor = list(filter(('.').__ne__, seat_line))
    if len(removed_floor) == 0 or removed_floor[0] == 'L':
        return False
    return True


def get_input_filename():
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    return input_file


if __name__ == '__main__':
    main()
