import random
def game():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    your_cards = []
    computer_cards = []
    for i in range(2):
        your_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
    sum_of_user = sum(your_cards)
    sum_of_computer = sum(computer_cards)

    print(f"Your cards: {your_cards}, current score: {sum_of_user}\nComputer's first card:{computer_cards[0]}")

    if sum_of_user == 21:
        print("YOU WON! ***BLACKJACK**")
        return
    if sum_of_computer == 21:
        print("YOU LOST! *** COMPUTER HAS BLACKJACK**")
        return

    continue_game = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    user = -1
    while continue_game == "y":
        your_cards.append(random.choice(cards))
        sum_of_user = sum(your_cards)

        
        if sum_of_user > 21:
            if 11 in your_cards:
                your_cards.remove(11)
                your_cards.append(1)
                print(f"Your cards: {your_cards}, current score: {sum(your_cards)}\nComputer's first card:{computer_cards[0]}")
            else:
                user = 1
                break
        else:
            print(f"Your cards: {your_cards}, current score: {sum(your_cards)}\nComputer's first card:{computer_cards[0]}")


        
        continue_game = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    
    
    # computer_deal = random.randint(0,1)
    while sum_of_computer < 17 and user != 1:
        computer_cards.append(random.choice(cards))
        sum_of_computer = sum(computer_cards)

        if sum_of_computer > 21 :
            if 11 in computer_cards:
                computer_cards.remove(11)
                computer_cards.append(1)
            else:
                user = 0
                break
        elif sum_of_computer == 21:
            user = -1
            break

        # computer_deal = random.randint(0,1)

    print(f"Your final hard: {your_cards}, final score: {sum_of_user}\nComputer's final hand:{computer_cards}, final score:{sum(computer_cards)}")

    if user == -1:
        if sum_of_user > sum_of_computer:
            print("You Won!")
        elif sum_of_user < sum_of_computer:
            print("You Lost!")
        else:
            print("Draw!")    
    else:
        if user == 0:
            print("YOU WON! **DEALER HAVE CARDS ABOVE 21**")
        elif user == 1:
            print("YOU LOST! **YOU HAVE CARDS ABOVE 21**")
            


yes_or_no = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if yes_or_no == "y":
    game()