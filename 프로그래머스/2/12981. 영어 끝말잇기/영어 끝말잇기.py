
"""
N 명의 사람들이 순서대로 끝말잇기를 진행할 때
누가 탈락하는지, 몇번쨰 순서에 탈락하는지 리턴하시오
단어 배열의 길이는 100 이하
정답은 [번호, 차례]


["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
0           1       2       3       4       5           6       7        8

"""

def solution(n, words):
    answer=[]
    wordLen = len(words)
    seen = set([words[0]])
    
    for i in range(1,wordLen):
        if words[i] in seen:
            print("단어 중복!")
            humanNum = i % n + 1
            cntNum = i // n + 1
            answer.append(humanNum)
            answer.append(cntNum)
            break
        
        elif words[i-1][-1] != words[i][0]:
            print("끝말 불일치!")
            humanNum = i % n + 1
            cntNum = i // n + 1
            answer.append(humanNum)
            answer.append(cntNum)
            break
        
        else:
            seen.add(words[i])
        
    
    
    if len(answer) == 0:
        answer = [0,0]
    
    return answer