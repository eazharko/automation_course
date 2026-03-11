my_dict = {'tuple': (1, 2.5, "text", True, 5),
           'list': ['el1', 'el2', 'el3', 'el4', 'el5'],
           'dict': {
               'key1': 'value1',
               'key2': 'value2',
               'key3': 'value3',
               'key4': 'value4',
               'key5': 'value5'
           },
           'set': {0, 1, 2, 3, 4}
}
print(my_dict['tuple'][-1])
my_dict['list'].append('el6')
my_dict['list'].pop(1)
my_dict['dict']['i am a tuple'] = 'any_value'
my_dict['dict'].pop('key3')
my_dict['set'].add(5)
my_dict['set'].pop()
print(my_dict)