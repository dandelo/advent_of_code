#!/usr/local/bin/python

def part1(filename='day1.input'):
    curr_freq = 0
    freqs = read_ints_from_file(filename)
    for freq in freqs:
        curr_freq+=(freq)
    print(curr_freq)

def part2(filename='day1.input'):
    curr_freq = 0
    prev_freqs = set([])
    freqs = read_ints_from_file(filename)

    # loop_count = 0
    while True:
        for freq in freqs:
            curr_freq+=(freq)
            if curr_freq in prev_freqs:
                print(curr_freq)
                # print(loop_count)
                return
            else:
                prev_freqs.add(curr_freq)
                # loop_count+=1

def read_ints_from_file(filename):
    with open(filename) as f:
        return map(int, f)


part2()
