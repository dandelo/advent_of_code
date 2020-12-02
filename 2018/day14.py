#!/usr/local/bin/python3

do_small = False

def main():
    recipes = [3,7]
    if do_small:
        recipe_count = 9
        recipe_ans = '59414'
    else:
        recipe_count = 430971
        recipe_ans = '430971'

    ans1 = solve_part1(recipes,recipe_count)
    print(f'Part 1 answer: {ans1}')

    ans2 = solve_part2(recipe_ans)
    print(f'Part 2 answer: {ans2}')


def solve_part1(recipes, recipe_count):
    recipes = recipes.copy()
    elf_1_idx = 0
    elf_2_idx = 1
    while len(recipes) < recipe_count + 10:
        new_recipe = recipes[elf_1_idx] + recipes[elf_2_idx]
        recipes.extend([int(d) for d in str(new_recipe)])
        elf_1_idx = (elf_1_idx + recipes[elf_1_idx] + 1) % len(recipes)
        elf_2_idx = (elf_2_idx + recipes[elf_2_idx] + 1) % len(recipes)
    ans = recipes[recipe_count:recipe_count + 10]
    return ''.join(str(x) for x in ans)

def solve_part2(recipe_ans):
    recipes = '37'
    recipe_ans_size = len(recipe_ans) + 1
    elf_1_idx = 0
    elf_2_idx = 1
    while recipe_ans not in recipes[-recipe_ans_size:]:
        new_recipe = str(int(recipes[elf_1_idx]) + int(recipes[elf_2_idx]))
        recipes += new_recipe
        elf_1_idx = (elf_1_idx + int(recipes[elf_1_idx]) + 1) % len(recipes)
        elf_2_idx = (elf_2_idx + int(recipes[elf_2_idx]) + 1) % len(recipes)
    ans = recipes.index(recipe_ans)
    return ans

if __name__ == '__main__':
    main()
