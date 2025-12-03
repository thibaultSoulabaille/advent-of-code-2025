from itertools import combinations
import utils.aoc_utils as aoc_utils
from utils import check_time


@check_time
def part_1(input_: list[str]) -> int:
    res = 0
    for bank in input_:
        max_jolt = 0
        for comb in combinations(bank, 2):
            jolt = int("".join(comb))
            if jolt > max_jolt:
                max_jolt = jolt
        res += max_jolt
    return res


@check_time
def part_2(input_: list[str]) -> int:
    res = 0
    len_jolt = 12
    for bank in input_:
        jolt = ""
        bank_int = [int(bat) for bat in bank]

        max_bat = bank_int[0]
        max_bat_idx = 1

        for i in range(len_jolt):
            bat_list = bank_int[max_bat_idx : len(bank) + 1 - (len_jolt - i)]

            curr_max_bat_idx = 0
            for bat_idx, bat in enumerate(bat_list):
                if bat > max_bat:
                    max_bat = bat
                    curr_max_bat_idx = bat_idx + 1

            max_bat_idx += curr_max_bat_idx

            jolt += str(max_bat)
            max_bat = 0

        res += int(jolt)
    return res


if __name__ == "__main__":
    input_ = aoc_utils.open_input(day=3, test=False)
    print(f"Part 1: {part_1(input_)}")
    print(f"Part 2: {part_2(input_)}")
