import lib.commons as commons
import networkx as nx

input_file = commons.get_input_filename()
with open(input_file) as myfile:
    edges = [line.strip().split('-') for line in myfile]

G = nx.Graph()
for edge in edges:
    G.add_edge(*edge)


def part_one(G, n, visited, end='end'):
    if n == end:
        return 1
    foo = visited.copy()
    foo.add(n)
    return sum(part_one(G, neighbour, foo) for neighbour in nx.neighbors(G, n)
               if neighbour.isupper() or neighbour not in visited)


def part_two(G, n, visited, visited_small_cave_twice, end='end'):
    if n == end:
        return 1
    foo = visited.copy()
    foo.add(n)

    count = 0
    for neighbour in nx.neighbors(G, n):
        if neighbour.isupper() or neighbour not in visited:
            count += part_two(G, neighbour, foo, visited_small_cave_twice)
        elif not visited_small_cave_twice and neighbour not in {'start', 'end'}:
            count += part_two(G, neighbour, foo, True)

    return count


print(part_one(G, 'start', set()))
print(part_two(G, 'start', set(), False))
