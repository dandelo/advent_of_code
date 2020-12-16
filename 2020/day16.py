#!/usr/local/bin/python3

import os
from functools import reduce
from timeit import default_timer as timer

def main():
    start = timer()
    ticket_data = open(get_input_filename()).read().split('\n\n')
    rules = dict([x.split(': ') for x in ticket_data[0].split('\n')])
    for k,v in rules.items():
        fields = [[int(x) for x in field.split('-')] for field in v.split(' or ')]
        rules[k] = [range(field[0], field[1]+1) for field in fields]

    my_ticket = [int(x) for x in ticket_data[1].split('\n')[1].split(',')]
    nearby_ticket = [[int(x) for x in y.split(',')] for y in ticket_data[2].split('\n')[1:]]

    print(f'Part 1 answer: {solve_part1(nearby_ticket, rules)}')
    print(f'Part 2 answer: {solve_part2(my_ticket, nearby_ticket, rules)}')
    stop = timer()
    print(f"Completed in in {stop - start}")

def solve_part1(tickets, rules):
    valid_values = set()
    invalid_fields_total = 0
    [[valid_values.add(x) for x in y] for y in rules.values()]

    
    for ticket in tickets:
        for field in ticket:
            if not is_valid_value(field, valid_values):
                invalid_fields_total += field

    return invalid_fields_total

def solve_part2(my_ticket, tickets, rules):
    valid_tickets = get_valid_tickets(tickets, rules)
    
    possible_rules_for_fields = []
    for i in range(len(rules)):
        field_values = set([ticket[i] for ticket in valid_tickets])
        possible_field_rules = get_possible_rules_for_field(rules, field_values)
        possible_rules_for_fields.append(possible_field_rules)
        if len(possible_field_rules) == 1:
            del rules[possible_field_rules[0]]


    actual_field_rules = get_actual_rules_for_fields(possible_rules_for_fields)
    departure_fields = [idx for idx,x in enumerate(actual_field_rules) if x[0].startswith('departure')]
    
    return reduce((lambda x, y: x * y), [my_ticket[x] for x in departure_fields])

def get_possible_rules_for_field(rules, field_values):
    possible_rules_for_fields = set(rules.keys())

    for field_value in field_values:
        for rule, valid_rule_values in rules.items():
            if not is_valid_value(field_value, valid_rule_values):
                possible_rules_for_fields.remove(rule)
    
    return list(possible_rules_for_fields)

def get_actual_rules_for_fields(possible_rules_for_fields):
    solved = set()
    while len(solved) != len(possible_rules_for_fields):
        fields_with_single_answer = [x[0] for x in possible_rules_for_fields if len(x) == 1 and x[0] not in solved]
        solved.update(fields_with_single_answer)
        for idx, possible_rules in enumerate(possible_rules_for_fields):
            if len(possible_rules) == 1:
                continue
            possible_rules_for_fields[idx] = [x for x in possible_rules if x not in solved]

    return possible_rules_for_fields

def get_valid_tickets(tickets, rules):
    valid_values = set()
    [[valid_values.add(x) for x in y] for y in rules.values()]
    valid_tickets = []
    for ticket in tickets:
        for field in ticket:
            if not is_valid_value(field, valid_values):
                break
        else:
            valid_tickets.append(ticket)
    return valid_tickets

def is_valid_value(value, valid_values):
    return any([x for x in valid_values if value in x])


def get_input_filename():
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    return input_file


if __name__ == '__main__':
    main()
