result = 'результат операции: 42'
result_1 ='результат операции: 514'
result_2 = 'результат работы программы: 9'

index = result.index(':')
index_1 = result_1.index(':')
index_2 = result_2.index(':')

resulting_number = result[index + 2:]
resulting_number_1 = result_1[index_1 + 2:]
resulting_number_2 = result_2[index_2 + 2:]

print(int(resulting_number) + 10)
print(int(resulting_number_1) + 10)
print(int(resulting_number_2) + 10)

