sentence = list(input().lower().split())

for word_ind in range(len(sentence)):
    if not sentence[word_ind].isalpha():
        sentence[word_ind] = (sentence[word_ind])[:-1]

for word_ind in range(len(sentence)):
    if (sentence[word_ind] != sentence[0]
            and len(set(sentence[word_ind])) == len(sentence[word_ind])):
        print(sentence[word_ind], end=' ')











