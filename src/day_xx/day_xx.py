import pathlib

DATA_DIR = pathlib.Path(__file__).parent.parent.parent / "data"


def load_raw_data() -> str:
    data_file_name = "data.txt"
    data_file_name = "data_sample_1.txt"
    with open(DATA_DIR / "day_01" / data_file_name) as f:
        raw_data = f.read()
    print(raw_data)
    return raw_data


def main() -> None:
    raw_data = load_raw_data()


if __name__ == "__main__":
    main()
