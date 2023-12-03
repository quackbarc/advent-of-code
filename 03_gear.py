
"""@quackbarc, https://adventofcode.com/2023/day/03"""

import itertools
import re
import string

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
    data_lines = data.split("\n")

    # Part 1
    # sum_num = 0

    # Part 2
    gear_index: dict[tuple[int, int], list[int]] = {}
    gear_ratio_sum = 0

    for line_no, line in enumerate(data_lines):
        for num_match in re.finditer(r"\d+", line):
            num = int(num_match.group(0))
            ms, me = num_match.span()

            for y_delt in range(-1, 2):
                try:
                    check_substr = data_lines[max(line_no + y_delt, 0)][max(ms - 1, 0):me + 1]
                except IndexError:
                    continue

                # Part 1
                # if re.search(r"[^0-9.]", check_substr):
                #     print("----------", num, check_substr)
                #     sum_num += num
                #     break

                # Part 2
                if (star_match := re.search(r"\*", check_substr)):
                    star_line_no = max(line_no + y_delt, 0)
                    star_char_no = max(ms - 1, 0) + star_match.start()
                    star_key = (star_line_no, star_char_no)

                    gear_index.setdefault(star_key, [])
                    gear_index[star_key].append(num)

                    print("----------", num, check_substr)
                    break

    # Part 1
    # print(sum_num)

    # Part 2
    for nums in gear_index.values():
        if len(nums) == 2:
            gear_ratio = nums[0] * nums[1]
            gear_ratio_sum += gear_ratio

    print(gear_ratio_sum)

if __name__ == "__main__":
    main()
