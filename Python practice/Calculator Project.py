def addition(n1, n2):
    return n1+n2

def subtraction(n1, n2):
    return n1-n2

def multiplication(n1, n2):
    return n1*n2

def division(n1, n2):
    return n1/n2
 

operations = {
    "+" : addition,
    "-" : subtraction,
    "*" : multiplication,
    "/" : division
}

def calculator():
    should_continue = True
    num1 = float(input("What's the first number?: "))

    while should_continue:
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        for i in operations:
            if i == operation:
                result = operations[i](num1, num2)
            else:
                print("You entered an invalid operator. Try again")
                restart = "n"
        print(f"{num1} {operation} {num2} = {result}")
        restart = input(f"Type 'y' to continute calculating with {result}, or type 'n' to start a new calculation: ")

        if restart == "y":
            num1 = result
        elif restart == "n":
            print("\n"*20)
            calculator()
            '''recursion - calling a funtion inside itself
            while loop is also acceptable'''
        else:
            return


calculator()