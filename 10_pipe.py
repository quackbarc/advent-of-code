
"""@quackbarc, https://adventofcode.com/2023/day/10"""

import itertools
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
    lines = data.split("\n")

    # i don't want pyright to give me any of them yellow lines
    line_pos = -1
    col_pos = -1

    for line_pos, line in enumerate(lines):
        match = re.search("S", line)

        if match is None:
            continue

        col_pos = match.start()
        break

    start_pos = (line_pos, col_pos)
    queue = [
        (start_pos, (0, 1), 0),
        (start_pos, (0, -1), 1),
        (start_pos, (1, 0), 2),
        (start_pos, (-1, 0), 3),
    ]

    pipe_check_index: dict[tuple[int, int], str] = {
        (0, 1): "-J7",
        (0, -1): "-LF",
        (1, 0): "|LJ",
        (-1, 0): "|F7",
    }

    pipe_follow_index: dict[str, list[tuple[int, int]]] = {}
    for relpos, pipes in pipe_check_index.items():
        followpos = (-relpos[0], -relpos[1])
        for pipe in pipes:
            pipe_follow_index.setdefault(pipe, [])
            pipe_follow_index[pipe].append(followpos)

    l = iter(range(100000))
    pipe_loops = [[], [], [], []]
    pipe_loop_map: dict[tuple[int, int], int] = {}

    while queue:
        current, diff, loop_no = queue.pop(0)
        scany, scanx = current[0] + diff[0], current[1] + diff[1]

        try:
            pipe = lines[scany][scanx]
            pipe_pos = (scany, scanx)
        except IndexError:
            continue

        # Check, then follow
        # Author's note: It took me a bit to realize that I'm supposed to follow a pipe,
        # not a general 4-direction flood fill. God damn it.

        # Check
        accepted_pipes = pipe_check_index[diff]
        if pipe in accepted_pipes:
            if pipe_pos in pipe_loop_map:
                if pipe_loop_map[pipe_pos] != loop_no:
                    # We've found two loops that connect each other.
                    connecting_loop_nos = (loop_no, pipe_loop_map[pipe_pos])
                    break
                else:
                    # We've just went backwards on the loop we're on.
                    continue

            # Follow
            for follow_diff in pipe_follow_index[pipe]:
                queue.append([pipe_pos, follow_diff, loop_no])

            pipe_loops[loop_no].append(pipe_pos)
            pipe_loop_map[pipe_pos] = loop_no

        # Debugging tidbit to prevent the while loop from going forever
        next(l)

    print([len(loop) for loop in pipe_loops])

    # -- Part 2 --

    a, b = connecting_loop_nos  # type: ignore
    full_loop: list[tuple[int, int]] = [start_pos, *pipe_loops[a], *reversed(pipe_loops[b])]
    full_loop_lookup = set(full_loop)
    assert len(full_loop_lookup) == len(full_loop)

    _top, *_, _bottom = sorted(full_loop, key=lambda pos: pos[0])
    _left, *_, _right = sorted(full_loop, key=lambda pos: pos[1])
    top_left = (_top[0], _left[1])
    bottom_right = (_bottom[0], _right[1])

    # Iterate through all the points, and raycast to one direction.
    # (In this implementation, it's to the east -- but any direction works)
    # - If it hits an even amount of boundaries, it's outside.
    # - If it hits an odd amount, it's inside.
    # https://en.wikipedia.org/wiki/Even%E2%80%93odd_rule

    # ^ The comment above is outdated; this implementation iterates AND raycasts
    # at the same time, but the general idea's still there.
    # Needed to do that cuz I also have to check whether a tile's part of the
    # main pipe loop or not.

    inside_count = 0

    for scany in range(top_left[0], bottom_right[0] + 1):
        even_odd = 0
        current_corner = None

        for scanx in range(top_left[1], bottom_right[1] + 1):
            if (scany, scanx) not in full_loop_lookup:
                inside = even_odd % 2 == 1
                if inside:
                    inside_count += 1

            else:
                tile = lines[scany][scanx]

                if tile == "|":
                    even_odd += 1
                elif tile in "LF":
                    current_corner = tile
                # Passing through an L7 or FJ is essentially the same as passing through a |.
                elif (current_corner == "L" and tile == "7") or (current_corner == "F" and tile == "J"):
                    even_odd += 1
                elif tile == "-":
                    pass

                if tile in "7J":
                    current_corner = None

    print(inside_count)

if __name__ == "__main__":
    main()
