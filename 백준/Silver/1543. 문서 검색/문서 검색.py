word = input()
s = input()

cnt = 0
i = 0

while i <= len(word) - len(s):
    if word[i:i+len(s)] == s:
        cnt += 1
        i += len(s)   # 찾으면 길이만큼 점프
    else:
        i += 1

print(cnt)