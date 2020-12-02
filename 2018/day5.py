#!/usr/local/bin/python

from string import ascii_lowercase

def solve(filename='day5.input'):
    with open(filename) as f:
        polymer = f.read()

    # solved_polymer = solve_part1(polymer)
    # print(len(solved_polymer) - 1)
    solved_polymer_len = solve_part2(polymer)
    print(solved_polymer_len - 1)

def solve_part2(polymer):
    smallest_length = len(polymer)
    for char in ascii_lowercase:
        improved_polymer = polymer
        improved_polymer = improved_polymer.replace(char, "")
        improved_polymer = improved_polymer.replace(char.upper(), "")
        improved_polymer = solve_part1(improved_polymer)
        current_length = len(improved_polymer)
        if current_length < smallest_length:
            smallest_length = current_length

    # print(polymer)
    return smallest_length

def solve_part1(polymer):
    prev_length = len(polymer)
    current_length = 0
    while prev_length != current_length:
        prev_length = len(polymer)
        for char in ascii_lowercase:
            to_remove1 = char + char.upper()
            to_remove2 = char.upper() + char
            polymer = polymer.replace(to_remove1, "")
            polymer = polymer.replace(to_remove2, "")
        current_length = len(polymer)
    # print(polymer)
    return(polymer)


solve('day5.input')
