import pathlib

DATA_DIR = pathlib.Path(__file__).parent.parent.parent / "data"


class Dial:
    def __init__(self, position: int = 50, n_positions: int = 100):
        self.position = position
        self.n_positions = 100
        self.hits = 0

    def right(self, distance: int = 1):
        self.position += distance
        self.position %= 100

    def left(self, distance: int = 1):
        self.position -= distance
        self.position %= 100

    def execute_command(self, command: str):
        if command[0] == "L":
            self.right(int(command[1:]))
        else:
            self.left(int(command[1:]))
        if self.position == 0:
            self.hits += 1

    def execute_command_2(self, command: str):
        distance = int(command[1:])
        if command[0] == "L":
            self.right(distance)
        else:
            self.left(distance)
        loops, remainder = divmod(distance, self.n_positions)
        self.hits += loops
        if (command[0] == "L" and remainder >= self.position and self.position > 0) or (
            command[0] == "R" and remainder >= self.n_positions - self.position
        ):
            self.hits += 1


def load_raw_data() -> str:
    data_file_name = "data_sample_1.txt"
    data_file_name = "data.txt"
    with open(DATA_DIR / "day_01" / data_file_name) as f:
        raw_data = f.read()
    # print(raw_data)
    return raw_data


def main():
    raw_data = load_raw_data()
    dial = Dial()
    for command in raw_data.split():
        dial.execute_command(command)
    print(f"dial.hits = {dial.hits}")

    dial2 = Dial()
    for command in raw_data.split():
        dial2.execute_command_2(command)
    print(f"dial2.hits = {dial2.hits}")


if __name__ == "__main__":
    main()
