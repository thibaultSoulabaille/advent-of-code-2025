import utils.aoc_utils as aoc_utils
from utils import check_time
from itertools import combinations


@check_time
def part_1(input_: list[str]) -> int:
    tiles = [list(map(int, line.split(","))) for line in input_]

    return max(
        (abs(t1[0] - t0[0]) + 1) * (abs(t1[1] - t0[1]) + 1)
        for (t0, t1) in combinations(tiles, 2)
    )


@check_time
def part_2(input_: list[str]) -> int:
    res = 0
    return res


if __name__ == "__main__":
    input_ = aoc_utils.open_input(day=9, test=False, as_list=True)
    print(f"Part 1: {part_1(input_)}")
    print(f"Part 2: {part_2(input_)}")
