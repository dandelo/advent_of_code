#!/usr/local/bin/python3

from collections import Counter


def main():
    min = 134564
    max = 585159

    solve1(min,max)
    solve2(min,max)

def solve1(min, max):
    valid_pass_count = 0
    for i in range(min, max+1):
        digits = [int(x) for x in str(i)]
        if contains_adjacent_dupe(digits) and is_ascneding(digits):
            valid_pass_count += 1
    print(valid_pass_count)

def solve2(min, max):
    valid_pass_count = 0
    for i in range(min, max+1):
        digits = [int(x) for x in str(i)]
        if contains_exactly_two_adjacent_dupes(digits) and is_ascneding(digits):
            valid_pass_count += 1
    print(valid_pass_count)

def contains_exactly_two_adjacent_dupes(digits):
    return 2 in Counter(digits).values()

def contains_adjacent_dupe(digits):
    return max(Counter(digits).values()) >=2

def is_ascneding(digits):
    return sorted(digits) == digits

if __name__ == '__main__':
    main()
