import game
import random

def main():
        
    def formatted_data(account):
        account_name = account["name"]
        account_descr = account["description"]
        account_country = account["country"]

        return f"{account_name}, a {account_descr}, from {account_country}"
    
    def compare(a,b, guess):
        a_followers = a["follower_count"]
        b_followers = b["follower_count"]
        
        if a_followers > b_followers:
            return guess == "a"
        else:
            return guess == "b"
    
    score = 0
    game_over = False
    item2 = random.choice(game.data)

    while game_over == False:
        item1 = item2
        item2 = random.choice(game.data)
        if item2 == item1:
            item2 = random.choice(game.data)

        print(f"Compare A: {formatted_data(item1)}")
        print(f"Against B: {formatted_data(item2)}")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        answer = compare(item1, item2, guess)

        if answer:
            score += 1
            print(f"You're right! Current Score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score {score}")
            game_over = True
        
    restart = input("Play again? 'Yes or 'No': ").lower()
    if restart == 'yes':
        main()
    else:
        print("Bye")

main()
        

