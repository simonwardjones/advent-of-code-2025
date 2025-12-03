import pathlib
from typing import Iterable

DATA_DIR = pathlib.Path(__file__).parent.parent.parent / "data"


def load_raw_data() -> str:
    data_file_name = "data_sample_1.txt"
    data_file_name = "data.txt"
    with open(DATA_DIR / "day_03" / data_file_name) as f:
        raw_data = f.read()
    return raw_data


class Battery:
    def __init__(self, joltage: int):
        self.joltage = joltage

    def __repr__(self) -> str:
        return f"Battery(joltage={self.joltage})"

    def __lt__(self, other: "Battery") -> bool:
        return self.joltage < other.joltage

    def __gt__(self, other: "Battery") -> bool:
        return self.joltage > other.joltage

    def __eq__(self, other: "Battery") -> bool:
        return self.joltage == other.joltage

    def __ne__(self, other: "Battery") -> bool:
        return self.joltage != other.joltage


class BatteryBank:
    def __init__(self, batteries=Iterable[Battery]):
        self.batteries = list(batteries)

    def __repr__(self) -> str:
        return f"BatteryBank(batteries={self.batteries})"

    def max_joltage(self, n_batteries: int = 2) -> int:
        start_index = max_joltage = 0
        for i in range(n_batteries):
            max_index = len(self.batteries) - n_batteries + 1 + i
            value = max(battery for battery in self.batteries[start_index:max_index])
            start_index += self.batteries[start_index:max_index].index(value) + 1
            max_joltage += 10 ** (n_batteries - i - 1) * value.joltage
        return max_joltage


def pass_data(raw_data: str) -> list[BatteryBank]:
    return [BatteryBank(Battery(int(val)) for val in row) for row in raw_data.split()]


def main() -> None:
    raw_data = load_raw_data()
    banks = pass_data(raw_data)
    print(sum(bank.max_joltage() for bank in banks))
    print(sum(bank.max_joltage(12) for bank in banks))


if __name__ == "__main__":
    main()
