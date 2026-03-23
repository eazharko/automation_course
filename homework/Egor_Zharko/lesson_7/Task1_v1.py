correct_number = 7
while True:
    user_input = input("Guess a digit")
    if user_input.isdigit():
        user_input = int(user_input)
        if user_input != correct_number:
            print("Wrong guess, try again")
            continue
        else:
            print("Congratulations,you're correct" )
            break
    else:
        print("Please, enter a number")