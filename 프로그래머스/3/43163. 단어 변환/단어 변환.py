from collections import deque
def bfs(begin, target, words):
    v = [0] * len(words)
    q = deque()
    q.append((begin, 0))# count
    
    while q:
        cw, count = q.popleft() # 현재 단어와 지금까지의 카운트
        
        # 만역 현재 단어가 타겟과 같다면 카운트 리턴
        if cw == target:
            return count
        
        # words의 문자들을 하나하나 순회하며 검사
        for i in range(len(words)):
            
            # 만약 방문하지 않은 문자열이라면
            if v[i] == 0:
                
                # 같은 인덱스 문자가 몇개가 다른지 체크하는 변수
                difCount = 0
                
                # 현재 단어와 검사하는 문자열의 같은 인덱스 문자를 비교
                for j in range(len(cw)):
                    
                    # 같은 인덱스 문자가 다르다면 +1
                    if cw[j] != words[i][j]:
                        difCount += 1
                
                # 만약 현재 단어와 검사하는 문자열이 일치하지 않는 문자가 딱 1개라면
                if difCount == 1:
                    
                    # 큐에 삽입 후 방문 처리
                    q.append((words[i], count + 1))
                    v[i] = 1
    
    # 만약 모든 bfs가 끝나도 target과 일치하지 않는다면 0 리턴
    return 0
                
    

def solution(begin, target, words):
    answer = bfs(begin, target, words)
    return answer