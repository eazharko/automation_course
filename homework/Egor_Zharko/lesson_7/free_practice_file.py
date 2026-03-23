def title_price(**kwargs):
    print(kwargs)
    print(kwargs.items())
    for k, v in kwargs.items():
        if k == 'key3':
            print('goodbye')
            break
        print(f"Key = {k} and Value = {v}")
title_price(key="value", key1="value1", key2="value2", key3="value3" )


words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

def print_words(dictionary):
    result = []
    for key, value in dictionary.items():
        output = key * value
        result.append(output)
    print(" ".join(result))
print_words(words)