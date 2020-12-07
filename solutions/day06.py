"""
Day 06 of the Advent of Code Challenge

Author: Gage Larsen
Date: December 5, 2020
"""
import functools

from inputs.day06 import puzzle_data, example_data


def main():
    do_puzzle = True
    groups = puzzle_data if do_puzzle else example_data
    yes_count = sum([len(x) for x in [functools.reduce(lambda a, b: set(list(a)) | set(list(b)), y) for y in [x for x in [x.split() for x in groups.split('\n\n')]]]])
    print(f'The answer to part 1 is: {yes_count}')
    yes_count = sum([len(x) for x in [functools.reduce(lambda a, b: set(list(a)) & set(list(b)), y) for y in [x for x in [x.split() for x in groups.split('\n\n')]]]])
    print(f'The answer to part 2 is: {yes_count}')


if __name__ == '__main__':
    main()
