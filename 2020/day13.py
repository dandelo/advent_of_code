#!/usr/local/bin/python3

import os


def main():

    print(f'Part 1 answer: {solve_part1()}')
    print(f'Part 2 answer: {solve_part2()}')


def solve_part1():
    with open(get_input_filename()) as f:
        earliest_dep_time = int(f.readline().rstrip('\n'))
        buses = [int(bus) for bus in f.readline().split(',') if bus != 'x']

    least_waiting_time = (float("inf"), 0)
    for bus in buses:
        bus_waiting_time = bus - (earliest_dep_time % bus)
        if bus_waiting_time < least_waiting_time[0]:
            least_waiting_time = (bus_waiting_time, bus)
    return least_waiting_time[0] * least_waiting_time[1]

def solve_part2():
    buses = open(get_input_filename()).read().split('\n')[1].split(',')
    buses_idx = [(int(buses[k]), k) for k in range(len(buses)) if buses[k] != 'x']

    lcm = 1
    time = 0    
    for i in range(len(buses_idx)-1):
        bus_id = buses_idx[i+1][0]
        idx = buses_idx[i+1][1]
        lcm *= buses_idx[i][0]
        while (time + idx) % bus_id != 0:
            time += lcm
    return time

def get_input_filename():
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    return input_file


if __name__ == '__main__':
    main()
