#!/usr/local/bin/python3

import os, sys
from dataclasses import dataclass
import collections

debug = False

def main():
    do_small = False

    input_file = get_input_filename(do_small)
    with open(input_file) as f:
        board = f.read().splitlines()

    rounds, hp_remaining, winning_race = solve_part1(board)
    print(f'Part 1 answer: {winning_race} win with {hp_remaining} hp in {rounds} rounds. Answer = {rounds * hp_remaining}')

    rounds, hp_remaining, winning_race = solve_part2(board)
    print(f'Part 2 answer: {winning_race} win with {hp_remaining} hp in {rounds} rounds. Answer = {rounds * hp_remaining}')

def solve_part2(board):
    starting_elves = 10
    elf_attack_pwr = 10
    while True:
        if debug:
            print(f'Running with elf attack {elf_attack_pwr}')
        board_size = len(board)
        units = []
        walls = []
        for i,row in enumerate(board):
            for j,col in enumerate(row):
                if board[i][j] in 'GE':
                    attack_pwr = elf_attack_pwr if board[i][j] == 'E' else 3
                    units.append(Unit(
                        race=board[i][j],
                        pos=(i,j),
                        power=attack_pwr,
                        ))
                elif board[i][j] == '#':
                    walls.append((i,j))

        if debug:
            draw_board(get_board(board_size, walls, units), units)

        rounds = 1
        while True:
            units = play_round(board_size, walls, units)
            units = [unit for unit in units if unit.alive]
            races_left = set([unit.race for unit in units])

            if debug:
                print(f'{rounds}')
                draw_board(get_board(board_size, walls, units), units)

            if len([unit for unit in units if unit.race == 'E']) < starting_elves:
                break
            if len(races_left) == 1:
                return rounds, sum([unit.hp for unit in units]), races_left.pop()
            rounds += 1
        elf_attack_pwr +=1


def solve_part1(board):
    board_size = len(board)
    units = []
    walls = []
    for i,row in enumerate(board):
        for j,col in enumerate(row):
            if board[i][j] in 'GE':
                units.append(Unit(
                    race=board[i][j],
                    pos=(i,j),
                    ))
            elif board[i][j] == '#':
                walls.append((i,j))

    if debug:
        draw_board(get_board(board_size, walls, units), [])

    rounds = 0
    while True:
        units = play_round(board_size, walls, units)
        units = [unit for unit in units if unit.alive]
        races_left = set([unit.race for unit in units])

        if debug:
            print(f'Round {rounds}')
            draw_board(get_board(board_size, walls, units), units)

        if len(races_left) == 1:
            break
        rounds += 1

    return rounds, sum([unit.hp for unit in units]), races_left.pop()

def play_round(board_size, walls, units):
    units = sorted(units, key=lambda unit: (unit.pos[0],unit.pos[1]))
    for unit in units:
        if not unit.alive:
            continue
        targets = [target.pos for target in units if unit.race != target.race and target.alive]
        board = get_board(board_size, walls, units)
        moves_to_enemy = bfs(board, unit.pos, unit.race, targets)
        if len(moves_to_enemy) > 2:
            unit.pos = bfs(board, unit.pos, unit.race, targets)[1]
        do_attack(board, unit, units)
        # draw_board(get_board(board_size, walls, units),units)
    return units

def do_attack(grid, unit, units):
    width = len(grid)
    height = len(grid[0])
    target = 'G' if unit.race == 'E' else 'E'
    x, y = unit.pos
    targets = []

    for x2, y2 in ((x-1,y), (x,y-1), (x,y+1), (x+1,y)):
        for target in units:
            if target.race == unit.race or not target.alive:
                continue
            if 0 <= x2 < width and 0 <= y2 < height and (x2,y2) == target.pos:
                targets.append(target)
    if len(targets) > 0:
        if len(targets) > 1:
            lowest_hp = min([target.hp for target in targets])
            lowest_hp_targets = []
            for target in targets:
                if target.hp == lowest_hp:
                    lowest_hp_targets.append(target)
            targets = sorted(lowest_hp_targets, key=lambda target: (target.pos[0],target.pos[1]))
        target = targets[0]
        target.hp -= unit.power
        if target.hp <= 0:
            target.alive = False

def bfs(grid, start, race, targets):
    wall = '#' + race
    width = len(grid)
    height = len(grid[0])
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x,y) in targets:
            return path
        for x2, y2 in ((x-1,y), (x,y-1), (x,y+1), (x+1,y)):
            if 0 <= x2 < width and 0 <= y2 < height and grid[x2][y2] not in wall and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
    return []

def get_board(size, walls, units):
    board = [['.' for x in range(size)] for y in range(size)]

    for wall in walls:
        board[wall[0]][wall[1]] = '#'
    for unit in units:
        if unit.alive:
            board[unit.pos[0]][unit.pos[1]] = unit.race
    return board

def draw_board(board, units):
    # print('\n'.join([''.join(['{}'.format(item) for item in row])
    #   for row in board]))
    units = sorted(units, key=lambda unit: (unit.pos[0],unit.pos[1]))
    for i, row in enumerate(board):
        print(''.join(row) + '     ' + ' '.join([str(unit.hp) for unit in units if unit.pos[0] == i]))


@dataclass
class Unit:
    race: str
    pos: tuple
    hp: int = 200
    power: int = 3
    alive: bool = True

def get_input_filename(do_small):
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    if do_small:
        input_file += ".small"

    return input_file

if __name__ == '__main__':
    main()
