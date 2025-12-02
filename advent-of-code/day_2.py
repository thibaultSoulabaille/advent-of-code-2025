import utils.aoc_utils as aoc_utils
from utils import split_string_by_block


def part_1(input_: list[str]) -> int:
    res = 0
    for id_range in input_[0].split(","):
        id_min, id_max = id_range.split("-")
        id_len = 2
        for id_ in range(int(id_min), int(id_max) + 1):
            id_len = len(str(id_))
            if id_len % 2 != 0:
                continue
            divider = int("1" + "0" * (id_len // 2 - 1) + "1")
            if id_ % divider == 0:
                res += id_
    return res


def part_2(input_: list[str]) -> int:
    res = 0
    for id_range in input_[0].split(","):
        id_min, id_max = id_range.split("-")
        for id_ in range(int(id_min), int(id_max) + 1):
            id_len = len(str(id_))

            for pattern_len in range(1, id_len // 2 + 1):
                split_id = split_string_by_block(str(id_), pattern_len)
                if len(set(split_id)) == 1:
                    if len(set(split_id)) == 1:
                        res += id_
                        break
    return res


if __name__ == "__main__":
    input_ = aoc_utils.open_input(day=2, test=False)
    print(f"Part 1: {part_1(input_)}")
    print(f"Part 2: {part_2(input_)}")
