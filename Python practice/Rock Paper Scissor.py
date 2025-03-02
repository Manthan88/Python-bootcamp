import random

options = ["Rock", "Paper", "Scissors"]
comp = random.choice(options)

user = input("What do you select 0 for rock, 1 for paper or 2 for scissors?\n")
print(f"Computer played: {comp}")

if comp == options[0] and user == options[2]:
    print("Comuputer wins")
elif comp == options[0] and user == options[1]:
    print("User wins")
elif comp == options[1] and user == options[0]:
    print("Comuputer wins")
elif comp == options[1] and user == options[2]:
    print("User wins")
elif comp == options[2] and user == options[1]:
    print("Comuputer wins")
elif comp == options[2] and user == options[0]:
    print("User wins")
else:
    print("Its a draw, try again") 

