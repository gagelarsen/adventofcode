"""
Day 03 of the Advent of Code Challenge Code

Author: Gage Larsen
Date: December 2, 2020
"""
from inputs.day03 import example_data, part_two_slopes_example_data, puzzle_data


TREE = "#"
OPEN = '.'


def count_trees(tree_map, down, right):
    global TREE
    trees_encountered = 0
    cur_x = cur_y = 0
    while cur_y < len(tree_map):
        if tree_map[cur_y][cur_x] == TREE:
            trees_encountered += 1
        cur_x += right
        if cur_x >= len(tree_map[0]):
            cur_x -= len(tree_map[0])
        cur_y += down
    return trees_encountered


def main():
    do_puzzle = True
    data = puzzle_data if do_puzzle else example_data
    encountered_trees = count_trees(data, 1, 3)
    print(f'The answer to part 1 is: {encountered_trees}')

    tree_encounters = []
    for slope in part_two_slopes_example_data:
        tree_encounters.append(count_trees(data, slope[1], slope[0]))
    product_of_encounters = 1
    for x in tree_encounters:
        product_of_encounters *= x
    print(f"The answer to part 2 is: {product_of_encounters}")


if __name__ == '__main__':
    main()
