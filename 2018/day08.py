#!/usr/local/bin/python3

import os
from parse import parse
import sys

do_small = False
with open('day08.input') as f:
    data = f.read().splitlines()
data = list(map(int, data[0].split()))

def main():
    input_file = get_input_filename(do_small)

    with open(input_file) as f:
        data = f.read().splitlines()
    data = list(map(int, data[0].split()))

    # total, next_data, node_values = solve_part1(data)
    
    total, node_values = solve_part2(0)
    print(node_values)
    print(total)


def solve_part2(idx):
    next_idx = idx+2
    child_nodes, metadata_count = data[idx:next_idx]
    totals = 0

    if child_nodes:
        node_values = []
        for child_node in range(child_nodes):
            this_total, next_idx = solve_part2(next_idx)
            # totals += this_total
            node_values.append(this_total)
        for this_idx in data[next_idx:next_idx + metadata_count]:
            if this_idx - 1 < len(node_values):
                totals += node_values[this_idx - 1]
    else:
        totals += sum(data[next_idx:next_idx + metadata_count])

    return totals, next_idx + metadata_count


def solve_part1(data):
    child_nodes, metadata_count = data[:2]
    next_data = data[2:]
    node_values = []
    totals = 0

    for child_node in range(child_nodes):
        this_total, next_data, node_value = solve_part1(next_data)
        totals += this_total
        node_values.append(node_value)
    node_values.append(sum(next_data[:metadata_count]))
    totals += sum(next_data[:metadata_count])
    next_data = next_data[metadata_count:]

    return totals, next_data, node_values


def get_input_filename(do_small):
    day = os.path.basename(__file__)[3:5]
    input_file = "day" + day + ".input"

    if do_small:
        input_file += ".small"

    return input_file

if __name__ == '__main__':
    main()
