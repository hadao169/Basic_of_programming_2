import random

# Define the suits, values, and colors
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
colors = {"Hearts": "Red", "Diamonds": "Red", "Clubs": "Black", "Spades": "Black"}

# Initialize the deck of cards as a list
deck_of_cards = []

# Populate the deck using a nested loop
for suit in suits:
    for value in values:
        card = {
            "suit": suit,
            "value": value,
            "colour": colors[suit]
        }
        deck_of_cards.append(card)

# Select a random card from the deck
random_card = random.choice(deck_of_cards)

# Print the selected card's data


print(len(deck_of_cards))