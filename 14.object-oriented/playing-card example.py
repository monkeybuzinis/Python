class Card:
    def __init__(self, value, suit):
        self.value=value
        self.suit=suit
    def __str__(self):
        names=['Jack','Queen','King','Ace']
        if self.value<=10:
            return '{} of {}'.format(self.value,self.suit)
        else:
            return '{} of {}'.format(names[self.value-11],self.suit)
            
import random
class Card_group:
    def __init__(self,cards=[]):
        self.cards=cards
    def nextCard(self):
        return self.cards.pop(0)
    def hasCard(self):
        return len(self.cards)>0
    def size(self):
        return len(self.cards)
    def shuffle(self):
        random.shuffle(self.cards)
    
class Standard_deck(Card_group):
    def __init__(self):
        self.cards=[]
        for s in ['Heart','Diamond','Club','Spades']:
            for v in range (2,15):
                self.cards.append(Card(v,s))

class Pinochle_deck(Card_group):
    def __init__(self):
        self.cards=[]
        for s in ['Heart','Diamond','Club','Spades']*2:
            for v in range (9,15):
                self.cards.append(Card(v,s))

deck= Standard_deck()
deck.shuffle()

new_card=deck.nextCard()
print('\n',new_card)
choice=input("higher (h) or lower (l): ")
streak=0

while (choice=='h' or choice=='l'):
    if not deck.hasCard():
        deck = Standard_deck()
        deck.shuffle()

    old_card = new_card
    new_card = deck.nextCard()

    if (choice.lower()=='h' and new_card.value>old_card.value or\
        choice.lower()=='l' and new_card.value<old_card.value):
        streak = streak + 1
        print("Right! That's", streak, "in a row!")

    elif (choice.lower()=='h' and new_card.value<old_card.value or\
        choice.lower()=='l' and new_card.value>old_card.value):
        streak = 0
        print('Wrong.')

    else:
        print('Push.')

    print('\n', new_card)
    choice = input("Higher (h) or lower (l): ")