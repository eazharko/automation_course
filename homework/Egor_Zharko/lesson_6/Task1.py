text = """Etiam tincidunt neque erat, quis molestie enim imperdiet vel.
Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"""
words = text.split()
fin_words = []

for word in words:
    punct = ''
    if word.endswith(','):
        punct = ','
        word = word[:-1]
    elif word.endswith('.'):
        punct = '.'
        word = word[:-1]
    word = word + 'ing'
    word = word + punct
    fin_words.append(word)

final_text = " ".join(fin_words)
print(final_text)
