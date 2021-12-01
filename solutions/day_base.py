"""
A base class for doing the advent of code challenges.

This file was created on December 01, 2021
"""


class AdventDay(object):
    @staticmethod
    def answer_01(input_data):
        print('Answer 01 must be implemented')
        return '<no answer given>'

    @staticmethod
    def answer_02(input_data):
        print('Answer 02 must be implemented')
        return '<no answer given>'

    def get_answers(self, example_input, puzzle_input):
        """A function used to get the answers for printing the answers to the puzzles."""
        answer = self.answer_01(example_input)
        print(f'The example #1 answer is: {answer}')

        answer = self.answer_01(puzzle_input)
        print(f'The puzzle #1 answer is: {answer}')

        answer2 = self.answer_02(example_input)
        print(f'The example #2 answer is: {answer2}')

        answer2 = self.answer_02(puzzle_input)
        print(f'The puzzle #2 answer is: {answer2}')
