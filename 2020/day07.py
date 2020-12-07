#!/usr/local/bin/python3

from parse import parse
import networkx as nx
import os


def main():
    bags_graph = get_bags_graph()

    print(f'Part 1 answer: {len(nx.ancestors(bags_graph,"shiny gold"))}')


def get_bags_graph():
    G = nx.DiGraph()
    with open(get_input_filename()) as f:
        for line in f.readlines():
            bags = line.rstrip('.\n').replace('bags', 'bag').split(" bag contain")
            container_bag = bags[0]
            if bags[1] == ' no other bag':
                continue

            contained_bags = bags[1].split(",")
            for contained_bag in contained_bags:
                bag_count, bag_type = parse(' {:d} {} bag', contained_bag)
                G.add_edge(container_bag, bag_type, weight=bag_count)

    return G


def get_input_filename():
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    return input_file


if __name__ == '__main__':
    main()
