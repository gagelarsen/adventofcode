"""
Day 02 of the Advent of Code Challenge Code

Author: Gage Larsen
Date: December 2, 2020
"""
from inputs.day02 import example_data, puzzle_data


def find_valid_passwords(list_of_passwords):
    valid_passwords = []
    for password_string in list_of_passwords:
        policy, letter, password = password_string.split(' ')
        char_min, char_max = policy.split('-')
        letter_count = password.count(letter[0])
        if int(char_min) <= letter_count <= int(char_max):
            valid_passwords.append(password)
    return valid_passwords


def find_valid_passwords_2(list_of_passwords):
    valid_passwords = []
    for password_string in list_of_passwords:
        policy, letter, password = password_string.split(' ')
        first_occ, second_occ = policy.split('-')
        if (password[int(first_occ) - 1] == letter[0] and password[int(second_occ) - 1] != letter[0]) or \
                password[int(first_occ) - 1] != letter[0] and password[int(second_occ) - 1] == letter[0]:
            valid_passwords.append(password)
    return valid_passwords


def main():
    do_puzzle = True
    passwords = puzzle_data if do_puzzle else example_data
    valid_passwords = find_valid_passwords(passwords)
    print(f'The answer to part 1 is: {len(valid_passwords)}')
    new_valid_passwords = find_valid_passwords_2(passwords)
    print(f'The answer to part 2 is: {len(new_valid_passwords)}')


if __name__ == '__main__':
    main()
