class Symbol:
    self.clubs=0
    self.diamonds=1
    self.hearts=2
    self.spades=3

class Color:
    self.red=0
    self.black=0

class Card:
    def __init__(self,number,color,symbol):
        self.number=number
        self.color=color
        self.symbol=symbol

class Rule:
    def check(self):
        pass

class User:
    def __init__(self,cards):
        self.cards=cards
        self.status=None

class Flush(Rule):
    def __init__(self):
        super().__init__()
    def check(self,cards):
        cards=set([card.color for card in cards])
        return True if len(cards)==1 else False

class Straight(Rule):
    def __init__(self):
        super().__init__()
    def check(self,cards):
        cards = sorted(cards,key= lambda x:x.number)
        return True 

class TwoPairs(Rule):
    def __init__(self):
        super().__init__()
    def check(self,cards):
        cards = sorted(cards,key= lambda x:x.number)
        return True 


class Poker:
    def __init__(self,cards):
        self.deck=cards
        self.users=[]
        self.is_completed=False
        self.rules=reversed([TwoPairs(),Straight(),Flush()])

    def get_winner(self):
        for user in self.users:
            for rule in rules:
                if rule.check([*user.cards,*self.deck]):
                    user.status=rule
                    break
        final_winner=user
        self.is_completed=True
        return final_winner


