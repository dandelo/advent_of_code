#!/usr/local/bin/python3

import os
from functools import reduce

def main():
    
    passports = get_passports()

    ans1 = solve(passports)
    print(f'Part 1 answer: {ans1}')


def solve(passports):
    valid_passports_count = 0

    for passport in passports:
        if passport_is_valid(passport):
            valid_passports_count += 1
    
    return valid_passports_count
            
def passport_is_valid(passport):
    fields = dict(field.split(":") for field in passport.split(' '))
    if len(fields) == 8 or (len(fields) == 7 and "cid" not in fields):
        return True
    
    return False

def get_passports():
    input_file = get_input_filename()

    with open(input_file) as f:
        data = f.read()
    
    return [passport.replace('\n', ' ') for passport in data.split('\n\n')]


def get_input_filename():
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    return input_file

if __name__ == '__main__':
    main()
