import utils.aoc_utils as aoc_utils
from utils import check_time


@check_time
def part_1(input_: list[str]) -> int:
    devices_paths_dict = {
        line.split(":")[0]: line.split(":")[1].split() for line in input_
    }
    res = 0

    paths = ["you"]
    while len(paths) > 0:
        device = paths.pop(0)
        if device == "out":
            res += 1
        else:
            paths.extend(devices_paths_dict[device])
    return res


@check_time
def part_2(input_: list[str]) -> int:
    res = 0
    return res


if __name__ == "__main__":
    input_ = aoc_utils.open_input(day=11, test=False, as_list=True)
    print(f"Part 1: {part_1(input_)}")
    print(f"Part 2: {part_2(input_)}")
