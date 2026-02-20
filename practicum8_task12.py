import string
import keyword

s = input()
flag = False
if len(s) > 0:
    s_new = list(s.lower())
    flag = True
    if s.isdigit() or s_new[0].isdigit() or keyword.iskeyword(s):
        flag = False
    if any(((symbol != '_') and (symbol not in string.ascii_letters)
                            and (symbol not in string.digits))
                            for symbol in s_new):
        flag = False
if flag:
    print('может быть именем в Python')
else:
    print('не может быть именем в Python')

