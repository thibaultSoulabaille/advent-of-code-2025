import re
import utils.aoc_utils as aoc_utils
from utils import check_time


@check_time
def part_1(input_: list[str]) -> int:
    res = 0

    beam_loc = set({input_[0].find("S")})

    for line in input_[1:]:
        if line.find("^") > 0:
            for splitter_idx in re.finditer("\^", line):
                if splitter_idx.start() in beam_loc:
                    res += 1
                    beam_loc.remove(splitter_idx.start())
                    beam_loc.add(splitter_idx.start() + 1)
                    beam_loc.add(splitter_idx.start() - 1)
    return res


@check_time
def part_2(input_: list[str]) -> int:
    res = 0
    return res


if __name__ == "__main__":
    input_ = aoc_utils.open_input(day=7, test=False, as_list=True)
    print(f"Part 1: {part_1(input_)}")
    print(f"Part 2: {part_2(input_)}")
