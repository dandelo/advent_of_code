#!/usr/local/bin/python

from datetime import datetime
import re

def solve(filename='day4.input'):
    with open(filename) as f:
        records = f.read().splitlines()

    parsed_records = list(map(parse_records, records))
    parsed_records.sort()

    # print('\n'.join(' '.join(map(str,sl)) for sl in parsed_records))
    guards_sleep_times = calc_sleep_times(parsed_records)
    # print(guards_sleep_times)
    solve_part1(guards_sleep_times)
    solve_part2(guards_sleep_times)

def solve_part2(guards_sleep_times):
    higest_freq_min_alseep = 0
    guard_id, min = 0,0
    for guard in guards_sleep_times:
        if len(guards_sleep_times[guard]) == 0:
            continue
        most_common_min_asleep = get_most_common_min_asleep(guards_sleep_times, guard)
        most_common_min_asleep_count = guards_sleep_times[guard].count(most_common_min_asleep)
        if most_common_min_asleep_count > higest_freq_min_alseep:
            higest_freq_min_alseep = most_common_min_asleep_count
            guard_id = guard
            min = most_common_min_asleep
    # print ("{} {} {}".format(guard_id, min, higest_freq_min_alseep))
    print(guard_id * min)

def solve_part1(guards_sleep_times):
    longest_sleeping_guard = max(guards_sleep_times, key= lambda x: len(guards_sleep_times[x]))
    # print(longest_sleeping_guard)
    most_common_min_asleep = get_most_common_min_asleep(guards_sleep_times, longest_sleeping_guard)
    print(longest_sleeping_guard * most_common_min_asleep)

def get_most_common_min_asleep(guards_sleep_times, guard_id):
    return max(set(guards_sleep_times[guard_id]), key=guards_sleep_times[guard_id].count)

def calc_sleep_times(records):
    guards_sleep_times = {}
    for record in records:
        time = record[0]
        action = record[1]
        min = time.minute

        if action.startswith('Guard'):
            guard_id = int(action.split()[1])
            if guard_id not in guards_sleep_times:
                guards_sleep_times[guard_id]=[]
        elif action == 'falls asleep':
            start_sleep_time = min
        elif action == 'wakes up':
            end_sleep_time = min
            asleep_time = list(range(start_sleep_time, end_sleep_time))
            guards_sleep_times[guard_id]=guards_sleep_times.get(guard_id) + asleep_time
    return(guards_sleep_times)



def parse_records(records):
    line_els = records.split()

    line_els = records.split()

    # Remove []# chars
    line_els = [s.strip('[]#') for s in line_els]
    date = line_els[0].replace('1518', '2000')
    time = line_els[1]

    # 1518-06-12 23:57
    record_time = datetime.strptime(date + time, '%Y-%m-%d%H:%M')

    action = ' '.join(line_els[2:])
    return [record_time, action]

solve()
