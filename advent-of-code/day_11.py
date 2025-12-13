import utils.aoc_utils as aoc_utils
from utils import check_time
from functools import lru_cache


@check_time
def day_11(input_: list[str]) -> tuple[int, int]:
    devices_paths = {line.split(":")[0]: line.split(":")[1].split() for line in input_}

    @lru_cache
    def count_paths(start: str, end: str) -> int:
        """use memoized recursive DFS to count paths from given start to finish device"""
        if start == end:
            return 1
        return sum(count_paths(dst, end) for dst in devices_paths.get(start, []))

    ######## PART 1
    res_1 = count_paths("you", "out")

    ######## PART 2
    svr_fft_path = count_paths("svr", "fft")
    fft_dac_path = count_paths("fft", "dac")
    dac_out_path = count_paths("dac", "out")

    svr_dac_path = count_paths("svr", "dac")
    dac_fft_path = count_paths("dac", "fft")
    fft_out_path = count_paths("fft", "out")

    res_2 = (
        svr_fft_path * fft_dac_path * dac_out_path
        + svr_dac_path * dac_fft_path * fft_out_path
    )

    return res_1, res_2


if __name__ == "__main__":
    input_ = aoc_utils.open_input(day=11, test=False, as_list=True)
    part_1, part_2 = day_11(input_)
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")
