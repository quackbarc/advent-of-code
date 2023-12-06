
"""@quackbarc, https://adventofcode.com/2023/day/06"""

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

    def get_record_beat_count(time: int, record_distance: int) -> int:
        record_beat = 0

        for charge_time in range(time):
            release_distance = (time - charge_time) * charge_time
    
            if record_distance < release_distance:
                record_beat += 1

            # Large number progress check
            # Learned that lesson from yesterday.
            if record_beat % 10000000 == 0:
                print(f"{record_beat // 10000}:", time, release_distance)

        return record_beat

    # Part 1, trial-and-error. If that makes thins worse in Part 2 I might actually just lose it.

    times = [int(x) for x in re.findall(r"\d+", re.findall(r"Time: (.+)", data)[0])]
    distances = [int(x) for x in re.findall(r"\d+", re.findall(r"Distance: (.+)", data)[0])]
    
    record_beat_product = 1
    for time, record_distance in zip(times, distances):
        record_beat_product *= get_record_beat_count(time, record_distance)
    print(record_beat_product)

    # Part 2. Welp.

    time = re.findall(r"\d+", re.findall(r"Time: (.+)", data)[0])
    time = int("".join(time))
    record_distance = re.findall(r"\d+", re.findall(r"Distance: (.+)", data)[0])
    record_distance = int("".join(record_distance))

    record_beat = get_record_beat_count(time, record_distance)
    print(record_beat)

    # That... actually wasn't so bad? Interesting


if __name__ == "__main__":
    main()
