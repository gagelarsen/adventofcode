from typing import List

from data.day_03_data import EXAMPLE_DATA, PUZZLE_DATA, EXAMPLE_ANSWER_01, EXAMPLE_ANSWER_02, \
    PUZZLE_ANSWER_01, PUZZLE_ANSWER_02
from day_base import AdventDay


class Day03(AdventDay):

    def answer_01(self, input_data: List[str]) -> object:

        splits = list(zip(*input_data))

        if len(splits) <= 0:
            return '<no answer>'

        g_rate = ''.join(['1' if x.count('1') > x.count('0') else '0'for x in splits])
        e_rate = ''.join(['1' if x.count('1') < x.count('0') else '0' for x in splits])

        return int(g_rate, 2) * int(e_rate, 2)

    def answer_02(self, input_data: List[str]) -> object:

        oxygen = self._answer_02_helper(input_data, 0, True)
        co2 = self._answer_02_helper(input_data, 0, False)
        return int(oxygen, 2) * int(co2, 2)

    def _answer_02_helper(self, input_data: List[str], index: int = 0, common: bool = True) -> object:
        if len(input_data) == 1 or index >= len(input_data[0]):
            return input_data[0]

        splits = list(zip(*input_data))

        if common:
            keep = '1' if splits[index].count('1') >= splits[index].count('0') else '0'
        else:
            keep = '0' if splits[index].count('1') >= splits[index].count('0') else '1'

        filtered_data = [x for x in input_data if x[index] == keep]

        return self._answer_02_helper(filtered_data, index + 1, common)


if __name__ == '__main__':
    day_03 = Day03(EXAMPLE_ANSWER_01, EXAMPLE_ANSWER_02, PUZZLE_ANSWER_01, PUZZLE_ANSWER_02)
    day_03.get_answers(EXAMPLE_DATA, PUZZLE_DATA)
