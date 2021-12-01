from data.day_02_data import EXAMPLE_DATA, PUZZLE_DATA, EXAMPLE_ANSWER_01, EXAMPLE_ANSWER_02, \
    PUZZLE_ANSWER_01, PUZZLE_ANSWER_02
from day_base import AdventDay


class Day02(AdventDay):

    def answer_01(self, input_data: object) -> object:
        answer = '<no answer>'
        return answer

    def answer_02(self, input_data: object) -> object:
        answer = '<no answer>'
        return answer


if __name__ == '__main__':
    day_02 = Day02(EXAMPLE_ANSWER_01, EXAMPLE_ANSWER_02, PUZZLE_ANSWER_01, PUZZLE_ANSWER_02)
    day_02.get_answers(EXAMPLE_DATA, PUZZLE_DATA)
