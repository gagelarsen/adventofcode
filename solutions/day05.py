"""
Day 05 of the Advent of Code Challenge Code

Author: Gage Larsen
Date: December 4, 2020
"""
import re

from inputs.day05 import puzzle_data, example_data


def find_seat_id(row_count, number_front_back, column_count, number_left_right, seat):
    format_pattern = re.compile(r'[FB]{7}[LR]{3}')
    if not bool(format_pattern.match(seat)):
        raise Exception('Bad seat pattern')

    available_rows = [x for x in range(row_count)]
    available_columns = [x for x in range(column_count)]

    for fb in seat[:number_front_back]:
        half_rows = int(len(available_rows)/2)
        if fb is 'F':
            available_rows = available_rows[:half_rows]
        else:
            available_rows = available_rows[half_rows:]
    row = available_rows[0]

    for rl in seat[number_front_back:]:
        half_cols = int(len(available_columns)/2)
        if rl is 'L':
            available_columns = available_columns[:half_cols]
        else:
            available_columns = available_columns[half_cols:]
    col = available_columns[0]

    return (row * 8) + col


def find_missing_seat_id(seat_ids):
    existing_ids = set(seat_ids)
    all_ids = (x for x in range(min(seat_ids), max(seat_ids) + 1))
    missing_ids = list(set(all_ids) - set(existing_ids))
    return missing_ids[0]


def main():
    do_puzzle = True
    seats_for_part_1 = puzzle_data if do_puzzle else example_data
    seat_ids_part_1 = []
    for seat in seats_for_part_1:
        seat_ids_part_1.append(find_seat_id(128, 7, 8, 3, seat))
    print(f'The answer to part 1 is: {max(seat_ids_part_1)}')
    answer = find_missing_seat_id(seat_ids_part_1)
    print(f'The answer to part 2 is: {answer}')


if __name__ == '__main__':
    main()
