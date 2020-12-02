import os
import sys
import re
from queue import Queue
from math import ceil

component_rx = re.compile(r'(\d+) (\w+)')

def main():
    recipes = {}
    input_file = get_input_filename()
    with open(input_file) as f:
        for line in f:
            inputstr, output = line.rstrip().split(' => ')
            inputs = inputstr.split(', ')
            output_chem = parse_component(output)
            input_chems = [parse_component(input) for input in inputs]
            # chemical_quantitiy, chemical_name = chemical.split(' ')
            # components = components.split(', ')
            recipes[output_chem.name] = Recipe(input_chems, output_chem)

    solve1(recipes)
    solve2(recipes)


def solve1(recipes):
    ans = make_fuel(1, recipes)
    print(f'Answer to part 1: {ans}')

def solve2(recipes):
    upper_bound = None
    lower_bound = 1
    ore_capacity = 1000000000000
    while lower_bound + 1 != upper_bound:
        if upper_bound is None:
            guess = lower_bound * 2
        else:
            guess = (upper_bound + lower_bound) // 2

        ore_needed = make_fuel(guess, recipes)
        if ore_needed > ore_capacity:
            upper_bound = guess
        else:
            lower_bound = guess

    print(f'Answer to part 2: {guess}')

def make_fuel(quantity, recipes):
    orders = Queue()
    ore_required = 0
    inventory = {}
    orders.put(Chemial('FUEL', quantity))

    while not orders.empty():
        order = orders.get()
        if order.name == 'ORE':
            ore_required += order.quantity
        elif order.name in inventory and order.quantity < inventory[order.name].quantity:
            inventory[order.name].quantity -= order.quantity
        else:
            if order.name in inventory:
                quantity_req = order.quantity - inventory[order.name].quantity
            else:
                quantity_req = order.quantity
            recipe = recipes[order.name].clone()
            batches = ceil(quantity_req / recipe.output_chemical.quantity)

            for chem in recipe.input_chemicals:
                orders.put(Chemial(chem.name, chem.quantity * batches))
            leftover_amount = batches * recipe.output_chemical.quantity - quantity_req
            inventory[order.name] = recipe.output_chemical.clone()
            inventory[order.name].quantity = leftover_amount
    return ore_required


def parse_component(s):
    match = component_rx.search(s)
    groups = match.groups()
    return Chemial(groups[1], int(groups[0]))

class Chemial:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.quantity} {self.name}"

    def __repr__(self):
        return f"{self.quantity} {self.name}"

    def __eq__(self, other):
        if isinstance(other, Chemial):
            return self.name == other.name
        return False
    def clone(self):
        return Chemial(self.name, self.quantity)

class Recipe:
    def __init__(self, input_chemicals, output_chemical):
        self.input_chemicals = [input.clone() for input in input_chemicals]
        self.output_chemical = output_chemical

    def __str__(self):
        return f"{self.input_chemicals} => {self.output_chemical}"

    def __repr__(self):
        return f"{self.input_chemicals} => {self.output_chemical}"

    def clone(self):
        return Recipe(self.input_chemicals, self.output_chemical)

def get_input_filename(do_small = False):
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    if do_small:
        input_file += ".small"

    return input_file


if __name__ == '__main__':
    main()
