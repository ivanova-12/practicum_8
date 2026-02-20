sentence = input().lower()

if sentence.isalpha():
        print(len(set(sentence)))
else:
    set_alpha = set()
    for word in sentence:
        if word.isalpha():
            set_alpha.add(word)
    print(len(set_alpha))






