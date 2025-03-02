auct_dict = {}    
restart = True

def winning_bid(dict):
    max_counter = 0
    winner = ""
    for bidder in dict:         
        highest_bid = dict[bidder]
        if highest_bid > max_counter:                               #can also use max function.
            max_counter = highest_bid                               #max(dictionary_name, key = dictionary_name.get)
            winner = bidder                                         # this gives the key with the max value. Can use the key to get the value then for print func.
    print(f"The winner is {winner} with a bid of {max_counter}")

while restart:
    name = input("Enter your name:\n")
    bid = int(input("Enter your bid: $\n"))
    auct_dict[name] = bid
    users = input("Are there any other users? Yes or No?\n").lower()

    if users == "no":
        restart = False
        winning_bid(auct_dict)
    else:
        print("\n"*20)



