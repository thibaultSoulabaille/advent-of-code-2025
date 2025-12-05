import utils.aoc_utils as aoc_utils
from utils import check_time


def preprocess_input_1(input_: str) -> tuple[list[str], list[str]]:
    id_ranges, ids = map(str.splitlines, input_.split("\n\n"))

    ids.sort(key=lambda id_: int(id_))
    id_ranges.sort(key=lambda id_range: int(id_range.split("-")[0]))

    return id_ranges, ids


def preprocess_input_2(input_: str):
    id_ranges = [list(map(int, id_range.split("-"))) for id_range in input_.split("\n\n")[0].splitlines()]
    id_ranges.sort()
    return id_ranges


def check_id(id_: str, id_ranges: list[str]) -> int:
    for id_range in id_ranges:
        if int(id_) >= int(id_range.split("-")[0]) and int(id_) <= int(id_range.split("-")[1]):
            return 1
    return 0


@check_time
def part_1(input_: str) -> int:
    id_ranges, ids = preprocess_input_1(input_)
    res = sum(map(lambda id_: check_id(id_, id_ranges), ids))

    return res


@check_time
def part_2(input_: str) -> int:
    id_ranges = preprocess_input_2(input_)

    merged_ranges = [id_ranges[0]]
    for id_range in id_ranges[1:]:
        if id_range[0] > merged_ranges[-1][1]:
            merged_ranges.append(id_range)
        else:
            merged_ranges[-1][1] = max(merged_ranges[-1][1], id_range[1])

    res = sum(id_range[1] - id_range[0] + 1 for id_range in merged_ranges)

    return res


if __name__ == "__main__":
    input_ = aoc_utils.open_input(day=5, test=False, as_list=False)
    print(f"Part 1: {part_1(input_)}")
    print(f"Part 2: {part_2(input_)}")
