class Card:
    order = []
    def __init__(self, _value, _suit):
        self.value = _value
        self.suit = _suit

    def __str__(self):
        return "({} {})".format(self.value, self.suit)


    def next1(self):
        values = [ '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K','A', '2']
        suits = ['club','diamond','heart','spade']

        nv = self.value 
        ns = self.suit 
        if self.suit != suits[-1]:
            ns = suits[suits.index(self.suit) + 1]
        if self.suit == suits[-1]:
            ns = suits[0]
            if self.value != values[-1]:
                nv = values[values.index(self.value) + 1]
            else:
                nv = values[0]


        return Card(nv,ns)

    def next2(self):
        values = [ '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K','A', '2']
        suits = ['club','diamond','heart','spade']

        nv = self.value 
        ns = self.suit 
        if self.suit != suits[-1]:
            ns = suits[suits.index(self.suit) + 1]
        if self.suit == suits[-1]:
            ns = suits[0]
            if self.value != values[-1]:
                nv = values[values.index(self.value) + 1]
            else:
                nv = values[0]
                ns = suits[0]

        self.value = nv
        self.suit = ns



n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())

print("----------")
for i in range(n):
     print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])







