
"""@quackbarc, https://adventofcode.com/2023/day/02"""

# Input fetchers

import operator
import re

def get_input() -> str:
    from pathlib import Path
    filename_number = Path(__file__).name.partition("_")[0]
    filepath_txt = Path("inputs", filename_number).with_suffix(".txt")

    with open(filepath_txt, "r", encoding="utf-8") as f:
        return f.read().strip()

# Main

def main():
    data = get_input()

    # Part 1
    # cum_game_id = 0

    # Part 2
    cum_cube_power = 0

    for line in data.split("\n"):
        match = re.findall(r"Game (\d+): (.+)", line)
        game_id, cube_roll_set = match[0]

        suspected_cube_count = {
            "red": 0,
            "blue": 0,
            "green": 0,
        }

        for cube_rolls in re.split(r";\s?", cube_roll_set):
            for match in re.findall(r"(\d+) (red|blue|green)", cube_rolls):
                cube_count, cube_type = match
                suspected_cube_count[cube_type] = max(int(cube_count), suspected_cube_count[cube_type])

        # Part 1
        # s = suspected_cube_count
        # if s["red"] <= 12 and s["green"] <= 13 and s["blue"] <= 14:
        #     cum_game_id += int(game_id)
        #     print(game_id, suspected_cube_count)

        # Part 2
        cube_power = 1
        for cube_count in suspected_cube_count.values():
            cube_power *= cube_count
        cum_cube_power += cube_power

    # Part 1
    # print(cum_game_id)

    # Part 2
    print(cum_cube_power)

if __name__ == "__main__":
    main()
