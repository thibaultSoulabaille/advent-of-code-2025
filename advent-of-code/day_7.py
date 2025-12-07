import re
from collections import defaultdict
import utils.aoc_utils as aoc_utils
from utils import check_time


@check_time
def part_1(input_: list[str]) -> int:
    res = 0

    beam_loc = set({input_[0].find("S")})

    for line in input_[1:]:
        if line.find("^") > 0:
            for splitter_idx in re.finditer("\^", line):
                idx = splitter_idx.start()
                if idx in beam_loc:
                    res += 1
                    beam_loc.remove(idx)
                    beam_loc.add(idx + 1)
                    beam_loc.add(idx - 1)
    return res


@check_time
def part_2(input_: list[str]) -> int:
    beam_loc = set({input_[0].find("S")})

    paths = defaultdict(int)
    paths[input_[0].find("S")] = 1

    for line in input_[1:]:
        if line.find("^") > 0:
            for splitter_idx in re.finditer("\^", line):
                idx = splitter_idx.start()
                if idx in beam_loc:
                    paths[idx - 1] += paths[idx]
                    paths[idx + 1] += paths[idx]
                    paths[idx] = 0

                    beam_loc.remove(idx)
                    beam_loc.add(idx + 1)
                    beam_loc.add(idx - 1)

    return sum(paths.values())


if __name__ == "__main__":
    input_ = aoc_utils.open_input(day=7, test=False, as_list=True)
    print(f"Part 1: {part_1(input_)}")
    print(f"Part 2: {part_2(input_)}")
