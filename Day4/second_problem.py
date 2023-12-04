from collections import defaultdict

def get_card_score(card, mem_cards):
    card_id = int(card.split(":")[0].split(" ")[-1])
    mem_cards[card_id] += 1

    card = card.split(":")[1].strip(" ").strip("\n")

    winning_nums = set(card.split("|")[0].strip(" ").split(" "))
    personal_cards = set(card.split("|")[1].strip(" ").split(" "))

    if "" in winning_nums:
        winning_nums.remove("")

    count = 0

    for pers_card in personal_cards:
        if pers_card in winning_nums:
            count += 1
            mem_cards[card_id + count] += mem_cards[card_id]

    return

def get_cards_score(file):
    mem_cards = defaultdict(int)

    with open(file, mode="r") as f:
        for line in f.readlines():
            get_card_score(line, mem_cards)
    return sum(mem_cards.values())