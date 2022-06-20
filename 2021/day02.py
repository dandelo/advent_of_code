import lib.commons as commons

input_file = commons.get_input_filename()
input = commons.read_file_to_list(input_file)


def part_one(input):
    depth = horizontal_pos = 0
    for instruction in input:
        direction, amount = instruction.split()
        amount = int(amount)
        if direction == 'forward':
            horizontal_pos = horizontal_pos + amount
        elif direction == 'down':
            depth = depth + amount
        elif direction == 'up':
            depth = depth - amount
    return depth * horizontal_pos


def part_two(input):
    depth = horizontal_pos = aim = 0
    for instruction in input:
        direction, amount = instruction.split()
        amount = int(amount)
        if direction == 'forward':
            horizontal_pos = horizontal_pos + amount
            depth = depth + (aim * amount)
        elif direction == 'down':
            aim = aim + amount
        elif direction == 'up':
            aim = aim - amount
    return depth * horizontal_pos


print(part_one(input))
print(part_two(input))
