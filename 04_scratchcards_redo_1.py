
"""@quackbarc, https://adventofcode.com/2023/day/04. Second solution.

I was a bit tired when I wrote that first solution, so I thought I'd do a redo.
Turns out I came up with the exact same thing, but with prettier writing.
"""

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

    # Part 1
    # total_points = 0

    # Part 2
    card_count: dict[int, int] = {}

    for line in data.split("\n"):
        pattern = re.compile(r"Card\s+(\d+): (.+) \| (.+)")
        match, = pattern.findall(line)

        card_id = int(match[0])
        winning_nums = set(re.findall(r"\d+", match[1]))
        my_nums = set(re.findall(r"\d+", match[2]))

        # Part 1
        # common_nums = winning_nums & my_nums
        # points = 2 ** (len(common_nums) - 1) if len(common_nums) > 0 else 0
        # total_points += points

        # Part 2
        common_nums = winning_nums & my_nums
        card_copies = card_count.setdefault(card_id, 1)

        for n in range(0, len(common_nums)):
            new_card_id = card_id + n + 1
            card_count.setdefault(new_card_id, 1)
            card_count[new_card_id] += card_copies

    # Part 1
    # print(total_points)

    # Part 2
    print(sum(card_count.values()))

if __name__ == "__main__":
    main()
