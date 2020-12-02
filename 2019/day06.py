import os
import networkx as nx


def main():
    input_file = get_input_filename()

    with open(input_file) as f:
        input = [(x,y) for x,y in [el.split(')') for el in f.read().splitlines()]]
    solve(input)
    solve2(input)

def solve(map):
    g = nx.DiGraph()
    for orbit in map:
        g.add_edge(orbit[1], orbit[0])
    print(sum(len(nx.ancestors(g, n)) for n in g.nodes))

def solve2(map):
    g = nx.Graph()
    for orbit in map:
        g.add_edge(orbit[1], orbit[0])
    print(len(nx.shortest_path(g, 'YOU', 'SAN')) - 3)

def get_input_filename(do_small = False):
    day = os.path.basename(__file__)[3:5]
    input_file = "inputs/day" + day + ".input"

    if do_small:
        input_file += ".small"

    return input_file


if __name__ == '__main__':
    main()
