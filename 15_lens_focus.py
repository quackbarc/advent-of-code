
"""
@quackbarc, https://adventofcode.com/2023/day/15.
Part 1 written on December 15th,
Part 2 written on the 17th.
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

    def holiday_hash(seq: str) -> int:
        val = 0

        for char in seq:
            val = ((ord(char) + val) * 17) % 256
        return val

    # Part 1
    # Testing holiday_hash

    accum_val = 0

    for sequence in data.split(","):
        accum_val += holiday_hash(sequence)

    print(accum_val)

    # Part 2
    # Lens shifting around the boxes

    boxes: dict[int, dict[str, int]] = {}
    r = iter(range(100))

    for lens_label, op, lens_focal_repl in re.findall(r"([a-z]+)([=-])(\d*)", data):
        box = holiday_hash(lens_label)

        # Using Python is really cheating here because dicts are already ordered by insertion
        boxes.setdefault(box, {})
        if op == "=":
            boxes[box][lens_label] = int(lens_focal_repl)
        elif op == "-":
            try:
                del boxes[box][lens_label]
            except KeyError:
                pass

    total_focus_power = 0

    for box_id, lenses in boxes.items():
        for ind, lens in enumerate(lenses.items()):
            lens_label, lens_focus = lens
            total_focus_power += (box_id + 1) * (ind + 1) * lens_focus

    print(total_focus_power)

if __name__ == "__main__":
    main()
