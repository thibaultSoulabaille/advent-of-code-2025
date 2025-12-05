import utils.aoc_utils as aoc_utils
from utils import check_time


@check_time
def part_1(input_: list[str]) -> int:
    res = 0
    pos = 50
    for move in input_:
        direction = move[0]
        distance = int(move[1:])

        if direction == "L":
            distance *= -1

        pos = (pos + distance) % 100
        res += (pos == 0)
    return res


@check_time
def part_2(input_: list[str]) -> int:
    res = 0
    pos = 50
    for move in input_:
        direction = move[0]
        distance = int(move[1:])

        if direction == "L":
            distance *= -1

        q = 0
        if pos == 0:
            q, _ = divmod(abs(pos + distance), 100)
        elif distance > 0:
            q, _ = divmod(pos + distance, 100)
        else:
            q, _ = divmod(100 - pos + abs(distance), 100)
        res += abs(q)

        pos = (pos + distance) % 100
    return res


if __name__ == "__main__":
    input_ = aoc_utils.open_input(day=1, test=False)
    print(f"Part 1: {part_1(input_)}")
    print(f"Part 2: {part_2(input_)}")
