number = int(input())
units = [
         'один', 'два', 'три',
         'четыре', 'пять' , 'шесть',
         'семь', 'восемь', 'девять'
         ]

fem_units = [
             'одна', 'две', 'три',
             'четыре', 'пять' , 'шесть',
             'семь', 'восемь', 'девять'
             ]

decades = [
           'десять','двадцать', 'тридцать',
           'сорок', 'пятьдесят',
           'шестьдесят', 'семьдесят',
           'восемьдесят', 'девяносто'
           ]
teens = [
         'одиннадцать', 'двенадцать', 'тринадцать',
         'четырнадцать','пятнадцать', 'шестнадцать',
         'семнадцать', 'восемнадцать', 'девятнадцать'
         ]
hundreds = [
            'сто', 'двести', 'триста',
            'четыреста', 'пятьсот', 'шестьсот',
            'семьсот', 'восемьсот', 'девятьсот'
           ]

result = ''
millions = number // 1000000
if millions > 0:
    if millions >= 100:
        result += hundreds[millions // 100 - 1] +  ' '
        millions = millions % 100
    if millions >= 20:
        result += decades[millions // 10 - 1] + ' '
        millions = millions % 10
    if millions >= 10:
        result += teens[millions - 10 - 1] + ' '
    elif millions > 0:
        result += units[millions - 1] + ' '


    if millions == 1:
        result += 'миллион '
    elif 2 <= millions <= 4:
        result += 'миллиона '
    else:
        result += 'миллионов '

thousands = (number // 1000) % 1000
if thousands > 0:
    if thousands >= 100:
        result += hundreds[thousands // 100 - 1] + ' '
        thousands = thousands % 100
    if thousands >= 20:
        result += decades[thousands // 10 - 1] + ' '
        thousands = thousands % 10
    if thousands >= 10:
        result += teens[thousands - 10 - 1] + ' '
    elif thousands > 0:
        result += fem_units[thousands - 1] + ' '

    if thousands == 1:
        result += 'тысяча '
    elif 2 <= thousands <= 4:
        result +='тысячи '
    else:
        result += 'тысяч '

number = number % 1000
if number > 0:
    if number >= 100:
        result += hundreds[number // 100 - 1] + ' '
        number = number % 100
    if number >= 20:
        result += decades[number // 10 - 1] + ' '
        number = number % 10
    if number >= 10:
        result += teens[number - 10 - 1] + ' '
    elif number > 0:
        result += units[number - 1] + ' '

print(result)
