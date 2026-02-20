def lucky_ticket(number):
    result = False
    if len(number) % 2 == 0:
        if (sum(int(n) for n in number[:(len(number)//2)]) == sum(int(n)
                        for n in number[len(number)//2:])):
            result = True
    return result

number = '0'
number_cnt = 0
while not lucky_ticket(number):
    number = input()
    if lucky_ticket(number):
        number_cnt += 1
        print(number_cnt)
        break
    else:
        number_cnt += 1


