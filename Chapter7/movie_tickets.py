# Depending on user input on age, use while-loop to tell movie ticket price
while True:
    userAge = "How old are you? \n(type 'quit' to end): "
    userAge = input(userAge)
    if userAge == 'quit':
        break
    else:
        userAge = int(userAge)
        if userAge < 3:
            print("The ticket is free")
            continue
        elif (userAge >= 3) and (userAge <= 12):
            print("The ticket is $10")
            continue
        else:
            print("The ticket is $15")
            continue

