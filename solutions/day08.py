"""
Day 08 of the Advent of Code Challenge Code

Author: Gage Larsen
Date: December 7, 2020
"""
from inputs.day08 import puzzle_data, example_data


def puzzle_function(data):
    accumulator = 0
    used_command_indexes = []
    commands = data.split('\n')
    command_index = 0
    while command_index not in used_command_indexes:
        command = commands[command_index]
        used_command_indexes.append(command_index)
        com = command[:3]
        sign = command[4]
        amount = int(command[5:])
        if com == 'acc':
            if sign == '+':
                accumulator += amount
            else:
                accumulator -= amount
            command_index += 1
        elif com == 'jmp':
            if sign == '+':
                command_index += amount
            else:
                command_index -= amount
        elif com == 'nop':
            command_index += 1
    return accumulator


def puzzle_function_fixed(data):
    commands = data.split('\n')
    fixable_commands = {
        # These are swapped intentionally
        'nop': [i for i, x in enumerate(commands) if x.startswith('jmp')],
        'jmp': [i for i, x in enumerate(commands) if x.startswith('nop')]
    }
    for cmd in fixable_commands.keys():
        for index in fixable_commands[cmd]:
            accumulator = 0
            command_index = 0
            used_command_indexes = []
            fixed_commands = [x for i, x in enumerate(commands)]
            fixed_commands[index] = fixed_commands[index].replace(fixed_commands[index][:3], cmd)
            while command_index not in used_command_indexes:
                if command_index == len(fixed_commands):
                    return accumulator
                command = fixed_commands[command_index]
                used_command_indexes.append(command_index)
                com = command[:3]
                sign = command[4]
                amount = int(command[5:])
                if com == 'acc':
                    if sign == '+':
                        accumulator += amount
                    else:
                        accumulator -= amount
                    command_index += 1
                elif com == 'jmp':
                    if sign == '+':
                        command_index += amount
                    else:
                        command_index -= amount
                elif com == 'nop':
                    command_index += 1


def main():
    do_puzzle = True
    data = puzzle_data if do_puzzle else example_data
    answer = puzzle_function(data)
    print(f'The answer to part 1 is: {answer}')
    answer = puzzle_function_fixed(data)
    print(f'The answer to part 2 is: {answer}')


if __name__ == "__main__":
    main()
