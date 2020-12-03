#!/usr/local/bin/python3

from parse import parse
import os

def main():
    input_file = get_input_filename()

    ans1 = solve_part1(input_file)
    print(f'Part 1 answer: {ans1}')

    ans2 = solve_part2(input_file)
    print(f'Part 2 answer: {ans2}')

def solve_part1(input_file):
    valid_passwds_count = 0
    with open(input_file) as f:
        for line in f.readlines():
            least, most, char, passwd = parse('{:d}-{:d} {}: {}', line)
            if passwd.count(char) >= least and passwd.count(char) <= most:
                valid_passwds_count+=1

    return valid_passwds_count

def solve_part2(input_file):
    valid_passwds_count = 0
    with open(input_file) as f:
        for line in f.readlines():
            pos1, pos2, char, passwd = parse('{:d}-{:d} {}: {}', line)
            if (passwd[pos1-1] == char) + (passwd[pos2-1] == char) == 1:
                valid_passwds_count+=1

    return valid_passwds_count
                    

def get_input_filename():
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    return input_file

if __name__ == '__main__':
    main()
