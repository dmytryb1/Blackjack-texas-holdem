import random

# Base deck of cards
cards = {'h1': 1, 'h2': 2, 'h3': 3, 'h4': 4, 'h5': 5, 'h6': 6, 'h7': 7, 'h8': 8, 'h9': 9, 'h10': 10,
         'hj': 10, 'hq': 10, 'hk': 10,
         'd1': 1, 'd2': 2, 'd3': 3, 'd4': 4, 'd5': 5, 'd6': 6, 'd7': 7, 'd8': 8, 'd9': 9, 'd10': 10,
         'dj': 10, 'dq': 10, 'dk': 10,
         's1': 1, 's2': 2, 's3': 3, 's4': 4, 's5': 5, 's6': 6, 's7': 7, 's8': 8, 's9': 9, 's10': 10,
         'sj': 10, 'sq': 10, 'sk': 10,
         'c1': 1, 'c2': 2, 'c3': 3, 'c4': 4, 'c5': 5, 'c6': 6, 'c7': 7, 'c8': 8, 'c9': 9, 'c10': 10,
         'cj': 10, 'cq': 10, 'ck': 10}
# dealth card
#dealtcard = random.choice(list(cards))
#print(dealtcard)

# remove dealt card from deck
#cards.pop(dealtcard)
#print(cards)

# Turns
playing = True
while playing == True:
    card1 = random.choice(list(cards))
    valcard1 = cards[card1]
    if valcard1 == 1:
        valcard1 = 11
    cards.pop(card1)
    card2 = random.choice(list(cards))
    valcard2 = cards[card2]
    if valcard2 == 1 and valcard1 != 11:
        valcard2 = 11
    cards.pop(card2)
    print(card1 + ' ' + card2)
    comphand = valcard1 + valcard2
    print(comphand)
    if comphand == 21:
        print("Computer got Blackjack!")
        playing = False
    if 17 <= comphand <= 21:
        print('stay')
        playing = False
    if comphand <= 16:
        card3 = random.choice(list(cards))
        valcard3 = cards[card3]
        cards.pop(card3)
        comphand = valcard1 + valcard2 + valcard3
        print(card1 + ' ' + card2 + ' ' + card3)
        print(comphand)
        if comphand > 21 and valcard1 == 11:
            valcard1 == 1
            comphand = valcard1 + valcard2 + valcard3
        if comphand > 21 and valcard2 == 11:
            valcard2 == 1
            comphand = valcard1 + valcard2 + valcard3
        if comphand > 21:
            print("You Bust")
            playing = False
        if comphand >= 17 and comphand <= 21:
            print('stay')
            playing = False
        if comphand <= 16:
            card4 = random.choice(list(cards))
            valcard4 = cards[card4]
            cards.pop(card4)
            comphand = valcard1 + valcard2 + valcard3 + valcard4
            print(card1 + ' ' + card2 + ' ' + card3 + ' ' + card4)
            print(comphand)
            if comphand > 21 and valcard1 == 11:
                valcard1 == 1
                comphand = valcard1 + valcard2 + valcard3 + valcard4
            if comphand > 21 and valcard2 == 11:
                valcard2 == 1
                comphand = valcard1 + valcard2 + valcard3 + valcard4
            if comphand > 21:
                print("You Bust")
                playing = False
            if comphand >= 17 and comphand <= 21:
                print('stay')
                playing = False
            if comphand <= 16:
                card5 = random.choice(list(cards))
                valcard5 = cards[card5]
                cards.pop(card5)
                comphand = valcard1 + valcard2 + valcard3 + valcard4 + valcard5
                print(card1 + ' ' + card2 + ' ' + card3 + ' ' + card4 + ' ' + card5)
                print(comphand)
                if comphand > 21 and valcard1 == 11:
                    valcard1 == 1
                    comphand = valcard1 + valcard2 + valcard3 + valcard5
                if comphand > 21 and valcard2 == 11:
                    valcard2 == 1
                    comphand = valcard1 + valcard2 + valcard3 + valcard5
                if comphand > 21:
                    print("You Bust")
                    playing = False
                if comphand >= 17 and comphand <= 21:
                    print('stay')
                    playing = False
                if comphand <= 16:
                    card6 = random.choice(list(cards))
                    valcard6 = cards[card6]
                    cards.pop(card6)
                    comphand = valcard1 + valcard2 + valcard3 + valcard4 + valcard5 + valcard6
                    print(card1 + ' ' + card2 + ' ' + card3 + ' ' + card4 + ' ' + card5 + ' ' + card6)
                    print(comphand)
                    if comphand > 21 and valcard1 == 11:
                        valcard1 == 1
                        comphand = valcard1 + valcard2 + valcard3 + valcard6
                    if comphand > 21 and valcard2 == 11:
                        valcard2 == 1
                        comphand = valcard1 + valcard2 + valcard3 + valcard6
                    if comphand > 21:
                        print("You Bust")
                        playing = False
                    if comphand >= 17 and comphand <= 21:
                        print('stay')
                        playing = False
                    else:
                        print("You Bust")
                        playing = False

