PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

price_list_list = PRICE_LIST.split('\n')

# new_dict = {}
#
# # for x in price_list_list:
# #     new_item = x.split(' ')
# #     item = new_item[0]
# #     price = int(new_item[1][:-1])
# #     new_dict[item] = price

new_dict = {x.split()[0]: int(x.split()[1][:-1]) for x in price_list_list}

# print(item)
# print(price)
print(new_dict)

