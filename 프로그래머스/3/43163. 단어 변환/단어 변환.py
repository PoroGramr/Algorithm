from collections import deque

def dfs(cw, target, words,cnt):
    global v,answer
    if cw == target:
        answer = cnt - 1
        return 
    
    for i in range(len(words)):
        # 아직 변환한 단어가 아닐 경우에만
        if v[i] == 0:
            
            # words에서 문자가 1개만 다른경우인 문자 찾기
            difCnt = 0
            for j in range(len(cw)):
                
                # 현재 단어와 words의 단어의 같은 인덱스 문자를 확인
                if cw[j] != words[i][j]: 
                    difCnt += 1
            
            # 한글자만 다를 경우
            if difCnt == 1:
                v[i] = cnt+1
                dfs(words[i], target, words, cnt + 1)
                v[i] = 0
                
            
            

def solution(begin, target, words):
    global v,answer
    v = [0] * len(words)
    answer = 0
    dfs(begin, target, words,1)
    return answer