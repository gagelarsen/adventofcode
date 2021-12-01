from typing import List

from data.day_01_data import *
from day_base import AdventDay


INCREASE = 'i'
DECREASE = 'd'


class Day01(AdventDay):

    def answer_01(self, depths: List[int]) -> int:
        measurements = map(lambda x, y: INCREASE if x < y else DECREASE, depths[:-1], depths[1:])
        answer = list(measurements).count(INCREASE)
        return answer

    def answer_02(self, depths: List[int]) -> int:
        summed_measurements = map(lambda x, y, z: x + y + z, depths[0:-2], depths[1:-1], depths[2:])
        answer = self.answer_01(list(summed_measurements))
        return answer


if __name__ == '__main__':
    Day01().get_answers(EXAMPLE_DEPTHS, PUZZLE_DEPTHS)
