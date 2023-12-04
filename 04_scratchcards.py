
"""@quackbarc, https://adventofcode.com/2023/day/04"""

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

    # Part 1
    # accum_points = 0

    # Part 2
    card_copies: dict[int, int] = {}

    for line in data.split("\n"):
        match = re.findall(r"Card \s*(\d+): (.+) \| (.+)", line)
        card_id, winning_numbers, my_numbers = match[0]

        winning_numbers = set(re.findall(r"\d+", winning_numbers))
        my_numbers = set(re.findall(r"\d+", my_numbers))
        common_numbers = winning_numbers & my_numbers

        # Part 1
        # if not common_numbers:
        #     points = 0
        # else:
        #     points = 2 ** (len(common_numbers) - 1)
        #     accum_points += points

        # Part 2
        card_id = int(card_id)

        card_copies.setdefault(card_id, 1)
        copies = card_copies[card_id]

        for new_card in range(card_id + 1, card_id + len(common_numbers) + 1):
            card_copies.setdefault(new_card, 1)
            card_copies[new_card] += copies

    # Part 1
    # print(accum_points)

    # Part 2
    print(sum(card_copies.values()))

if __name__ == "__main__":
    main()
