from functools import reduce
from operator import mul

import utils.aoc_utils as aoc_utils
from utils import check_time


OPERATIONS_MAP = {
    "+": lambda x: sum(x),
    "*": lambda x: reduce(mul, x),
}


@check_time
def part_1(input_: list[str]) -> int:
    res = 0

    numbers_l = map(str.split, input_[:-1])
    operations = input_[-1].split()

    res_list = []
    for numbers in numbers_l:
        if len(res_list) == 0:
            res_list = list(map(int, numbers))
        else:
            for j, x in enumerate(map(int, numbers)):
                res_list[j] = OPERATIONS_MAP[operations[j]]((res_list[j], x))

    res = sum(res_list)
    return res


@check_time
def part_2(input_: list[str]) -> int:
    res = 0
    return res


if __name__ == "__main__":
    input_ = aoc_utils.open_input(day=6, test=False, as_list=True)
    print(f"Part 1: {part_1(input_)}")
    print(f"Part 2: {part_2(input_)}")
