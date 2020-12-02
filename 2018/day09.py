#!/usr/local/bin/python3

from collections import defaultdict, deque
from operator import itemgetter
from parse import parse
import os
from sys import exit

do_small = False


def main():
    input_file = get_input_filename(do_small)

    with open(input_file) as f:
        data = f.read().splitlines()

    for line in data:
        players, end_score  = parse('{:d} players; last marble is worth {:d} points', line)
        winner1 = solve_fast(players, end_score)
        print(f'Part1: max score is {winner1[1]} (player {winner1[0] + 1})')
        winner2 = solve_fast(players, end_score*100)
        print(f'Part2: max score is {winner2[1]} (player {winner2[0] + 1})')


def solve_fast(players, turn_count):
    marbles = deque([0])
    player_scores = defaultdict(int)
    turn = 0
    # print(f'players = {players}, last marble = {turn_count}')

    while turn < turn_count:
        turn += 1
        if turn % 23 == 0:
            player = turn % players
            marbles.rotate(-7)
            marble_score = turn + marbles.pop()
            player_scores[player] += marble_score
        else:
            marbles.rotate(2)
            marbles.append(turn)

    winner = max(player_scores.items(), key=itemgetter(1))
    return winner


def solve(players, end_score):
    marbles = [0]
    player_scores = defaultdict(int)
    turn = marble_idx = 0
    no_marbles = 1
    print(f'players = {players}, last marble = {end_score}')

    while turn < end_score:
        # print(turn)
        turn += 1

        if turn % 23 == 0:
            player = turn % players
            marble_remove_idx = marble_idx - 7
            if marble_remove_idx < 0:
                marble_remove_idx = no_marbles + marble_remove_idx
            marble_remove = marbles[marble_remove_idx]
            del marbles[marble_remove_idx]
            marble_score = turn + marble_remove
            player_scores[player] += marble_score
            marble_idx = marble_remove_idx
            no_marbles -= 1
            # print(marble_score)
        else:
            marble_idx = (marble_idx + 2) % no_marbles
            # Append to list instead of starting at pos 0
            if marble_idx == 0:
                marble_idx = no_marbles
            marbles.insert(marble_idx, turn)
            no_marbles += 1
        # print(marbles)

    winner = max(player_scores.items(), key=itemgetter(1))
    return winner

def get_input_filename(do_small):
    day = os.path.basename(__file__)[3:5]
    input_file = "day" + day + ".input"

    if do_small:
        input_file += ".small"

    return input_file

if __name__ == '__main__':
    main()
