S = input()

# 문자를 뒤집는 과정
reS = ""

# 괄호가 있으면 그대로 삽입위한 임시 저장소
noRes = ""
flag = False
# 정답 출력용 리스트
answer = []
for c in S:
    if flag:
        if c != ">":
            noRes += c
        else:
            noRes += ">"
            answer.append(noRes)
            noRes = ""
            flag = False
        
    else:
        if c == " ":
            if reS != "":
                answer.append(reS)
                answer.append(" ")
                reS = ""
        
        elif c == "<":
            if reS != "":
                answer.append(reS)
                reS = ""
            noRes +="<"
            flag = True
        
        else:
            c = c+reS
            reS = c

if reS != "":
    answer.append(reS)


result = ""
for p in answer:
    result += p

print(result)


