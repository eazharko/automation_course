import sys
sys.set_int_max_str_digits(0)

def generator():
    number_1 = 0
    number_2 = 1
    while True:
        yield number_1
        next_number = number_1 + number_2
        number_1 = number_2
        number_2 = next_number
counter = 0
for number in generator():
    counter += 1
    if counter == 5 or counter == 200 or counter == 1000 or counter == 100000:
        print(number)
    if counter == 100000:
        break


