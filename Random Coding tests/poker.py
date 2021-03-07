'''
Design a poker game

1. U cn assume that the cards are only marked from 2-10
2. For now, lets assume that you are only given 3 rules
	a. Two pair
	b. Straight
	c. Flush


New usecases:
0. There will be multiple games running in this app at a time where  
1. What if I want to change the priority of the two pair rule?
2. What if I want to add a new rule with its own priority?
3. What if I want to add the J, Q, K, A cards?
'''
class Symbol:
    self.clubs = 0
    self.diamonds = 1
    self.hearts = 2
    self.spades = 3


class Color:
    self.red = 0
    self.black = 0


class Card:
    def __init__(self, number, color, symbol):
        self.printingValue = number
        self.value = value
        self.color = color
        self.symbol = symbol


class Rule:
    def check(self):
        pass


class User:
    def __init__(self, cards):
        self.cards = cards
        self.status = None


class Flush(Rule):
    def __init__(self):
        self.pr
        super().__init__()

    def check(self, cards):
        cards = set([card.color for card in cards])
        return True if len(cards) == 1 else False


class Straight(Rule):
    def __init__(self):
        super().__init__()

    def check(self, cards):
        # cards = sorted(cards,key= lambda x:x.number) logicv
        return True


class TwoPairs(Rule):
    def __init__(self):
        super().__init__()

    def check(self, cards):
        cards = sorted(cards, key=lambda x: x.number)
        return True


class Poker:
    def __init__(self, cards):
        self.bunch_of_cards = []
        self.deck = cards
        self.users = []
        self.is_completed = False
        self.rules = reversed([TwoPairs(), Straight(), Flush()])

    def get_winner(self):
        for user in self.users:
            for rule in rules:
                if rule.check([*user.cards, *self.deck]):
                    user.status = rule
                    break
        final_winner = user
        self.is_completed = True
        return final_winner

    def add_user(self, user):
        if self.is_completed:
            return False
        user.cards = self.bunch_of_cards.pop()
        return


class Solution:
    def function():
        self.val = 0

    def function(val):
        self.val += 1
        return


