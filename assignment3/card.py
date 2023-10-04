import random

class Card:
    '''A playing card with a suit and a number'''
    
    def __init__(self, suit, number):
        '''__init__ method for Card class, takes suit and number as arguments, sets them as attributes, and prints a message to the console'''
        self._suit = suit
        self._number = number

    def __repr__(self):
        '''__repr__ method for Card class, returns a string representation of the card, e.g. "Ace of Spades"'''
        return self._number + " of " + self._suit

    @property
    def suit(self):
        '''Getter and setter method for suit attribute, returns the suit of the card'''
        return self._suit

    @suit.setter
    def suit(self, suit):
        if suit in ["hearts", "clubs", "diamonds", "spades"]:
            self._suit = suit
        else:
            print("That's not a suit!")

    @property
    def number(self):
        '''Getter and setter method for number attribute, returns the number of the card,  e.g. "Ace"'''
        return self._number

    @number.setter
    def number(self, number):
        valid = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
        if number in valid:
            self._number = number
        else:
            print("That's not a valid number")


class Deck:

    '''
    A deck of playing cards, 
    with a list of cards, and methods to 
    populate, shuffle, and deal cards, 
    and a __repr__ method to return a string 
    representation of the deck, e.g. "Deck of 52 cards"
    '''
    
    def __init__(self):
        '''__init__ method for Deck class, creates an empty list of cards, and populates it with 52 cards'''
        self._cards = []
        self.populate()

    def populate(self):
        '''Populates the deck with 52 cards, one of each suit and number, e.g. Ace of Spades'''
        suits = ["hearts", "clubs", "diamonds", "spades"]
        numbers = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
        self._cards = [ Card(s, n) for s in suits for n in numbers ]

    def shuffle(self):
        '''
        Shuffles the deck of cards, using the random module, 
        and the shuffle method, which shuffles the list in place, 
        rather than returning a new list, and returns the shuffled list, 
        which is the deck of cards, e.g. [Ace of Spades, 2 of Spades, 3 of Spades, ...], 
        but in a random order, e.g. [3 of Clubs, 7 of Diamonds, 2 of Hearts, ...], etc.
        '''
        random.shuffle(self._cards)

    def deal(self, no_of_cards):
        '''deals a number of cards from the deck, and returns them as a list, e.g. [Ace of Spades, 2 of Spades, 3 of Spades, ...]'''
        dealt_cards = []
        for i in range(no_of_cards):
            dealt_card = self._cards.pop(0)
            dealt_cards.append(dealt_card)
        return dealt_cards

    def __repr__(self):
        '''__repr__ method for Deck class, returns a string representation of the deck, e.g. "Deck of 52 cards"'''
        cards_in_deck = len(self._cards)
        return "Deck of " + str(cards_in_deck) + " cards"
 
    
deck = Deck()
'''deck represents a deck of cards, e.g. [Ace of Spades, 2 of Spades, 3 of Spades, ...]'''