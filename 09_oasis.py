
"""@quackbarc, https://adventofcode.com/2023/day/09"""

# Input fetchers

import functools
import itertools
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

    next_number_sum = 0

    for line in data.split("\n"):
        numbers = [int(x) for x in re.findall(r"-?\d+", line)]
        number_diffs = numbers.copy()

        # Part 1
        # last_numbers = [numbers[-1]]
        # Part 2
        first_numbers = [numbers[0]]

        for _ in itertools.count(1):
            for ind, this in enumerate(number_diffs):
                try:
                    next_ = number_diffs[ind+1]
                except IndexError:
                    del number_diffs[ind]
                    break
                else:
                    number_diffs[ind] = next_ - this

            # Part 1
            # last_numbers.append(number_diffs[-1])
            # Part 2
            first_numbers.append(number_diffs[0])

            if len(set(number_diffs)) == 1:
                break

        # Part 1
        # next_number = functools.reduce(lambda x, y: x + y, reversed(last_numbers))
        # next_number_sum += next_number
        # Part 2
        next_number = functools.reduce(lambda x, y: y - x, reversed(first_numbers))
        next_number_sum += next_number

    print(next_number_sum)


if __name__ == "__main__":
    main()
