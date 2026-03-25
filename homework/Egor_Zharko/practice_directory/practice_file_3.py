numbers = [4, -2, 7, -5, 10, -1]
positive_numbers = []
for number in numbers:
    if number > 0:
        positive_numbers.append(number)
sum_of_numbers = sum(positive_numbers)
print(sum_of_numbers)