import utils.aoc_utils as aoc_utils
from utils import check_time


OPERATIONS_MAP = {
    "+": lambda x, y: x + y,
    "*": lambda x, y: x * y,
}

DEFAULT_OPERATION_VAL = {
    "+": 0,
    "*": 1,
}


@check_time
def part_1(input_: list[str]) -> int:
    res = 0

    numbers_l = map(str.split, input_[:-1])
    operations = input_[-1].split()

    res_list = []
    for numbers in numbers_l:
        if len(res_list) == 0:
            res_list = list(map(int, numbers))
        else:
            for j, x in enumerate(map(int, numbers)):
                res_list[j] = OPERATIONS_MAP[operations[j]](res_list[j], x)

    res = sum(res_list)
    return res


@check_time
def part_2(input_: list[str]) -> int:
    res = 0

    operations = input_[-1]
    numbers_l = input_[:-1]

    operation_res = 0

    for i, char in enumerate(operations):
        if char != " ":
            res += operation_res
            operation = OPERATIONS_MAP[char]
            operation_res = DEFAULT_OPERATION_VAL[char]

        operation_input = "".join(line[i] for line in numbers_l).strip()
        if operation_input != "":
            operation_res = operation(operation_res, int(operation_input))

    res += operation_res

    return res


if __name__ == "__main__":
    input_ = aoc_utils.open_input(day=6, test=False, as_list=True)
    print(f"Part 1: {part_1(input_)}")
    print(f"Part 2: {part_2(input_)}")
