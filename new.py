
import argparse
import datetime as dt
import requests
from pathlib import Path

from default.cookie import SESSION_COOKIE

# Main

def fetch_input(day: int, advent_year: int) -> str:
    resp = requests.get(
        "https://adventofcode.com/{}/day/{}/input".format(advent_year, day),
        cookies={"session": SESSION_COOKIE},
        headers={"user-agent": "just a simple input fetcher (https://twitter.com/quackbarc)"}
    )

    if 400 <= resp.status_code < 500:
        print(f"\x1b[93mAoC raised a {resp.status_code}: {resp.text}\x1b[0m")
        print(f"-" * 50)
        resp.raise_for_status()

    resp.raise_for_status()
    return resp.text

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--day", "-d", required=True, help="The day to generate the script and fetch the input of.", type=int)
    parser.add_argument("--name", "-n", help="The name of the day. Must be a single word.")
    parser.add_argument("--year", "-y", help="The year of the advent event. Defaults to the current year.", type=int)
    args = parser.parse_args()

    day: int = args.day
    day_name = str(day).zfill(2)
    advent_year: int = args.year or dt.datetime.now().year

    if args.name:
        name = f"{day_name}_{args.name}"
    else:
        name = day_name

    template_file = Path("default/template.py")
    inputs_folder = Path("inputs")
    inputs_folder.mkdir(exist_ok=True)
    input_file = Path(inputs_folder, f"{day_name}.txt")
    py_file = Path(f"{name}.py")

    if py_file.exists():
        while True:
            yn = input(f"\"{py_file}\" already exists. continue anyways? (Y/N): ")
            if yn.lower().startswith("y"):
                break
            elif yn.lower().startswith("n"):
                return

    with open(template_file, "r", encoding="utf-8") as f:
        template = f.read()
    with open(py_file, "w", encoding="utf-8") as f:
        f.write(template.format(advent_year, name))
        print(f"written {py_file}.")

    with open(input_file, "w", encoding="utf-8") as f:
        input_text = fetch_input(day, advent_year)
        f.write(input_text)
        print(f"written {input_file}.")

if __name__ == '__main__':
    main()
