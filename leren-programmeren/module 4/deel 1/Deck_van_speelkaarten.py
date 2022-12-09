import random
deck = []
kleuren = ("harten", "klaveren", "schoppen", "ruiten")
nummers_en_personages = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "boer", "vrouw", "heer", "aas")

for inhoudsopgave in range(0, 4):
    for i in range(0, 13):
        deck.append(kleuren[inhoudsopgave] + " " + nummers_en_personages[i])

deck.append("joker")
deck.append("joker")
random.shuffle(deck)

for inhoudsopgave in range(1, 8):
    print(f"kaart {inhoudsopgave}: ", deck[inhoudsopgave])
