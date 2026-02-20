sentence = list(input().split())
end = []
for word_ind in range(len(sentence)):
    if not sentence[word_ind].isalpha():
        sentence[word_ind] = (sentence[word_ind])[:-1]

for word in sentence:
    end.append(len(word))
print(min(end))










