
"""@quackbarc, https://adventofcode.com/2023/day/07"""

import re
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

    hands_and_bids: list[tuple[str, int]] = []

    for line in data.split("\n"):
        hand, bid = re.findall(r"(.....) (\d+)", line)[0]
        hands_and_bids.append((hand, bid))

    def card_sort(hand_and_bid: tuple[str, int]) -> int:
        hand, _ = hand_and_bid
        n = 0

        # Part 1
        # index = "23456789TJQKA"

        # Part 2
        index = "J23456789TQKA"

        for i, c in enumerate(hand[::-1]):
            n += (len(index)**i) * index.index(c)

        return n

    def hand_sort(hand_and_bid: tuple[str, int]) -> int:
        hand, _ = hand_and_bid

        # Five of a kind, where all five cards have the same label: AAAAA
        # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
        # Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
        # Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
        # Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
        # One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
        # High card, where all cards' labels are distinct: 23456

        counter = Counter(hand)

        if any(v == 5 for v in counter.values()):
            return 7

        if any(v == 4 for v in counter.values()):
            return 6

        if set(counter.values()) == {3, 2}:
            return 5

        if any(v == 3 for v in counter.values()):
            return 4

        if list(counter.values()).count(2) == 2:
            return 3

        if any(v == 2 for v in counter.values()):
            return 2

        if all(v == 1 for v in counter.values()):
            return 1

        assert False, counter

    def society_sort(hand_and_bid: tuple[str, int]) -> int:
        hand, bid = hand_and_bid

        no_jokers = hand.replace("J", "")
        counter = Counter(no_jokers)

        # Jokers are never able to make high cards, so we could just iterate through whatever we have just fine.
        # Jokers are also never able to make full houses.
        # Ideally, if we bump up the highest number in here, we'd definitely get a higher rank than the original.

        if not counter:
            return hand_sort(("KKKKK", bid))

        most_common, = counter.most_common(1)
        most_common_card, *_ = most_common
        new_hand = hand.replace("J", most_common_card)
        return hand_sort((new_hand, bid))

    # Part 1
    # hands_and_bids.sort(key=card_sort)
    # hands_and_bids.sort(key=hand_sort)

    # Part 2
    hands_and_bids.sort(key=card_sort)
    hands_and_bids.sort(key=society_sort)

    total_winnings = 0

    for rank, (hand, bid) in enumerate(hands_and_bids, start=1):
        total_winnings += rank * int(bid)

    print(total_winnings)


if __name__ == "__main__":
    main()
