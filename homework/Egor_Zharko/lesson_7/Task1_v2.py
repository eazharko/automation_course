correct_number = 7
while True:
    try:
        user_input = int(input("Guess a digit"))
        if user_input != correct_number:
            print("Wrong guess, try again")
            continue
        else:
            print("Congratulations,you're correct")
            break
    except:
        print("Please, enter a number")