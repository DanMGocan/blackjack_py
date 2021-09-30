import random

def create_players():
    number_of_players = 4
    # while number_of_players <= 0 or number_of_players > 6:
    #    number_of_players = int(input("How many players will play?"))

    list_of_players = []

    for player in range (0, number_of_players):
        list_of_players.append({
            "name": "Player #{}".format(player + 1),
            "cash": 100,
            "cards": []
            })
    list_of_players.append({"name": "House",
            "cash": 500,
            "cards": []
            })
    return list_of_players

def create_deck():
    deck = []
    suits = ["A", "B", "C", "D"]
    for element in suits:
        for number in range (2, 11):
            deck.append("{}{}".format(element, number))
    random.shuffle(deck)
    return deck

def distribute_cards(deck, players):
    for player in players:
        if player["name"] != "House":
            for card in range (0, 2):
                card_to_distribute = deck.pop(card)
                player["cards"].append(card_to_distribute)
    players[-1]["cards"] = deck
    return players

#Function that creates all the players and distributes the cards among them.
distribute_cards(create_deck(), create_players())

