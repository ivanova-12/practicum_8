sentence = input()
words = sentence[:-1].split()
words.sort(key=lambda word: sum(letter.isalpha() for letter in word))

print(' '.join(words).capitalize() + sentence[-1])