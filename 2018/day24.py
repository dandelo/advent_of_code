#!/usr/local/bin/python3

import os
import re
from dataclasses import dataclass
from copy import deepcopy

do_small = False
debug = False


def main():
    input_file = get_input_filename(do_small)
    armies = get_armies(input_file)

    winning_team, remaining_units = solve_part1(armies)
    print(f'Part 1 answer: {remaining_units} (winners = {winning_team})')

    boost = 78
    while winning_team != 'Immune System':
        print(f'Running with boost of {boost}')
        armies = get_armies(input_file, boost)
        winning_team, remaining_units = solve_part1(armies)
        boost += 1
    print(f'Part 2 answer: {remaining_units} (requied boost of {boost - 1})')

def solve_part1(armies):
    armies = reset_turn(armies)
    # While two teams left
    while len(set([army.team for army in armies if army.is_alive])) != 1:
        armies = target_selection(armies)
        armies = attack(armies)
        armies = reset_turn(armies)
        if debug:
            print('Immune System:')
            for army in sorted([x for x in armies if x.team == 'Immune System'], key=lambda army: (army.id)):
                print(f'{army.id}: {army.units}')
            print('Infection:')
            for army in sorted([x for x in armies if x.team == 'Infection'], key=lambda army: (army.id)):
                print(f'{army.id}: {army.units}')
            print()

    remaining_units = sum([army.units for army in armies])
    return armies[0].team, remaining_units

def attack(armies):
    armies = sorted(armies, key=lambda army: (army.initiative), reverse=True)
    for army in armies:
        if not army.is_alive or army.target == -1:
            continue
        defending_army = [x for x in armies if x.id == army.target and army.team != x.team][0]
        dmg_dealt = get_dmg_dealt(army, defending_army)
        killed_units = int(dmg_dealt / defending_army.hp)
        defending_army.units -= killed_units
        if defending_army.units <= 0:
            defending_army.is_alive = False
    return armies

def get_dmg_dealt(army, enemy):
    if army.dmg_type in enemy.weaknesses:
        dmg_multiplier = 2
    elif army.dmg_type in enemy.immunities:
        dmg_multiplier = 0
    else:
        dmg_multiplier = 1

    return army.get_power() * dmg_multiplier

def target_selection(armies):
    for army in armies:
        defending_army = get_defending_army(army, armies)
        if not defending_army:
            continue
        defending_army.is_targetted = True
        army.target = defending_army.id
    return armies

def reset_turn(armies):
    # Remove dead
    armies = [x for x in armies if x.is_alive]
    # Unset targets
    for army in armies:
        army.is_targetted = False
        army.target = -1
    # Sort for next turns targetting phase
    armies = sorted(armies, key=lambda army: (army.get_power(), army.initiative), reverse=True)
    return armies

def get_defending_army(army, armies):
    all_enemies = [x for x in armies if x.team != army.team and not x.is_targetted and army.dmg_type not in x.immunities]
    if not all_enemies:
        return None

    weak_enemies = [x for x in all_enemies if army.dmg_type in x.weaknesses]
    if weak_enemies:
        return sorted(weak_enemies, key=lambda army: (army.get_power(), army.initiative), reverse=True)[0]

    return sorted(all_enemies, key=lambda army: (army.get_power(), army.initiative), reverse=True)[0]


@dataclass
class Army:
    id: int
    team: str
    units: int
    hp: int
    dmg: int
    dmg_type: str
    initiative: int
    weaknesses: list
    immunities: list
    is_alive: bool = True
    is_targetted: bool = False
    target: int = -1

    def get_power(self):
        return self.units * self.dmg

def get_armies(input_file, boost=0):
    armies = []
    with open(input_file) as f:
        for line in f.readlines():
            weaknesses = []
            immunities = []
            if line == 'Immune System:\n':
                army_id = 1
                team = 'Immune System'
                dmg_boost = boost
                continue
            elif line == 'Infection:\n':
                army_id = 1
                team = 'Infection'
                dmg_boost = 0
                continue
            elif line == '\n':
                continue
            units, hp, dmg, initiative = map(int, re.findall('\d+', line))
            dmg += dmg_boost

            weaknesses_match = re.search(re.compile("weak to ([A-z, ]+)"), line)
            if weaknesses_match:
                weaknesses = weaknesses_match.group(1).split(', ')

            immunities_match = re.search(re.compile("immune to ([A-z, ]+)"), line)
            if immunities_match:
                immunities = immunities_match.group(1).split(', ')

            dmg_type = re.search(re.compile("([A-z]+) damage"), line).group(1)

            armies.append(Army(
                        id=army_id,
                        team=team,
                        units=units,
                        hp=hp,
                        dmg=dmg,
                        dmg_type=dmg_type,
                        initiative=initiative,
                        weaknesses=weaknesses,
                        immunities=immunities,
                        ))
            army_id += 1
    return armies

def get_input_filename(do_small):
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    if do_small:
        input_file += ".small"

    return input_file

if __name__ == '__main__':
    main()
