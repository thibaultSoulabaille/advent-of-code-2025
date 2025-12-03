from itertools import combinations
import utils.aoc_utils as aoc_utils
from utils import check_time


@check_time
def part_1(input_: list[str]) -> int:
    res = 0
    for bank in input_:
        max_jolt = 0
        for comb in combinations(bank, 2):
            jolt = int("".join(comb))
            if jolt > max_jolt:
                max_jolt = jolt
        res += max_jolt
    return res


@check_time
def part_2(input_: list[str]) -> int:
    res = 0
    return res


if __name__ == "__main__":
    input_ = aoc_utils.open_input(day=3, test=False)
    print(f"Part 1: {part_1(input_)}")
    print(f"Part 2: {part_2(input_)}")
