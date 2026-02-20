sentence = list(input().lower().split())
for word_ind in range(len(sentence)):
    if not sentence[word_ind].isalpha():
        sentence[word_ind] = (sentence[word_ind])[:-1]

for word in sentence:
    if sentence.count(word) == 2:
        print(word)
        break











