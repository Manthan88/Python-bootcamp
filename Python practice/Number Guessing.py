import random
def main():
    num = random.randrange(0,101)
    print("Welcome to the Number Guessing Game!!\nI'm thinking of a number between 1 and 100.")

    def difficulty_level():
        level = input("Choose a difficulty. Type 'hard' or 'easy': ").lower()
        if level == "hard":
            return 5
        if level == "easy":
            return 10
    
    def compare(user_guess, actual_num, lives):
        if user_guess < actual_num:
            print("Too low")
            return lives - 1
        elif user_guess > actual_num:
            print("Too high")
            return lives - 1
        else:
            print(f"You got it! the answer was {guess}")
                   

    turns = difficulty_level()
    guess = 0
    ''' Did not use any boolean value like game_over = True/False to initiate a while loop 
    because the game_over variable would be a global scope and could not be defined in the compare function
     where the game_over = True would have to be included in the else clause '''

    while guess != num:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        turns = compare(guess, num, turns)
        if turns == 0:
            print("You've run out of guesses")
        

    restart = input("Do you want to play again? 'Yes' or 'No': ").lower()
    if restart == 'yes':
        main()
    else:
        print("Bye!")

main()


''' It is recommended not to modify the glabl scope. A workaround is to use return statements in functions
so that the function result (in this case the return value) can be stored in a global scope variable'''

        
            




