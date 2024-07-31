# Write loop that prompts user to enter a series of pizza toppings, if they enter 'quit' end program
pizzaPrompt = True

while pizzaPrompt:
    userPizza = input("What pizza topping would you like? (enter 'quit to stop) ")
    if userPizza != 'quit':
        print(f"I will add {userPizza} to your pizza!")
    else:
        pizzaPrompt = False
        break