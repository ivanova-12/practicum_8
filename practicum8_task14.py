hint = input()
right_word = list(input().lower())
for cnt in range(25):
    print('')
print(hint)
print('*' * len(right_word))
s = list('*' * len(right_word))

def all_indexes(list1, element):
    indexes = []
    for index, value in enumerate(list1):
        if value == element:
            indexes.append(index)
    return indexes

flag = False
for cnt in range(10):
    print('Буква или слово (0 - буква, 1 - слово)?')
    number = int(input())
    if number == 1:
        word = input()
        if word.lower() == ''.join(right_word):
            flag = True
            break
        else:
            break
    else:
        letter = input()
        if letter.lower() in right_word:
            list_of_indexes = all_indexes(right_word, letter.lower())
            for index1 in list_of_indexes:
                s[index1] = letter.lower()
            print(''.join(s))
        else:
            print(''.join(s))

if flag:
    print('Победа!')
else:
    print('Проигрыш!')







