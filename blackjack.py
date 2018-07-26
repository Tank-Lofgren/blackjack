#Blackjack

import random

#class to handle the play deck
class play_deck:
    def __init__():
        #Add all card to a dictionary
        self.deck = {
        "2S":2, "2C":2, "2H":2, "2D":2,
        "3S":3, "3C":3, "3H":3, "3D":3,
        "4S":4, "4C":4, "4H":4, "4D":4,
        "5S":5, "5C":5, "5H":5, "5D":5,
        "6S":6, "6C":6, "6H":6, "6D":6,
        "7S":7, "7C":7, "7H":7, "7D":7,
        "8S":8, "8C":8, "8H":8, "8D":8,
        "9S":9, "9C":9, "9H":9, "9D":9,
        "10S":10, "10C":10, "10H":10, "10D":10,
        "JS":10, "JC":10, "JH":10, "JD":10,
        "QS":10, "QC":10, "QH":10, "QD":10,
        "KS":10, "KC":10, "KH":10, "KD":10,
        "AS":11, "AC":11, "AH":11, "AD":11,
        }
    #Function to remove a card from the deck and return it
    def draw_card():
        card = random.choice(self.deck.keys())
        self.deck.pop(card)
        return card


#def draw_card()

def game():
    player_money = 1000
    playing = True
    player_hand = []
    dealer_hand = []
    while playing == True:
        deck = play_deck()
        bet = raw_input("How much would you like to bet? (X to exit): ")
        if str(bet).upper() == "X":
            playing = False
            print "Thanks for playing!"
            continue
        bet = int(bet)
        print "Your bet is ", bet, "."



print "Welcome to blackjack!"
game()
