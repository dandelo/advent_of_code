import lib.commons as commons
import numpy as np

input_file = commons.get_input_filename()
lines = commons.read_file_to_list(input_file)
all_numbers_to_draw = lines[0].split(',')
board_size = 5

bingo_cards = []
for i in range(2, len(lines), board_size+1):
    bingo_card = np.array([
        commons.line_to_list(lines[i]),
        commons.line_to_list(lines[i+1]),
        commons.line_to_list(lines[i+2]),
        commons.line_to_list(lines[i+3]),
        commons.line_to_list(lines[i+4])
    ])
    bingo_cards.append(bingo_card)


def part_one():
    for i in range(5, len(all_numbers_to_draw)):
        drawn_numbers = all_numbers_to_draw[:i]
        for bingo_card in bingo_cards:
            for j in range(board_size):
                hoz_line = bingo_card[j]
                ver_line = bingo_card[:, j]
                if all(x in drawn_numbers for x in hoz_line):
                    unmarked_numbers = [int(x) for x in bingo_card.flatten() if x not in drawn_numbers]
                    return sum(unmarked_numbers) * int(drawn_numbers[-1])
                if all(x in drawn_numbers for x in ver_line):
                    return


def part_two():
    losing_board_idx = losing_board = None
    board_idxs_yet_to_win = set(range(len(bingo_cards)))
    for i in range(5, len(all_numbers_to_draw)):
        drawn_numbers = all_numbers_to_draw[:i]
        for board_idx, bingo_card in enumerate(bingo_cards):
            for j in range(board_size):
                hoz_line = bingo_card[j]
                ver_line = bingo_card[:, j]
                if all(x in drawn_numbers for x in hoz_line):
                    if board_idx == losing_board_idx:
                        unmarked_numbers = [int(x) for x in losing_board.flatten() if x not in drawn_numbers]
                        return sum(unmarked_numbers) * int(drawn_numbers[-1])
                    if board_idx in board_idxs_yet_to_win:
                        board_idxs_yet_to_win.remove(board_idx)
                    break
                if all(x in drawn_numbers for x in ver_line):
                    if board_idx == losing_board_idx:
                        unmarked_numbers = [int(x) for x in losing_board.flatten() if x not in drawn_numbers]
                        return sum(unmarked_numbers) * int(drawn_numbers[-1])
                    if board_idx in board_idxs_yet_to_win:
                        board_idxs_yet_to_win.remove(board_idx)
                    break
            if not losing_board_idx and len(board_idxs_yet_to_win) == 1:
                losing_board_idx = list(board_idxs_yet_to_win)[0]
                losing_board = bingo_cards[losing_board_idx]


print(part_one())
print(part_two())
