
"""
@quackbarc, https://adventofcode.com/2023/day/08.
A draft was written on December 8th, so a part 1 answer was submitted on the same day.
Re-written on December 10th.
"""

import itertools
import math
import re

# Type definitions

Nodes = dict[str, tuple[str, str]]

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

    directions = re.findall(r"[RL]+", data)[0]
    nodes: Nodes = {this: (left, right) for this, left, right in re.findall(r"(...) = \((...), (...)\)", data)}

    # Part 1
    # Good ol' brute forcing this thing for now

    current_node = "AAA"

    for direction, step in zip(itertools.cycle(directions), itertools.count(1)):
        lrnode_index = 1 if direction == "R" else 0
        next_node = nodes[current_node][lrnode_index]
    
        if next_node == "ZZZ":
            print(step)
            break
    
        current_node = next_node

    # Part 2
    # On that December 8 draft, I mentioned something about finding LCMs for this.
    # I've had doubts about doing that for a second, because I thought there'd be
    # more than one Z-ending stop per A-starting node to consider.
    #
    # To quote that draft:
    # " - LCMs wouldn't really work; there's more steps past ZZZ"
    #
    # But after seeing Day 8 discussions on other Discords mentioning it, I
    # might as well give it another try.

    current_nodes = [node for node in nodes.keys() if node.endswith("A")]
    end_node_multiples = []

    for current_node in current_nodes:
        for direction, step in zip(itertools.cycle(directions), itertools.count(1)):
            lrnode_index = 1 if direction == "R" else 0
            next_node = nodes[current_node][lrnode_index]
        
            if next_node.endswith("Z"):
                end_node_multiples.append(step)
                break
        
            current_node = next_node

    # It seems that the step count between each Z is constant.
    # What a meticulously simplified puzzle...

    lcm = math.lcm(*end_node_multiples)
    print(lcm)


if __name__ == "__main__":
    main()
