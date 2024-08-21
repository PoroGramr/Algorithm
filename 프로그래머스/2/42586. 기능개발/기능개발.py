"""
문제 이해
- list 2개가 주어짐 현재 작업된 퍼센트 리스트, 
각 작업별 하루에 작업할 수 있는 퍼센트 리스트
- 각 작업은 독립적으로 진행되지만 배포는 선행된 작업이 완료되어야 배포할 수 있음 

- 입력 : 
    - progresses : 작업의 진도가 적힌 정수 리스트
    - speeds : 작업의 속도가 적힌 정수 리스트

- 출력:
    - 배포가 일어날 때 배포되는 기능의 수 리스트

아이디어
- 1기수마다 progresses의 현황을 업데이트 하기 (speeds 만큼)
- 배포 가능한 기능 배포하기 (queue)
    - 배포된 기능이 있다면 숫자세서 추가하기


제한사항
- n : 100 
"""

from collections import deque # queue를 사용하기 위해 import
def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    while progresses: # 모든 작업이 완료될 때 까지 반복
        # 작업상태 업데이트
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            if progresses[i] > 100:
                progresses[i] = 100
                
        # 배포된 기능 배포하기
        cnt = 0 
        
        while progresses and progresses[0] == 100: # peek
            progresses.popleft()
            speeds.popleft()
            cnt += 1
        
        if cnt > 0:
            answer.append(cnt)
        
    return answer