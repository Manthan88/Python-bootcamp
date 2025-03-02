import random
word_list = ["madrid", "munich", "city", "football", "trophy"]


#Step 1: Select a random word
chosen_word = random.choice(word_list)
print(chosen_word)

#Step 2: Get same number of - as word

dash = ""
for i in range(len(chosen_word)-1):
    dash += '_'
print(f"Word to guess: {dash}")


#Step 3: Ask user to guess the letter
lives = 6
c_list = []
game_over = False

while not game_over:
    guess = input("Guess the letter: ").lower()
    if guess in c_list:
        print(f"You've already guessed the letter {guess}. Guess again")
    display = ""

    for letter in chosen_word: #not included lives -=1 in this loop as this loop is just for when the guess is in the word. Not when the guess is not in the word
        if letter == guess:
            display += letter
            c_list.append(guess)
        elif letter in c_list:
            display += letter
        else: 
            display += "_"
            
    
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. Lives remaining {lives}/6 ")
        if lives == 0:
            print("You lose")
            game_over = True


    if "_" not in display and lives != 0:
        print("You Win")
        game_over = True


