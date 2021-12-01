"""
A base class for doing the advent of code challenges.

This file was created on December 01, 2021
"""


class AdventDay(object):

    def __init__(self, example_answer_01=None, example_answer_02=None,
                 puzzle_answer_01=None, puzzle_answer_02=None):
        self.expected_example_answer_01 = example_answer_01
        self.expected_example_answer_02 = example_answer_02
        self.expected_puzzle_answer_01 = puzzle_answer_01
        self.expected_puzzle_answer_02 = puzzle_answer_02

    def answer_01(self, input_data):
        print('Answer 01 must be implemented')
        return '<no answer given>'

    def answer_02(self, input_data):
        print('Answer 02 must be implemented')
        return '<no answer given>'

    def get_answers(self, example_input, puzzle_input):
        """A function used to get the answers for printing the answers to the puzzles."""
        answer = self.answer_01(example_input)
        if self.expected_example_answer_01:
            assert self.expected_example_answer_01 == answer
        print(f'The example #1 answer is: {answer}')

        answer = self.answer_01(puzzle_input)
        if self.expected_puzzle_answer_01:
            assert self.expected_puzzle_answer_01 == answer
        print(f'The puzzle #1 answer is: {answer}')

        answer2 = self.answer_02(example_input)
        if self.expected_example_answer_02:
            assert self.expected_example_answer_02 == answer2
        print(f'The example #2 answer is: {answer2}')

        answer2 = self.answer_02(puzzle_input)
        if self.expected_puzzle_answer_02:
            assert self.expected_puzzle_answer_02 == answer2
        print(f'The puzzle #2 answer is: {answer2}')
