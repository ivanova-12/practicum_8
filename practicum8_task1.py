sentence = input()
cnt = 1
all_cnt = [1,]

for i in range(len(sentence) - 1):
    if sentence.count(' ') != 0:
        if sentence[i] == ' ' and sentence[i + 1] == ' ':
            cnt += 1
            all_cnt.append(cnt)
        elif sentence[i] != ' ':
            cnt = 1
    else:
        all_cnt = [0]

print(max(all_cnt))



