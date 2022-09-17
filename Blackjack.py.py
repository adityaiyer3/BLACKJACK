import random
from turtle import title
Cards = []
Winner = []
Lossers = []
Lossers_cards = []
Winner_cards = []
Tie = []

Suits = ["Spades", "Club", "Hearts", "Diamonds"]
Ranks = [
    {"Rank":"A","Value":1},
    {"Rank":"2","Value":2},
    {"Rank":"3","Value":3},
    {"Rank":"4","Value":4},
    {"Rank":"5","Value":5},
    {"Rank":"6","Value":6},
    {"Rank":"7","Value":7},
    {"Rank":"8","Value":8},
    {"Rank":"9","Value":9},
    {"Rank":"10","Value":10},
    {"Rank":"J","Value":10},
    {"Rank":"Q","Value":10},
    {"Rank":"K","Value":10},
    ]
for suit in Suits:
    for rank in Ranks:
        Cards.append([suit, rank])

#Definations
def shuffle():
    random.shuffle(Cards)
def Dealer():
    Held = []
    for x in range(2):
        card=Cards.pop()
        Held.append(card)
    return Held
def Distribute():
    Held = []
    for x in range(2):
        card=Cards.pop()
        Held.append(card)
    return Held
def Play():
    a = input("Hit or Stay?")
    if a.title() == "Hit" :
        Hit = Cards.pop()
    else :
        Hit = ""
    return Hit
def chk_val(a) :
    p=0
    Tot_val = 0
    for item in a:
        cur_val = a[p][1]['Value']
        Tot_val = Tot_val + cur_val
        p=p+1
    k=0
    for item in a:
        if a[k][1]['Value'] == 1 :
            if Tot_val + 10 <= 21:
                Tot_val = Tot_val + 10
        k=k+1
    return Tot_val
def Round():
    hit_card = Play()
    Player_Cards[l-1].append(hit_card)
    #To remove empty items in list
    while("" in Player_Cards[l-1]):
        Player_Cards[l-1].remove("")
    print(Player_Cards[l-1])
    Tot_val =chk_val(Player_Cards[l-1])
    print("Current Value : " + str(Tot_val))
    print("")
    if hit_card != "" and Tot_val < 21 :
        Round()
    elif Tot_val > 21 :
        print("BUSTERED! YOU LOST")
        print("")
        Lossers.append("Player"+str(l))
        Lossers_cards.append(Player_Cards[l-1])
    elif Tot_val == 21 :
        print("CONGRATULATIONS! YOU WON BLACKJACK")
        print("")
        Winner.append("Player "+str(l))
        Winner_cards.append(Player_Cards[l-1])

 
#GAME START

shuffle()

Players = int(input("Enter the number of Players :"))
Dealer_Cards= Dealer()
#PLAYER CARD DISTRIBUTION
Player_Cards = []
for p in range(Players):
    xyz = Distribute()
    Player_Cards.append(xyz)
    
#DISPLAY OF CARDS    
k=1
for q in Player_Cards :
    value = q[0][1]['Value']+q[1][1]['Value']
    if q[0][1]['Value'] == 1 or q[1][1]['Value'] == 1 :
        if value + 10 <= 21 :
            value = value + 10
    if value == 21 :
        res = "  BLACKJACK !!!!!!!!"
        Winner.append("Player " + str(k))
    else :
        res = ""
    print("Player "+ str(k)+": "+str(q) + " Total Value : " + str(value) + str(res))
    k=k+1 
print("Dealer's Card:" + str(Dealer_Cards[1]))
print("")

l=1
#ROUND_1
for q in Player_Cards :
    if chk_val(q) != 21 :
        print("Player "+ str(l) + " :" )
        Round()
    l=l+1
Holding_Cards = [x for x in Player_Cards if x not in (Winner_cards or Lossers_cards)]
n = 0

if Winner == [] :
    Winner.append("None")
if Lossers == [] :
    Lossers.append("None")
if Tie == [] :
    Tie.append("None")
    
print("")
if len(Holding_Cards) > 0 :
    print("Current Winners: " + str(Winner))
    print("Current Lossers: "+ str(Lossers))
    print("")
    dealer_val = chk_val(Dealer_Cards)
    print("Dealer Cards: " + str(Dealer_Cards))
    print("Dealer's Card Value : " + str(dealer_val))
    print("")
    while dealer_val <= 16:
        card_1 = Cards.pop()
        Dealer_Cards.append(card_1)
        dealer_val = chk_val(Dealer_Cards)
    print("Dealer Cards: " + str(Dealer_Cards))
    print("Dealer's Card Value : " + str(dealer_val))
    print("")
    for item in Holding_Cards:
        if dealer_val > 21 :
            Winner.append("Player " + str(Player_Cards.index(Holding_Cards[n])+1))
            n=n+1
        elif chk_val(Holding_Cards[n]) > dealer_val and dealer_val < 21 :
            Winner.append("Player " + str(Player_Cards.index(Holding_Cards[n])+1))
            n=n+1
        elif chk_val(Holding_Cards[n]) < dealer_val and dealer_val < 21 :
            Lossers.append("Player " + str(Player_Cards.index(Holding_Cards[n])+1))
            n=n+1
        elif dealer_val == 21 :
            Lossers.append("Player " + str(Player_Cards.index(Holding_Cards[n])+1))
            n=n+1
        else :
            Tie.append("Player " + str(Player_Cards.index(Holding_Cards[n])+1))
            n=n+1

    if len(Winner) > 1 :
        while("None" in Winner):
            Winner.remove("None")
    if len(Lossers) > 1 :
        while("None" in Lossers):
            Lossers.remove("None")
    if len(Tie) > 1 :
        while("None" in Tie):
            Tie.remove("None")

    print("Winners: " + str(set(Winner)))
    print("Lossers: "+ str(set(Lossers)))
    print("Tie: "+ str(set(Tie)))
else:
    print("Winners: " + str(set(Winner)))
    print("Lossers: "+ str(set(Lossers)))
    print("Tie: "+ str(set(Tie)))