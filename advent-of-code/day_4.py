import utils.aoc_utils as aoc_utils
from utils import check_time


@check_time
def part_1(input_: list[str]) -> int:
    res = 0

    input_int = [list(map(int, line)) for line in input_]

    grid_w, grid_h = len(input_[0]), len(input_)

    input_int.insert(0, [0] * grid_w)
    input_int.append([0] * grid_w)

    for i, line in enumerate(input_int[1 : grid_h + 1]):
        for j, roll in enumerate(line):
            if roll == 0:
                continue

            total = 0
            if j == 0:
                total += sum(input_int[i][:2]) + sum(input_int[i + 2][:2]) + line[j + 1]
            elif j == grid_w - 1:
                total += (
                    sum(input_int[i][grid_w - 2 :])
                    + sum(input_int[i + 2][grid_w - 2 :])
                    + line[j - 1]
                )
            else:
                total += (
                    sum(input_int[i][j - 1 : j + 2])
                    + sum(input_int[i + 2][j - 1 : j + 2])
                    + line[j - 1]
                    + line[j + 1]
                )

            res += total < 4

    return res


@check_time
def part_2(input_: list[str]) -> int:
    res = 0
    return res


if __name__ == "__main__":
    input_ = aoc_utils.open_input(day=4, test=False, as_list=False)
    input_ = input_.replace(".", "0")
    input_ = input_.replace("@", "1")
    input_ = input_.splitlines()

    print(f"Part 1: {part_1(input_)}")
    print(f"Part 2: {part_2(input_)}")
