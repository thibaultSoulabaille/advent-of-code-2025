from math import sqrt
from itertools import combinations

import utils.aoc_utils as aoc_utils
from utils import check_time


def dist(x: list[int], y: list[int]):
    return sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2 + (x[2] - y[2]) ** 2)


@check_time
def part_1(input_: list[str]) -> int:
    box_list = list(map(lambda box: list(map(int, box.split(","))), input_))
    idx_list = list(range(len(box_list)))

    box_comb = combinations(box_list, 2)
    idx_comb = combinations(idx_list, 2)

    box_dist_l = [
        [idx, dist(boxes[0], boxes[1])] for idx, boxes in zip(idx_comb, box_comb)
    ]
    box_dist_l = sorted(box_dist_l, key=lambda x: x[1])[:1000]

    box_cirtcuit_idx = -1
    box_cirtcuit: list[set] = []
    box_circuits_link: dict[int, int] = {}

    for (idx_0, idx_1), _ in box_dist_l:
        if idx_0 not in box_circuits_link.keys():
            if idx_1 not in box_circuits_link.keys():
                box_cirtcuit_idx += 1
                box_circuits_link[idx_0] = box_cirtcuit_idx
                box_circuits_link[idx_1] = box_cirtcuit_idx
                box_cirtcuit.append(set({idx_0, idx_1}))
            else:
                box_circuits_link[idx_0] = box_circuits_link[idx_1]
                box_cirtcuit[box_circuits_link[idx_1]].add(idx_0)
        else:
            if idx_1 not in box_circuits_link.keys():
                box_circuits_link[idx_1] = box_circuits_link[idx_0]
                box_cirtcuit[box_circuits_link[idx_0]].add(idx_1)
            else:
                box_cirtcuit_union = (
                    box_cirtcuit[box_circuits_link[idx_0]]
                    | box_cirtcuit[box_circuits_link[idx_1]]
                )

                box_cirtcuit_idx += 1
                box_cirtcuit[box_circuits_link[idx_0]] = set({})
                box_cirtcuit[box_circuits_link[idx_1]] = set({})

                for idx in box_cirtcuit_union:
                    box_circuits_link[idx] = box_cirtcuit_idx
                box_cirtcuit.append(box_cirtcuit_union)

    box_cirtcuit.sort(key=lambda x: -len(x))

    return len(box_cirtcuit[0]) * len(box_cirtcuit[1]) * len(box_cirtcuit[2])


@check_time
def part_2(input_: list[str]) -> int:
    box_list = list(map(lambda box: list(map(int, box.split(","))), input_))
    idx_list = list(range(len(box_list)))

    box_comb = combinations(box_list, 2)
    idx_comb = combinations(idx_list, 2)

    box_dist_l = [
        [idx, dist(boxes[0], boxes[1])] for idx, boxes in zip(idx_comb, box_comb)
    ]
    box_dist_l = sorted(box_dist_l, key=lambda x: x[1])

    box_cirtcuit_idx = -1
    box_cirtcuit: list[set] = []
    box_circuits_link: dict[int, int] = {}

    for (idx_0, idx_1), _ in box_dist_l:
        if idx_0 not in box_circuits_link.keys():
            if idx_1 not in box_circuits_link.keys():
                box_cirtcuit_idx += 1
                box_circuits_link[idx_0] = box_cirtcuit_idx
                box_circuits_link[idx_1] = box_cirtcuit_idx
                box_cirtcuit.append(set({idx_0, idx_1}))
            else:
                box_circuits_link[idx_0] = box_circuits_link[idx_1]
                box_cirtcuit[box_circuits_link[idx_1]].add(idx_0)
        else:
            if idx_1 not in box_circuits_link.keys():
                box_circuits_link[idx_1] = box_circuits_link[idx_0]
                box_cirtcuit[box_circuits_link[idx_0]].add(idx_1)
            else:
                box_cirtcuit_union = (
                    box_cirtcuit[box_circuits_link[idx_0]]
                    | box_cirtcuit[box_circuits_link[idx_1]]
                )

                box_cirtcuit_idx += 1
                box_cirtcuit[box_circuits_link[idx_0]] = set({})
                box_cirtcuit[box_circuits_link[idx_1]] = set({})

                for idx in box_cirtcuit_union:
                    box_circuits_link[idx] = box_cirtcuit_idx
                box_cirtcuit.append(box_cirtcuit_union)

        if len(box_circuits_link) == len(input_):
            if sum(map(lambda x: len(x) > 0, box_cirtcuit)) == 1:
                return box_list[idx_0][0] * box_list[idx_1][0]

    return 0


if __name__ == "__main__":
    input_ = aoc_utils.open_input(day=8, test=False, as_list=True)
    print(f"Part 1: {part_1(input_)}")
    print(f"Part 2: {part_2(input_)}")
