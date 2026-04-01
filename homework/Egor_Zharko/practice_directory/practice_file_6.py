text = "i love python automation"
words = text.split()
new_words = []

for word in words:
    first_letter = word[0].upper()
    rest = word[1:]
    new_words.append(first_letter + rest)
final_text = " ".join(new_words)
print(final_text)



