#!/usr/local/bin/python3

import os


def main():
    boarding_passes = [line.rstrip('\n') for line in open(get_input_filename())]

    seat_ids = []
    for boarding_pass in boarding_passes:
        seat_id = get_seat_id(boarding_pass)
        seat_ids.append(seat_id)
    print(f'Part 1 answer: {max(seat_ids)}')

    print(f'Part 1 answer: {get_missing_seat_id(seat_ids)}')


def get_seat_id(boarding_pass):
    row = int(boarding_pass[:-3].replace('F', '0').replace('B', '1'), 2)
    col = int(boarding_pass[-3:].replace('L', '0').replace('R', '1'), 2)

    return row * 8 + col

def get_missing_seat_id(seat_ids):
    seat_ids.sort()
    for idx, seat_id in enumerate(seat_ids):
        if seat_ids[idx+1] != seat_id + 1:
            return seat_id + 1


def get_input_filename():
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    return input_file


if __name__ == '__main__':
    main()
