user_string = input("Please enter a string.")
reversed = ""
 
for item in range(len(user_string) - 1, -1, -1):
    reversed += user_string[item]
 
print(reversed)



def word_counter(words):
    spaces_and_letters = ""
    word_count = 1
    for i in words:
        if i.isalnum() or i.isspace() or i == "-" or i == "'":
            spaces_and_letters += i
    for j in spaces_and_letters:
        if j == " ":
            word_count += 1
    return word_count
 
print(word_counter(user_string))
