# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 16:39:35 2020

@author: shrut
"""

import random

facevalues = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
suits = ('Spades', 'Hearts', 'Clubs', 'Diamonds')

playing = True

# CLASS DEFINTIONS:

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + ' of ' + self.suit
    

class Deck:
    
    def __init__(self):
        self.deck = []  # empty list is going to start
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                
    def __str__(self):
        deck_comp = ''  # empty string is going to start
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # object's print string to add on each card
        return 'The deck has:' + deck_comp
                
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card
    

class Hand:
    
    def __init__(self):
        self.cards = []  # starting with an empty list by doing similar as in the Deck class
        self.value = 0   # zero value is going to start
        self.aces = 0    # to keep track of aces , adding an attribute is important
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            

class shots:
    
    def __init__(self):
        self.total = 100
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet
        

# DEFINITIONS of FUNCTIONS:

def take_bet(shots):

    while True:
        try:
            shots.bet = int(input('How many shots would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if shots.bet > shots.total:
                print("Sorry, your bet can't exceed",shots.total)
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
    
def hit_or_stand(deck,hand):
    global playing
    
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        
        if x[0].lower() == 'h':
            hit(deck,hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break

    
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)
    
def player_busts(player,dealer,shots):
    print("Player busts!")
    shots.lose_bet()

def player_wins(player,dealer,shots):
    print("Player wins!")
    shots.win_bet()

def dealer_busts(player,dealer,shots):
    print("Dealer busts!")
    shots.win_bet()
    
def dealer_wins(player,dealer,shots):
    print("Dealer wins!")
    shots.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")
    
# GAMEPLAY!

while True:
    print('Welcome to the 21 game! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    # Player's shots has been set up
    player_shots = shots()  # remember the default value is 100
    
    # Prompt the Player for their bet:
    take_bet(player_shots)
    
    # Show the cards:
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)
        
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_shots)
            break
    
    # If Player hasn't busted, play Dealer's hand        
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
            
        # Show all cards
        show_all(player_hand,dealer_hand)
        
        # Test different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_shots)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_shots)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_shots)

        else:
            push(player_hand,dealer_hand)

    # Inform Player of their shots total    
    print("\nPlayer's winnings stand at",player_shots.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break 