class Card:
    def __init__(self,rank,suit):
        d={'A':'ace', 'J':'jack','Q':'queen', 'K':'king', 'C':'clubs' ,'D':'diamonds' ,'H': 'hearts' ,'S': 'spades'}
        if type(rank)==int:
            self.rank=str(rank)
            self.suit=d[suit]
        else:
            self.rank=d[rank]
            self.suit=d[suit]
    def __str__(self):
        return 'Card: '+self.rank+' of '+self.suit
    def __repr__(self):
        return str(self)
    def __eq__(self,other):
        print("execute __eq__")
        return self.suit<other.suit
    def __lt__(self,other):
        
        if other.rank==self.rank:
            Card.__eq__(self,other)
        else:
            print("execute __lt__")
            return self.rank<other.rank

        
if __name__ == "__main__":
    cards = []
    cards.append(Card('A', 'D'))
    cards.append(Card(10, 'S'))
    cards.append(Card('K', 'H'))
    cards.append(Card('A', 'C'))
    cards.append(Card(3, 'S'))
    cards.append(Card(3, 'D'))
    # print(Card('A', 'D')<Card(10, 'S'))
    print(cards)
    cards.sort()
    print(cards)