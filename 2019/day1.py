#!/usr/local/bin/python3

from math import floor
import os

def main():
    do_small = False
    input_file = get_input_filename(do_small)

    with open(input_file) as f:
        input = [int(x) for x in f.read().splitlines()]

    ans1 = solve_part1(input)
    print(f'Part 1 answer: {ans1}')

    ans2 = solve_part2(input)
    print(f'Part 2 answer: {ans2}')

def solve_part1(input):
    return sum([get_fuel_req(x) for x in input])

def solve_part2(input):
    return sum([get_complex_fuel_req(x) for x in input])

def get_fuel_req(mass):
    return floor(mass/3) - 2

def get_complex_fuel_req(mass):
    total = 0
    while mass >= 0:
        mass = floor(mass/3) - 2
        if mass > 0:
            total += mass

    return total

def get_input_filename(do_small):
    day = os.path.basename(__file__)[3:4]
    input_file = "inputs/day" + day + ".input"

    if do_small:
        input_file += ".small"

    return input_file

if __name__ == '__main__':
    main()
