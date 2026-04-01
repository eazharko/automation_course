text = "automation"
vowels = "aeiou"
consonants_text = ""
for letter in text:
    if letter not in vowels:
        consonants_text += letter
print(consonants_text)