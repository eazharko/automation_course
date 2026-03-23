text = "результат операции: 42"
text2 = "результат операции: 54"
text3 = "результат работы программы: 209"
text4 = "результат: 2"

def string_to_number(result):
    number = result.split(": ")
    final_number = int(number[1])+10
    return final_number

print(string_to_number(text))
print(string_to_number(text2))
print(string_to_number(text3))
print(string_to_number(text4))