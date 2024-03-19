import random

suit = ["clubs", "diamonds", "hearts", "spades"]
number = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
player1Suit = random.choice(suit)
player1Number = random.choice(number)
player2Suit = random.choice(suit)
player2Number = random.choice(number)
print("player 1: ", player1Number, " of ", player1Suit)
print("player 2: ", player2Number, " of ", player2Suit)

if number.index(player1Number) > number.index(player2Number):
    print("player 1 wins.")
elif number.index(player1Number) < number.index(player2Number):
    print("player 2 wins.")
else:
    if suit.index(player1Suit) > suit.index(player2Suit):
        print("player 1 wins.")
    else:
        print("player 2 wins.")