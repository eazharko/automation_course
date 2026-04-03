import random

while True:
    salary = input("Enter your salary: ")
    if salary.isdigit():
        salary = int(salary)
        break
    else: print("Please enter a numeric value")

final_salary = salary
bonus = random.choice([True, False])

if bonus == True:
    final_salary = salary + int(random.random() * 100)

print(f"{salary}, {bonus} - '${final_salary}'")







