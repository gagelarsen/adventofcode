from typing import List

from data.day_01_data import EXAMPLE_DATA, PUZZLE_DATA, EXAMPLE_ANSWER_01, EXAMPLE_ANSWER_02, \
    PUZZLE_ANSWER_01, PUZZLE_ANSWER_02
from day_base import AdventDay


INCREASE = 'i'
DECREASE = 'd'


class Day01(AdventDay):
    expected_example_answer_01 = 7
    expected_example_answer_02 = 5
    expected_puzzle_answer_01 = 1292
    expected_puzzle_answer_02 = 1262

    def answer_01(self, depths: List[int], chunk_size: int = 1) -> int:
        adjusted_array = [sum(depths[x:x+chunk_size]) for x in range(len(depths)) if x + chunk_size - 1 < len(depths)]
        measurements = map(lambda x, y: INCREASE if x < y else DECREASE, adjusted_array[:-1], adjusted_array[1:])
        answer = list(measurements).count(INCREASE)
        return answer

    def answer_02(self, depths: List[int]) -> int:
        answer = self.answer_01(depths=depths, chunk_size=3)
        return answer


if __name__ == '__main__':
    day_01 = Day01(EXAMPLE_ANSWER_01, EXAMPLE_ANSWER_02, PUZZLE_ANSWER_01, PUZZLE_ANSWER_02)
    day_01.get_answers(EXAMPLE_DATA, PUZZLE_DATA)
