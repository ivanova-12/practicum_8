text = input()
brackets = 0
flag = True

for symbol in text:
    if symbol == '(':
        brackets += 1
    elif symbol == ')':
        brackets -= 1
        if brackets < 0:
            flag = False
            break
            
if flag and brackets == 0:
    print('правильно!')
else:
    print('неправильно!')









