def get_card_score(card):
    card = card.split(":")[1].strip(" ").strip("\n")

    winning_nums = set(card.split("|")[0].split(" "))
    personal_cards = set(card.split("|")[1].split(" "))
    winning_nums.remove("")

    res = 2 ** (len(personal_cards) - len(personal_cards - winning_nums) -1)

    return 0 if res < 1 else res

def get_cards_score(file):
    res = 0

    with open(file, mode="r") as f:
        for line in f.readlines():
            res += get_card_score(line)
    return res