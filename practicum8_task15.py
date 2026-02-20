number = input()

for cnt in range(25):
    print('')

flag = False
for cnt in range(10):
    num = input()
    bulls = 0
    cows = 0
    if len(set(number) & set(num)) > 0:
        for index1 in range(4):
            if number[index1] == num[index1]:
                bulls += 1
            elif num[index1] in number and number[index1] != num[index1]:
                cows += 1
        print(f'Быков: {bulls}, Коров: {cows}')
        if bulls == 4:
            flag = True
            break
if flag:
    print('Победа!')
else:
    print('Проигрыш!')







