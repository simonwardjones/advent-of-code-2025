import pathlib

DATA_DIR = pathlib.Path(__file__).parent.parent.parent / "data"


def load_raw_data() -> str:
    data_file_name = "data_sample_1.txt"
    data_file_name = "data.txt"
    with open(DATA_DIR / "day_04" / data_file_name) as f:
        raw_data = f.read()
    return raw_data


def pass_data(raw_data: str) -> list[list[str]]:
    return {
        (i, j): val
        for i, row in enumerate(raw_data.splitlines())
        for j, val in enumerate(row)
    }


def offsets(i, j, grid):
    return [
        (i + di, j + dj)
        for di in [-1, 0, 1]
        for dj in [-1, 0, 1]
        if (di != 0 or dj != 0) and (i + di, j + dj) in grid
    ]


def part_1() -> None:
    raw_data = load_raw_data()
    grid = pass_data(raw_data)
    rolls = sum(
        sum(grid[ni, nj] == "@" for (ni, nj) in offsets(i, j, grid)) < 4
        for (i, j), val in grid.items()
        if val == "@"
    )
    print(rolls)


def part_2() -> None:
    raw_data = load_raw_data()
    grid = pass_data(raw_data)
    rolls = 0
    while True:
        flip = {}
        for (i, j), val in grid.items():
            if (
                val == "@"
                and sum(grid[ni, nj] == "@" for (ni, nj) in offsets(i, j, grid)) < 4
            ):
                flip[(i, j)] = True
            for i, j in flip.keys():
                grid[(i, j)] = "."
        rolls += len(flip)
        if not flip:
            break
    print(rolls)


if __name__ == "__main__":
    part_1()
    part_2()
