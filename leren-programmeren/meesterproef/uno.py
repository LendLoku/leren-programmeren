import random

# Function to initialize a deck of UNO cards
def initialize_deck():
    colors = ["Red", "Green", "Blue", "Yellow"]
    values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Skip", "Reverse", "Draw Two"]
    wilds = ["Wild", "Wild Draw Four"]

    deck = []

    # Add colored cards
    for color in colors:
        for value in values:
            card = color + " " + value
            deck.append(card)
            if value != "0":
                deck.append(card)