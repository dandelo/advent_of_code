#!/usr/local/bin/python3

import networkx as nx
import os
from parse import parse
import sys

do_small = False

def main():
    input_file = get_input_filename(do_small)
    step_deps = set(tuple(parse('Step {} must be finished before step {} can begin.', line)) for line in open(input_file))

    # solve_part1(step_deps)
    solve_part2(step_deps)

def solve_part1(steps):
    g = nx.DiGraph()
    for step, dep in steps:
        g.add_edge(step, dep)
    print(''.join(nx.lexicographical_topological_sort(g)))

def solve_part2(steps_deps):
    counter = 0
    if do_small:
        worker_count = 2
    else:
        worker_count = 5
    workers = {i: [0, '.'] for i in range(worker_count)}
    remaining_steps = set([step for dep in steps_deps for step in dep])
    in_progress_steps = set()

    while remaining_steps:
        for worker, activity in workers.items():
            busy_time = activity[0]
            if busy_time != 0:
                # if 1, then completing step this turn
                if busy_time == 1:
                    step = activity[1]
                    remaining_steps.remove(step)
                    workers[worker][1] = '.'
                    in_progress_steps.remove(step)
                    steps_deps = set([(x, y) for x, y in steps_deps if step not in x])
                workers[worker][0] = workers[worker][0] - 1

        ready_steps = get_nodes_with_no_deps(steps_deps, remaining_steps, in_progress_steps)
        if not ready_steps:
            counter += 1
            continue

        free_workers = get_free_workers(workers)
        while free_workers:
            if not ready_steps:
                break
            worker = free_workers.pop()
            step = ready_steps[0]
            if do_small:
                workers[worker][0] = ord(step) - 64
            else:
                workers[worker][0] = ord(step) - 4
            workers[worker][1] = step
            in_progress_steps.add(step)
            ready_steps.remove(step)
        # print(f'{counter}  {workers[1][1]}  {workers[2][1]}  {workers[3][1]}  {workers[4][1]}  {workers[5][1]}')
        counter += 1
    # Was complete before final increment
    print(counter - 1)

def get_free_workers(workers):
    free_workers = set()
    for worker, activity in workers.items():
        busy_time = activity[0]
        if busy_time == 0:
            free_workers.add(worker)
    return free_workers

def get_nodes_with_no_deps(steps_deps, remaining_steps, in_progress_steps):
    nodes_with_no_deps = set()
    for step in remaining_steps:
        # If step isn't a dep of another stop and not in progress
        if step not in [x[1] for x in steps_deps] and step not in in_progress_steps:
            nodes_with_no_deps.add(step)
    return sorted(nodes_with_no_deps)


def get_input_filename(do_small):
    day = os.path.basename(__file__)[3:5]
    input_file = "day" + day + ".input"

    if do_small:
        input_file += ".small"

    return input_file

if __name__ == '__main__':
    main()
