alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def main():
    direction = input("Type encode to encrypt, type decode to decrypt:\n").lower()
    text = input("Enter your message:\n").lower()
    shift = input("Enter shift:\n")

    if direction == "encrypt":
        encrypt(text,shift)
    elif direction == "decrypt":
        decrypt(text,shift)
    else:
        print("You typed something else than encrypt or decrypt.")

    restart = input("Do you want to continue? Yes or No?")
    if restart == "No":
        should_continue = False
        print("Bye")

def encrypt(text,shift):
    new_text = ""
    for i in text:
        if i in alphabet:
            new_pos= (alphabet.index(i) + int(shift))               #Below logic is fine, but won;t work when the shift is above 25
            new_pos %= len(alphabet)                                #if new_pos > len(alphabet) -1:
                                                                    #new_pos = alphabet.index(i) - len(alphabet) + int(shift)
            new_text += alphabet[new_pos]
    print(f"Here is you encoded text: {new_text}")


def decrypt(text, shift):
    new_text = ""
    for i in text:
        if i in alphabet:
            new_pos= (alphabet.index(i) - int(shift))               
            new_pos %= len(alphabet)                                
            new_text += alphabet[new_pos]
    print(f"Here is you decoded text: {new_text}")


should_continue = True
while should_continue:
    main()