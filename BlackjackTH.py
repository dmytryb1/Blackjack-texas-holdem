import random

value_card_one = 0
value_card_two = 0
value_card_three = 0
value_card_four = 0
value_card_five = 0
value_card_six = 0
value_card_seven = 0

# Base deck of cards
cards = {'h1': 1, 'h2': 2, 'h3': 3, 'h4': 4, 'h5': 5, 'h6': 6, 'h7': 7, 'h8': 8, 'h9': 9, 'h10': 10,
         'hj': 10, 'hq': 10, 'hk': 10,
         'd1': 1, 'd2': 2, 'd3': 3, 'd4': 4, 'd5': 5, 'd6': 6, 'd7': 7, 'd8': 8, 'd9': 9, 'd10': 10,
         'dj': 10, 'dq': 10, 'dk': 10,
         's1': 1, 's2': 2, 's3': 3, 's4': 4, 's5': 5, 's6': 6, 's7': 7, 's8': 8, 's9': 9, 's10': 10,
         'sj': 10, 'sq': 10, 'sk': 10,
         'c1': 1, 'c2': 2, 'c3': 3, 'c4': 4, 'c5': 5, 'c6': 6, 'c7': 7, 'c8': 8, 'c9': 9, 'c10': 10,
         'cj': 10, 'cq': 10, 'ck': 10}



# Turns
playing = True
while playing == True:
    card_one = random.choice(list(cards))
    value_card_one = cards[card_one]
    if value_card_one == 1:
        value_card_one = 11
    cards.pop(card_one)
    card_two = random.choice(list(cards))
    value_card_two = cards[card_two]
    if value_card_two == 1 and value_card_one != 11:
        value_card_two = 11
    cards.pop(card_two)
    print(card_one + ' ' + card_two)
    computer_hand = value_card_one + value_card_two
    print(computer_hand)
    if computer_hand == 21:
        print("Computer got Blackjack!")
        playing = False
        break
    if 17 <= computer_hand <= 21:
        print('stay')
        playing = False
    if computer_hand <= 16:
        card_three = random.choice(list(cards))
        value_card_three = cards[card_three]
        cards.pop(card_three)
        if value_card_three == 1:
            value_card_three = 11
        computer_hand = value_card_one + value_card_two + value_card_three
        print(card_one + ' ' + card_two + ' ' + card_three)
        if computer_hand > 21 and value_card_one == 11:
            value_card_one = 1
            computer_hand = value_card_one + value_card_two + value_card_three
        if computer_hand > 21 and value_card_two == 11:
            value_card_two = 1
            computer_hand = value_card_one + value_card_two + value_card_three
        if computer_hand > 21 and value_card_three == 11:
            value_card_three = 1
            computer_hand = value_card_one + value_card_two + value_card_three + value_card_four
        if computer_hand > 21 and value_card_four == 11:
            value_card_four = 1
            computer_hand = value_card_one + value_card_two + value_card_three + value_card_four + value_card_five
        print(computer_hand)
        if computer_hand > 21:
            print("You Bust")
            playing = False
        if 17 <= computer_hand <= 21:
            print('stay')
            playing = False
        if computer_hand <= 16:
            card_four = random.choice(list(cards))
            value_card_four = cards[card_four]
            cards.pop(card_four)
            if value_card_four == 1:
                value_card_four = 11
            computer_hand = value_card_one + value_card_two + value_card_three + value_card_four
            print(card_one + ' ' + card_two + ' ' + card_three + ' ' + card_four)
            if computer_hand > 21 and value_card_one == 11:
                value_card_one = 1
                computer_hand = value_card_one + value_card_two + value_card_three
            if computer_hand > 21 and value_card_two == 11:
                value_card_two = 1
                computer_hand = value_card_one + value_card_two + value_card_three
            if computer_hand > 21 and value_card_three == 11:
                value_card_three = 1
                computer_hand = value_card_one + value_card_two + value_card_three + value_card_four
            if computer_hand > 21 and value_card_four == 11:
                value_card_four = 1
                computer_hand = value_card_one + value_card_two + value_card_three + value_card_four + value_card_five
            print(computer_hand)
            if computer_hand > 21:
                print("You Bust")
                playing = False
            if 17 <= computer_hand <= 21:
                print('stay')
                playing = False
            if computer_hand <= 16:
                card_five = random.choice(list(cards))
                value_card_five = cards[card_five]
                cards.pop(card_five)
                if value_card_five == 1:
                    value_card_five = 11
                computer_hand = value_card_one + value_card_two + value_card_three + value_card_four + value_card_five
                print(card_one + ' ' + card_two + ' ' + card_three + ' ' + card_four + ' ' + card_five)
                if computer_hand > 21 and value_card_one == 11:
                    value_card_one = 1
                    computer_hand = value_card_one + value_card_two + value_card_three
                if computer_hand > 21 and value_card_two == 11:
                    value_card_two = 1
                    computer_hand = value_card_one + value_card_two + value_card_three
                if computer_hand > 21 and value_card_three == 11:
                    value_card_three = 1
                    computer_hand = value_card_one + value_card_two + value_card_three + value_card_four
                if computer_hand > 21 and value_card_four == 11:
                    value_card_four = 1
                    computer_hand = value_card_one + value_card_two + value_card_three + value_card_four + value_card_five
                print(computer_hand)
                if computer_hand > 21:
                    print("You Bust")
                    playing = False
                if 17 <= computer_hand <= 21:
                    print('stay')
                    playing = False
                if computer_hand <= 16:
                    card_six = random.choice(list(cards))
                    value_card_six = cards[card_six]
                    cards.pop(card_six)
                    if value_card_six == 1:
                        value_card_six = 11
                    computer_hand = value_card_one + value_card_two + value_card_three + value_card_four + value_card_five + value_card_six
                    print(card_one + ' ' + card_two + ' ' + card_three + ' ' + card_four + ' ' + card_five + ' ' + card_six)
                    if computer_hand > 21 and value_card_one == 11:
                        value_card_one = 1
                        computer_hand = value_card_one + value_card_two + value_card_three
                    if computer_hand > 21 and value_card_two == 11:
                        value_card_two = 1
                        computer_hand = value_card_one + value_card_two + value_card_three
                    if computer_hand > 21 and value_card_three == 11:
                        value_card_three = 1
                        computer_hand = value_card_one + value_card_two + value_card_three + value_card_four
                    if computer_hand > 21 and value_card_four == 11:
                        value_card_four = 1
                        computer_hand = value_card_one + value_card_two + value_card_three + value_card_four + value_card_five
                        print(computer_hand)
                    if computer_hand > 21:
                        print("You Bust")
                        playing = False
                    if 17 <= computer_hand <= 21:
                        print('stay')
                        playing = False
                    else:
                        print("You Bust")
                        playing = False
