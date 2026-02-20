str1 = set(list(input()))
str2 = set(list(input()))
str3 = set(list(input()))
end_of_program1 = []
end_of_program2 = []
end_of_program3 = []
for symbol in str1:
    if symbol not in str2 and symbol not in str3:
        end_of_program1.append(symbol)
for symbol in str2:
    if symbol not in str1 and symbol not in str3:
        end_of_program2.append(symbol)
for symbol in str3:
    if symbol not in str1 and symbol not in str2:
        end_of_program3.append(symbol)

print('Уникальные элементы строки 1:', *end_of_program1)
print('Уникальные элементы строки 2:', *end_of_program2)
print('Уникальные элементы строки 3:', *end_of_program3)







