#!/usr/local/bin/python3

import os


def main():
    adapters = [int(line.strip()) for line in open(get_input_filename())]
    adapters.sort()
    adapters.insert(0,0)
    print(f'Part 1 answer: {solve_part1(adapters)}')
    print(f'Part 2 answer: {solve_part2(adapters)}')


def solve_part1(adapters):
    diffs = [adapters[x] - adapters[x-1] for x in range(1, len(adapters))]
    return (diffs.count(1)) * (diffs.count(3) + 1)


def solve_part2(adapters):
    variations = [1, 1]
    for i in range(2, len(adapters)):
        in_range = len([x for x in adapters[i-3:i] if x >= adapters[i] - 3])
        variations.append(sum(variations[-in_range:]))

    return max(variations)


def get_input_filename():
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    return input_file


if __name__ == '__main__':
    main()
