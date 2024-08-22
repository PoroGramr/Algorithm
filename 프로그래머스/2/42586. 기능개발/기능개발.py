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
    
    # 입력받은 2개의 리스트를 큐로 변환
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    # progresses가 empty가 되버리면 중단
    while progresses:
        for update in range(len(progresses)):
            
            # speeds값만큼 progresses를 업데이트
            progresses[update] += speeds[update]
            
            # 만약 100을 넘기면 100으로 고정
            if progresses[update] > 100:
                progresses[update] = 100
            
        # 배포 기능 계산용 변수 선언
        cnt = 0
        
        # progresses가 비워져있지 않고 첫번째 요소가 100일때
        while progresses and progresses[0] == 100 :
            progresses.popleft()
            speeds.popleft()
            cnt += 1
        
        # cnt가 1 이상일때만 answer에 append
        if cnt > 0: 
            answer.append(cnt)
        
    return answer
    
            
        
