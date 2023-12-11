
"""@quackbarc, https://adventofcode.com/2023/day/11"""

import itertools
import re

# Input fetchers

def get_input() -> str:
    from pathlib import Path
    filename_number = Path(__file__).name.partition("_")[0]
    filepath_txt = Path("inputs", filename_number).with_suffix(".txt")

    with open(filepath_txt, "r", encoding="utf-8") as f:
        return f.read().strip()

# Main

def main():
    data = get_input()

    # Mostly for debugging with the test input.
    line_size = 140

    galaxies: list[tuple[int, int]] = []

    for line_pos, line in enumerate(data.split("\n")):
        for match in re.finditer(r"#", line):
            galaxy = (line_pos, match.start())
            galaxies.append(galaxy)

        line_size = len(line)

    # Find empty rows and cols via galaxy list
    empty_rows = set(range(line_size)) - set(g[0] for g in galaxies)
    empty_cols = set(range(line_size)) - set(g[1] for g in galaxies)

    # Calculate Manhattan distance between any two galaxies
    # Consider the empty rows and cols!!

    distances = 0

    for galaxy1, galaxy2 in itertools.combinations(galaxies, 2):
        y1, x1, y2, x2 = *galaxy1, *galaxy2

        # Part 1
        # expand_by = 1
        # Part 2
        # According to the instructions, every empty row/col doesn't *expand* by 1_000_000,
        # but *becomes* 1_000_000 rows/cols.
        expand_by = 999_999
        y1 += sum(expand_by for c in empty_rows if y1 > c)
        y2 += sum(expand_by for c in empty_rows if y2 > c)
        x1 += sum(expand_by for c in empty_cols if x1 > c)
        x2 += sum(expand_by for c in empty_cols if x2 > c)

        manhattan_distance = abs(y2 - y1) + abs(x2 - x1)
        distances += manhattan_distance

    print(distances)


if __name__ == "__main__":
    main()
