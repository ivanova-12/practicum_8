sentence = input()
cnt = 1
all_cnt = [0,]
flag = False

for i in range(len(sentence) - 1):
        if sentence[i] == sentence[i + 1]:
            cnt += 1
            all_cnt.append(cnt)
            flag = True
        elif sentence[i] != sentence[i + 1]:
            cnt = 1
            all_cnt.append(cnt)

if flag:
    print(max(all_cnt))
else:
    print(0)





