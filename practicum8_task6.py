s_new = list(input().lower().split())[::-1]
if not s_new[0].isalpha():
    s_end = (s_new[0])[-1]
    s_new[0] = (s_new[0])[:-1]

s_new_end = ''
for x in s_new:
    s_new_end = s_new_end + ' ' + x
print(s_new_end.strip().capitalize() + s_end)








