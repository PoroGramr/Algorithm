"""
"""

from collections import deque 
def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)

    answer = []

    # 100 프로가 넘는 것들끼리 다시 카운팅
    
    while(len(progresses) != 0):
        # 하루씩 진행률 업데이트
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        currentComplete = 0
        
        # 큐의 헤드가 100이 넘는지 확인
        for j in range(len(progresses)):
            currentProgress = progresses[0]
            
            if currentProgress >= 100:
                currentComplete += 1
                progresses.popleft()
                speeds.popleft()
            else:
                break
        
        # 해당 날짜에 완성된 작업들 카운트
        if currentComplete > 0:
            answer.append(currentComplete)
        
    return answer
    
            
        
