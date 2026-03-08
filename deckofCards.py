#Simone Frazier CIS261 DECKofCARDS LAB
import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        ranks = ["Ace", "2", "3", "4", "5", "6", "7",
                 "8", "9", "10", "Jack", "Queen", "King"]
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

    def count(self):
        return len(self.deck)


print("Simone The Card Dealer\n")

deck = Deck()
deck.shuffle()

print("I have shuffled a deck of 52 cards.\n")

num = int(input("How many cards would you like?: "))

print("\nHere are your cards:")
for i in range(num):
    card = deck.deal()
    print(card)

print(f"\nThere are {deck.count()} cards left in the deck.\n")
print("Good luck!")

input("Press any key to continue . . .")