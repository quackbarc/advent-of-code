
"""@quackbarc, https://adventofcode.com/2023/day/01"""

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

    calivalues = 0

    def to_number(char: str) -> str:
        if char in string.digits:
            return char

        word_digit_map = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9"
        }
        return word_digit_map[char]

    for line in data.split("\n"):
        start_matches = re.findall(r"\d|one|two|three|four|five|six|seven|eight|nine", line)
        end_matches = re.findall(r".*(\d|one|two|three|four|five|six|seven|eight|nine)", line)
        calivalue = int(to_number(start_matches[0]) + to_number(end_matches[0]))
        calivalues += calivalue
        print(calivalue, line)

    print()
    print(calivalues)

if __name__ == "__main__":
    main()
