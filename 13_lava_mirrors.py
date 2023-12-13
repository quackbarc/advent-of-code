
"""@quackbarc, https://adventofcode.com/2023/day/13"""

from collections import Counter

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

    cumul = 0
    cumul_part_2 = 0

    for chunk_no, chunk in enumerate(data.split("\n\n")):
        chunk_lines = chunk.split("\n")
        line_count = len(chunk_lines)
        line_length = len(chunk_lines[0])

        possible_vertical_symlines: Counter[int] = Counter()
        possible_horizontal_symlines: Counter[int] = Counter()

        for line in chunk_lines:
            for ind in range(len(line) - 1):
                # Vertical symmetry test for now.
                # Going from 0 to len(line) - 1; last index shouldn't count.

                sl1 = line[0 : ind+1]
                sl2 = line[ind+1 : ind+1+len(sl1)]

                if sl1[::-1].startswith(sl2):
                    possible_vertical_symlines.setdefault(ind, 0)
                    possible_vertical_symlines[ind] += 1

        for col in range(line_length):
            # Then the horizontal symmetry test.

            column = "".join(line[col] for line in chunk_lines)

            for ind in range(len(column) - 1):
                sl1 = column[0 : ind+1]
                sl2 = column[ind+1 : ind+1+len(sl1)]

                if sl1[::-1].startswith(sl2):
                    possible_horizontal_symlines.setdefault(ind, 0)
                    possible_horizontal_symlines[ind] += 1

        # Part 1

        vertical_symline = next((k for k, v in possible_vertical_symlines.items() if v == line_count), None)
        horizontal_symline = next((k for k, v in possible_horizontal_symlines.items() if v == line_length), None)

        # Add the lengths of that first half of the reflection.
        # Lengths, not the index, so we're adding 1.
        if vertical_symline is not None:
            cumul += vertical_symline + 1
        elif horizontal_symline is not None:
            cumul += 100 * (horizontal_symline + 1)

        # Part 2

        # If the mirror smudges were fixed, whatever new vertical/horizontal symlines we have now
        # were just 1 less in our counter last time.
        fvs = fixed_vertical_symline = next((k for k, v in possible_vertical_symlines.items() if v == line_count - 1), None)
        fhs = fixed_horizontal_symline = next((k for k, v in possible_horizontal_symlines.items() if v == line_length - 1), None)

        # Same solution case with part 1.
        if fvs is not None:
            cumul_part_2 += fvs + 1
        elif fhs is not None:
            cumul_part_2 += 100 * (fhs + 1)

    print(cumul)
    print(cumul_part_2)


if __name__ == "__main__":
    main()
