""" Class: A blueprint that defines attributes and methods for objects.

Instance: A concrete object created from a class.

Encapsulation: Bundling data and methods together and restricting direct access to them.

Abstraction: Hiding implementation details and showing only essential features.

Inheritance: A mechanism where a class derives properties and methods from another class.

Multiple inheritance: A class inheriting from more than one parent class.

Polymorphism: The ability of different objects to respond to the same method in different ways.

Method Resolution Order (MRO): The order in which a language (e.g., Python) looks for methods in a class hierarchy. """



class Card:
    possibleSuit=["Hearts", "Diamonds", "Clubs", "Spades"]
    possibleValue=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    def __init__(self, suit, value ):
        if suit not in Card.possible_suits or value not in Card.possible_values:
            raise ValueError("Invalid card")
        self.suit = suit
        self.value = value
import random
class Deck:
    possibleSuit=["Hearts", "Diamonds", "Clubs", "Spades"]
    possibleValue=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    def __init__(self):
        self.deck=[]
        for i in range(4):
            for j in range(13):
                oneCard=Card(self.possibleSuit[i],self.possibleValue[j])
                self.deck.append(oneCard)

    
    def shuffle(self):
        random.shuffle(self.deck)
        return self.deck
    def deal(self):
        if len(self.deck)==0:
            return "No cards left"
        myCard=random.choice(self.deck)
        self.deck.remove(myCard)
        return myCard.suit, myCard.value

myDeck=Deck()
print(myDeck.deal())

