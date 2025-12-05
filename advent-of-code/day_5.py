import utils.aoc_utils as aoc_utils
from utils import check_time


def preprocess_input(input_: str):
    id_ranges, ids = map(str.splitlines, input_.split('\n\n'))

    ids.sort(key=lambda id_: int(id_))
    id_ranges.sort(key=lambda id_range: int(id_range.split('-')[0]))

    return id_ranges, ids


def check_id(id_: str, id_ranges: list[str]) -> int:
    for id_range in id_ranges:
        if int(id_) >= int(id_range.split('-')[0]) and int(id_) <= int(id_range.split('-')[1]):
            return 1
    return 0


@check_time
def part_1(input_: str) -> int:
    id_ranges, ids = preprocess_input(input_)
    res = sum(map(lambda id_: check_id(id_, id_ranges), ids))

    return res


@check_time
def part_2(input_: list[str]) -> int:
    res = 0
    return res


if __name__ == "__main__":
    input_ = aoc_utils.open_input(day=5, test=False, as_list=False)
    print(f"Part 1: {part_1(input_)}")
    print(f"Part 2: {part_2(input_)}")
