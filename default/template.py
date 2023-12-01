
"""@quackbarc, https://adventofcode.com/{}/day/{}"""

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

if __name__ == "__main__":
    main()
