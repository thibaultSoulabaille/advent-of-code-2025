import utils.aoc_utils as aoc_utils
from utils import check_time
from itertools import combinations, pairwise


@check_time
def part_1(input_: list[str]) -> int:
    tiles = [list(map(int, line.split(","))) for line in input_]

    return max(
        (abs(t1[0] - t0[0]) + 1) * (abs(t1[1] - t0[1]) + 1)
        for (t0, t1) in combinations(tiles, 2)
    )


@check_time
def part_2(input_: list[str]) -> int:
    tiles = [list(map(int, line.split(","))) for line in input_]

    x_set = sorted(set(t[0] for t in tiles))
    y_set = sorted(set(t[1] for t in tiles))

    edges = list(pairwise(tiles))
    edges.append((tiles[-1], tiles[0]))

    def is_inside(x, y):
        count = 0
        for (x0, y0), (x1, y1) in edges:
            y0s, y1s = sorted((y0, y1))
            if x0 == x1 and x0 >= x and y0s <= y <= y1s:
                count += 1
        return count % 2

    grid: list[list[int]] = []
    for x in pairwise(x_set):
        grid_line = []
        for y in pairwise(y_set):
            grid_line.append(is_inside((x[0] + x[1]) // 2, (y[0] + y[1]) // 2))
        grid.append(grid_line)

    x_idx = {x: i for i, x in enumerate(x_set)}
    y_idx = {y: i for i, y in enumerate(y_set)}

    area_max = 0
    for (x0, y0), (x1, y1) in combinations(tiles, 2):
        if x0 == x1 or y0 == y1:
            continue

        x0s, x1s = sorted((x0, x1))
        y0s, y1s = sorted((y0, y1))

        tot_count = 0
        in_count = 0
        for x in x_set[x_idx[x0s] : x_idx[x1s]]:
            for y in y_set[y_idx[y0s] : y_idx[y1s]]:
                tot_count += 1
                in_count += grid[x_idx[x]][y_idx[y]]

        if tot_count == in_count:
            area = (abs(x1 - x0) + 1) * (abs(y1 - y0) + 1)
            if area > area_max:
                area_max = area

    return area_max


if __name__ == "__main__":
    input_ = aoc_utils.open_input(day=9, test=False, as_list=True)
    print(f"Part 1: {part_1(input_)}")
    print(f"Part 2: {part_2(input_)}")
