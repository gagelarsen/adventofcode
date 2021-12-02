from data.day_02_data import EXAMPLE_DATA, PUZZLE_DATA, EXAMPLE_ANSWER_01, EXAMPLE_ANSWER_02, \
    PUZZLE_ANSWER_01, PUZZLE_ANSWER_02
from day_base import AdventDay


class Day02(AdventDay):

    def answer_01(self, input_data: object) -> object:
        x = y = 0

        direction_map = {
            'up': lambda _x, _y, _count: (_x,  _y - _count),
            'down': lambda _x, _y, _count: (_x,  _y + _count),
            'forward': lambda _x, _y, _count: (_x + _count, _y),
            'backward': lambda _x, _y, _count: (_x - _count, _y),
        }

        for item in input_data:
            direction, count = item.split(' ')
            x, y = direction_map[direction](x, y, int(count))
        return x * y

    def answer_02(self, input_data: object) -> object:
        x = y = aim = 0

        direction_map = {
            'up': lambda _x, _y, _aim, _count: (_x,  _y, _aim - _count),
            'down': lambda _x, _y, _aim, _count: (_x,  _y, _aim + _count),
            'forward': lambda _x, _y, _aim, _count: (_x + _count,  _y + (_aim * _count), _aim),
            'backward': lambda _x, _y, _aim, _count: (_x + _count,  _y - (_aim * _count), _aim),
        }

        for item in input_data:
            direction, count = item.split(' ')
            x, y, aim = direction_map[direction](x, y, aim, int(count))
        answer = x * y
        return answer


if __name__ == '__main__':
    day_02 = Day02(EXAMPLE_ANSWER_01, EXAMPLE_ANSWER_02, PUZZLE_ANSWER_01, PUZZLE_ANSWER_02)
    day_02.get_answers(EXAMPLE_DATA, PUZZLE_DATA)
