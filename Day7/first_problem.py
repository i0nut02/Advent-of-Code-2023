from collections import Counter

CARD_ORDER = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

def format_hand(hand):
    cards, bid = tuple(hand.split(" ")[:2])
    count = sorted(Counter(cards).items(), key=lambda x : -x[1])

    if len(count) == 1: # Five of a kind
        return cards, 5, bid
    elif len(count) == 2 and count[0][1] == 4: # Four of a kind
        return cards, 4, bid
    elif len(count) == 2 and count[0][1] == 3: # Full house
        return cards, 3, bid
    elif len(count) == 3 and count[0][1] == 3: # Three of a kind
        return cards, 2, bid
    elif len(count) == 3 and count[0][1] == 2: # Two pair
        return cards, 1, bid
    elif len(count) == 4:
        return cards, 0, bid
    else:
        return cards, -1, bid

def get_amount(file):
    hands = []
    with open(file, mode="r") as f:
        for hand in f.read().split("\n"):
            hands.append(format_hand(hand))

    hands.sort(key= lambda x : (x[1], [- CARD_ORDER.index(y) for y in x[0]]))

    res = 0
    for i, hand in enumerate(hands):
        res += (i+1) * int(hand[-1])
    return res