import pathlib

DATA_DIR = pathlib.Path(__file__).parent.parent.parent / "data"


def load_raw_data() -> str:
    data_file_name = "data_sample_1.txt"
    data_file_name = "data.txt"
    with open(DATA_DIR / "day_02" / data_file_name) as f:
        raw_data = f.read()
    return raw_data


def pass_data(raw_data: str) -> list[tuple[int, int]]:
    return [tuple(map(int, pair.split("-"))) for pair in raw_data.split(",")]


def find_split_palindromes(pass_data: list[tuple[int, int]]) -> int:
    count = 0
    for start, end in pass_data:
        for value in range(start, end + 1):
            if len(str(value)) % 2 != 0:
                continue
            if check_value(value):
                count += value
    return count


def check_value(value: int) -> bool:
    first_half = str(value)[: len(str(value)) // 2]
    second_half = str(value)[len(str(value)) // 2 :]
    return first_half == second_half


def find_multi_split_palindromes(pass_data: list[tuple[int, int]]) -> int:
    found = set()
    for start, end in pass_data:
        for value in range(start, end + 1):
            for chunk_size in range(1, len(str(value)) // 2 + 1):
                if len(str(value)) % chunk_size != 0:
                    continue
                if all(
                    str(value)[j * chunk_size : (j + 1) * chunk_size]
                    == str(value)[(j + 1) * chunk_size : (j + 2) * chunk_size]
                    for j in range(0, len(str(value)) // chunk_size - 1)
                ):
                    found.add(value)
    return sum(found)


def main() -> None:
    raw_data = load_raw_data()
    data = pass_data(raw_data)
    print(find_split_palindromes(data))
    print(find_multi_split_palindromes(data))



if __name__ == "__main__":
    main()
