cities = input().lower().split()

for ind in range(len(cities)):
    if (cities[ind])[-1] == 'ь' or (cities[ind])[-1] == 'ъ':
        cities[ind] = (cities[ind])[:-1]


def right_game(cities):
    flag = True
    for ind in range(len(cities) - 1):
        if (cities[ind])[-1] == (cities[ind + 1])[0]:
            flag = True
        else:
            flag = False
            break
    return flag

def find_mistake(cities):
    res = 0
    for ind in range(len(cities) - 1):
        if (cities[ind])[-1] != (cities[ind + 1])[0]:
            res = ind
            break
    return res

if right_game(cities):
    if len(cities) % 2 == 0:
        print('Победил Вася')
    else:
        print('Победил Петя')
else:
    if find_mistake(cities) % 2 == 0:
        print('Победил Петя')
    else:
        print('Победил Вася')


