from os.path import join

words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

def print_words(dictionary):
    for key, value in dictionary.items():
        print(key * value)
print_words(words)

