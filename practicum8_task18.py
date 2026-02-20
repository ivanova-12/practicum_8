text = input()
size = int(input())
current_size = 0
s = ''
new_text = []
for word in text.split():
    if s:
        potential_length = current_size + 1 + len(word)
    else:
        potential_length = len(word)

    if potential_length <= size:
        if s:
            s += ' ' + word
            current_size += 1 + len(word)
        else:
            s = word
            current_size = len(word)
    else:
        if s:
            new_text.append(s)
        s = word
        current_size = len(word)
if s:
    new_text.append(s)
for strings in new_text:
    if len(strings) < size and ' ' in strings:
        strings = strings.replace(' ', (size - len(strings)) // strings.count(' ') * ' ')
    print(strings)




