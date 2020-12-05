#!/usr/local/bin/python3

import os


def main():
    boarding_passes = [line.rstrip('\n')
                       for line in open(get_input_filename())]

    seat_ids = set(map(get_seat_id, boarding_passes))

    print(f'Part 1 answer: {max(seat_ids)}')

    print(f'Part 1 answer: {get_missing_seat_id(seat_ids)}')


def get_seat_id(boarding_pass):
    row_digits = 3
    col = int(boarding_pass[-row_digits:].replace('L', '0').replace('R', '1'), 2)
    row = int(boarding_pass[:-row_digits].replace('F', '0').replace('B', '1'), 2)

    return row * 8 + col


def get_missing_seat_id(seat_ids):
    all_seats = set(range(min(seat_ids), max(seat_ids)))

    return (all_seats - seat_ids).pop()


def get_input_filename():
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    return input_file


if __name__ == '__main__':
    main()
