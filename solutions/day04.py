"""
Day 04 of the Advent of Code Challenge Code

Author: Gage Larsen
Date: December 3, 2020
"""
import re

from inputs.day04 import puzzle_data, example_data


def passport_is_valid(passport, ignore=None, extended=False):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    if ignore:
        required_fields = [x for x in required_fields if x not in ignore]
    passport_fields = passport.keys()
    if not set(required_fields).issubset(passport_fields):
        return False

    if not extended:
        return True

    # Verify byr
    byr = passport['byr']
    if not byr.isnumeric() or len(byr) != 4 or not 1920 <= int(byr) <= 2002:
        return False
    # Verify iyr
    iyr = passport['iyr']
    if not byr.isnumeric() or len(iyr) != 4 or not 2010 <= int(iyr) <= 2020:
        return False
    # Verify eyr
    eyr = passport['eyr']
    if not byr.isnumeric() or len(eyr) != 4 or not 2020 <= int(eyr) <= 2030:
        return False
    # Verify hgt
    hgt = passport['hgt']
    hgt_pattern = re.compile(r'^\d+(cm|in)$')
    if not bool(hgt_pattern.match(hgt)):
        return False
    if 'cm' in hgt:
        cms = int(hgt.split('cm')[0])
        if not 150 <= cms <= 293:
            return False
    if 'in' in hgt:
        cms = int(hgt.split('in')[0])
        if not 59 <= cms <= 76:
            return False
    # Verify hcl
    hcl = passport['hcl']
    hcl_pattern = re.compile(r'^#[0-9a-fA-F]{6}$')
    if not bool(hcl_pattern.match(hcl)):
        return False
    # Verify ecl
    ecl = passport['ecl']
    if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    # Verify pid
    pid = passport['pid']
    hcl_pattern = re.compile(r'^[0-9]{9}$')
    if not bool(hcl_pattern.match(pid)):
        return False
    return True


def count_valid_passports(puzzle_string, ignore_fields=None, extended=False):
    answer_value = 0
    passport_strings = puzzle_string.split('\n\n')
    passport_pairs = [x.split() for x in passport_strings]
    passports = []
    for passport_pair in passport_pairs:
        passport = {x.split(':')[0]: x.split(':')[1] for x in passport_pair}
        passports.append(passport)
    for passport in passports:
        if passport_is_valid(passport, ignore_fields, extended):
            answer_value += 1
    return answer_value


def main():
    do_puzzle = True
    data = puzzle_data if do_puzzle else example_data
    answer = count_valid_passports(data, ['cid'])
    print(f'The answer to part 1 is: {answer}')
    answer = count_valid_passports(data, ['cid'], extended=True)
    print(f'The answer to part 2 is: {answer}')


if __name__ == '__main__':
    main()
