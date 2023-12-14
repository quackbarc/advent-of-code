
"""@quackbarc, https://adventofcode.com/2023/day/14"""

# Input fetchers

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

    # Part 2: Input and spin cycle process analysis
    #
    # # Reduce the amount of O's.
    # data = data[::-1].replace("O", ".", data.count("O") - 19)[::-1]
    #
    # # Replace all the O's with that are easy to spot.
    # data = data.replace("O", "$")
    # for asc in range(65, 65 + data.count("$")):
    #     data = data.replace("$", chr(asc), 1)

    grid = data.split("\n")

    def normal_rotate(grid: list[str], direction: str):
        line_length = len(grid[0])

        # For different directions other than west, start mirroring the grid.
        if direction in ("north", "south"):
            grid = ["".join(line[col] for line in grid) for col in range(line_length)]
        if direction in ("south", "east"):
            grid = [line[::-1] for line in grid]

        rolled_grid: list[str] = []

        for raw_line in grid:
            line = list(raw_line)
            roll_stop = 0

            for ind, char in enumerate(line):
                # Part 1
                # is_rolling_stone = char == "O"
                # Part 2
                is_rolling_stone = ord(char) >= 65  # ascii A onwards

                if char == "#":
                    roll_stop = ind + 1
                if is_rolling_stone and roll_stop == ind:
                    roll_stop = ind + 1
                if is_rolling_stone and roll_stop < ind:
                    line[ind] = "."
                    line[roll_stop] = char
                    roll_stop += 1

                    try:
                        while line[roll_stop] == "#":
                            roll_stop += 1
                    except IndexError:
                        pass

            rolled_line = "".join(line)
            rolled_grid.append(rolled_line)

            assert len(rolled_line) == len(raw_line)
            assert re.match(r"\.O", rolled_line) is None

        # Mirror the grid again to go back to what we originally had.
        if direction in ("south", "east"):
            rolled_grid = [line[::-1] for line in rolled_grid]
        if direction in ("north", "south"):
            rolled_grid = ["".join(line[col] for line in rolled_grid) for col in range(line_length)]

        return rolled_grid

    # Part 1

    cumul = 0
    rotated_grid = normal_rotate(grid, "north")

    for ind, line in enumerate(reversed(rotated_grid), start=1):
        cumul += line.count("O") * ind

    print(cumul)

    # Part 2
    # Run the spin cycle for long enough, and you'd eventually notice that the
    # same patterns would repeat over and over again.
    # Find those repeating patterns, memoize them,
    # and see where iteration 1,000,000,000 would land in that infinite cycle.
    #
    # Solving this one took a heeeefty bit of very careful analysis.

    new_grid = grid
    seen_grids: dict[str, int] = {}
    # Empty list just so pyright doesn't complain about "None" being non-iterable later on
    seen_grid_minmax: list[int] = []

    for ind in range(1, 1001):
        for direction in ("north", "west", "south", "east"):
            new_grid = normal_rotate(new_grid, direction)

        new_grid_str = "\n".join(new_grid)
        seen = new_grid_str in seen_grids
        seen_grids.setdefault(new_grid_str, ind)
        seen_grid_ind = seen_grids[new_grid_str]

        if seen and not seen_grid_minmax:
            seen_grid_minmax = [seen_grid_ind, ind - 1]
            # Any iteration after this would be a pattern we've already went through.
            break

    print()
    print(f"SPIN CYCLE CYCLE")
    print(seen_grid_minmax)

    iteration = 1_000_000_000

    sg_min, sg_max = seen_grid_minmax
    sg_iteration = sg_min + ((iteration - sg_min) % (sg_max - sg_min + 1))
    cached_grid = next(grid.split("\n") for grid, ind in seen_grids.items() if ind == sg_iteration)

    # Wait... I didn't have to do this?
    # Hmm... must've just misread the question then.
    # When I read "north support beams", I naturally assumed the load when the grid is tilted north.
    # rotated_grid = normal_rotate(cached_grid, "north")

    cumul = 0

    for ind, line in enumerate(reversed(cached_grid), start=1):
        cumul += line.count("O") * ind

    print(cumul)


if __name__ == "__main__":
    main()
