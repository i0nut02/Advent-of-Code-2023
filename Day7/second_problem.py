from collections import Counter

CARD_ORDER = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

def format_hand(hand):
    cards, bid = tuple(hand.split(" ")[:2])
    count = sorted(Counter(cards).items(), key=lambda x : -x[1])

    J_founded = max([acc for card, acc in count if card == "J"] + [0])
    if J_founded != 0: count.remove(("J", J_founded))

    if len(count) <= 1: # Five of a kind
        return cards, 5, bid
    
    elif len(count) == 2:
        # there isn't any J
        if J_founded == 0:
            # 3 & 2 or 4 & 1
            if count[0][1] == 4:
                return cards, 4, bid
            else: return cards, 3, bid
        else:
            # j from 1 to 3, if j == 1 then 2 & 2 or 3 & 1, if j == 2 then 2 & 1 if j == 3 then 1 & 1
            if J_founded >= 2:
                return cards, 4, bid
            if count[0][1] == 3: return cards, 4, bid
            else: return cards, 3, bid
    elif len(count) == 3:
        if J_founded == 0:
            # 3 & 1 & 1 or 2 & 2 & 1 or
            if count[0][1] == 3: return cards, 2, bid
            return cards, 1, bid
        else:
            # j from 1 to 2, if j == 1 then 2 & 1 & 1, if j == 2 then 1 & 1 & 1
            return cards, 2, bid
        
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