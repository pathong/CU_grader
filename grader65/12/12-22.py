class Card:
    def __init__(self, _value:str, _suit:str):
        self.value = _value
        self.suit = _suit
    def __str__(self):
        return "({} {})".format(self.value, self.suit)

    def getScore(self):
        if self.value == "A": return 1
        if self.value.isnumeric(): return int(self.value)
        if self.value in "JQK" : return 10
        return 0

    def sum(self,rhs):
        return (Card.getScore(self) + Card.getScore(rhs))%10

    def __lt__(self, rhs):
        order_value = '345678910JQKA2'
        order_suit = ['club','diamond','heart','spade']
        vs = order_value.index(self.value)
        vr = order_value.index(rhs.value)

        if vs != vr: return vs < vr
        else:
            ss = order_suit.index(self.suit)
            sr = order_suit.index(rhs.suit)
            return ss < sr

n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].getScore())
print("----------")
for i in range(n-1):
    print(Card.sum(cards[i], cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
    print(cards[i])
