import utils.aoc_utils as aoc_utils
from utils import check_time


def preprocess_input(input_: list[str]) -> list[list[int]]:
    input_preproc = [list(map(int, line)) for line in input_]

    input_preproc.insert(0, [0] * len(input_[0]))
    input_preproc.append([0] * len(input_[0]))

    return input_preproc


def count_grid(grid: list[list[int]]) -> int:
    return sum([sum(row) for row in grid])


@check_time
def part_1(input_: list[str]) -> int:
    res = 0

    input_int = preprocess_input(input_)

    grid_w, grid_h = len(input_[0]), len(input_)

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

    input_int = preprocess_input(input_)
    grid_count = count_grid(input_int)

    grid_w, grid_h = len(input_[0]), len(input_)

    while True:
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

                if total < 4:
                    res += 1
                    input_int[i + 1][j] = 0

        curr_count_grid = count_grid(input_int)
        if curr_count_grid == grid_count:
            break
        grid_count = curr_count_grid

    return res


if __name__ == "__main__":
    input_ = aoc_utils.open_input(day=4, test=False, as_list=False)
    input_ = input_.replace(".", "0")
    input_ = input_.replace("@", "1")
    input_ = input_.splitlines()

    print(f"Part 1: {part_1(input_)}")
    print(f"Part 2: {part_2(input_)}")
