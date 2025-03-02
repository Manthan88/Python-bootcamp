import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

# #Ask user if they want to play
play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
def main():

    def display_score():
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first hand: {computer_cards[0]}")

    def total(card):
        if 11 in card and sum(card) > 21:
            card.remove(11)
            card.append(1)
        return sum(card)

#Start with 2 cards for user & computer
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(random.choice(cards))
        user_score = total(user_cards)
        computer_cards.append(random.choice(cards))
        computer_score = total(computer_cards)
    
    display_score()
    next_card = "y"

# Ask user if they want another card.
    while user_score <= 21 and next_card != "n":
        next_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if next_card == "y":
            user_cards.append(random.choice(cards))
            user_score = total(user_cards)
            display_score()
        elif next_card == "n":
            while computer_score <= 17: 
                computer_cards.append(random.choice(cards))
                computer_score = total(computer_cards)
            print(f"Your final hand: {user_cards}, current score: {user_score}")
            print(f"Computer's final hand: {computer_cards}, computer's final score: {computer_score}")

# For final part when user_score is more than 21
    if user_score <= 21 and computer_score <= 21:
        if user_score > computer_score:
            print("You Win")
        elif user_score < computer_score:
            print("You Lose")
        else:
            print("Draw")
    elif user_score <= 21 and computer_score > 21:
        print("You Win")
    else:
        print("You Lose")
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    main()
    print("\n"*20)
    

main()






            



            


