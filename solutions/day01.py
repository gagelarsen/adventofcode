"""
Day 01 of the Advent of Code Challenge Code

Author: Gage Larsen
Date: December 2, 2020
"""
from inputs.day01 import example_data, puzzle_data


def find_two_numbers_that_sum_to(numbers, sum_to):
    for x in numbers:
        for y in numbers:
            if x + y == sum_to:
                return x, y


def find_three_numbers_that_sum_to(numbers, sum_to):
    for x in numbers:
        for y in numbers:
            if x + y > sum_to:
                continue
            for z in numbers:
                if x + y + z == sum_to:
                    return x, y, z


def main():
    do_puzzle = True
    numbers = puzzle_data if do_puzzle else example_data
    sum_to = 2020
    x, y = find_two_numbers_that_sum_to(numbers, sum_to)
    print(f'The answer to part 1 is: {x * y}')
    x, y, z = find_three_numbers_that_sum_to(numbers, sum_to)
    print(f'The answer to part 2 is: {x * y * z}')


if __name__ == '__main__':
    main()
