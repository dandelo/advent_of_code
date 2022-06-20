import lib.commons as commons
import copy

# input_file = commons.get_input_filename()
input_file = 'inputs/day14_small.txt'
input = commons.read_file_to_list(input_file)
polymer = input[0]
pair_insertion_rules = {}
for pair in input[2:]:
    pair = pair.split()
    pair_insertion_rules[pair[0]] = pair[-1]


def step(polymer):
    polymer_copy = copy.deepcopy(polymer)
    for idx in range(len(polymer) - 1):
        pair = polymer[idx:idx+2]
        polymer_copy = polymer_copy[:idx+1+idx] + pair_insertion_rules[pair] + polymer_copy[idx+1+idx:]
    return polymer_copy


def solve(polymer, steps=10):
    polymer_copy = copy.deepcopy(polymer)
    for _ in range(steps):
        polymer_copy = step(polymer_copy)
        print(polymer_copy)
        print()

    letter_counts = [polymer_copy.count(char) for char in set(polymer_copy)]
    return max(letter_counts) - min(letter_counts)


print(solve(polymer))
# print(solve(polymer, 40))
