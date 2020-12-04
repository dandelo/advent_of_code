#!/usr/local/bin/python3

import os

def main():
    
    passports = get_passports()

    ans1 = solve(passports)
    print(f'Part 1 answer: {ans1}')

    ans2 = solve(passports, False)
    print(f'Part 2 answer: {ans2}')


def solve(passports, skip_passport_validation = True):
    valid_passports_count = 0

    for passport in passports:
        passport_fields = dict(field.split(":") for field in passport.split(' '))
        passport_fields.pop('cid', None) # Don't care whether 'cid' exists or not
        if is_passport_or_north_pole_creds(passport_fields):
            if skip_passport_validation or is_valid_passport(passport_fields):
                valid_passports_count += 1
    
    return valid_passports_count
            
def is_passport_or_north_pole_creds(passport_fields):
    return len(passport_fields) == 7

def is_valid_passport(passport_fields):
    return is_valid_birth_year(passport_fields.get('byr')) and \
        is_valid_issue_year(passport_fields.get('iyr')) and \
        is_valid_experation_year(passport_fields.get('eyr')) and \
        is_valid_height(passport_fields.get('hgt')) and \
        is_valid_hair_colour(passport_fields.get('hcl')) and \
        is_valid_eye_colour(passport_fields.get('ecl')) and \
        is_valid_passport_id(passport_fields.get('pid'))

def is_valid_birth_year(byr):
    return 1920 <= int(byr) <= 2002

def is_valid_issue_year(iyr):
    return 2010 <= int(iyr) <= 2020

def is_valid_experation_year(eyr):
    return 2020 <= int(eyr) <= 2030

def is_valid_height(hgt):
    height = int(hgt[:-2])
    height_metric = hgt[-2:]
    if height_metric == 'in':
        if not 59 <= height <= 76:
            return False
    elif height_metric == 'cm':
        if not 150 <= height <= 193:
            return False
    else:
        return False
    return True

def is_valid_hair_colour(hcl):
    return len(hcl) == 7 and all(char in [str(x) for x in range(0,10)] + ['a', 'b', 'c', 'd', 'e', 'f'] for char in hcl[1:])

def is_valid_eye_colour(ecl):
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def is_valid_passport_id(pid):
    return len(pid) == 9

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
