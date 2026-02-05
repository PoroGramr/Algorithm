"""
이중 우선순위 큐는 전형적인 우선순위 큐처럼 데이터를 삽입, 삭제 할 수 이쓴ㄴ 자료 구조이다.
큐와의 차이점은 데이터를 삭제할 때 연산 명령에 따라 우선순위가 가장 높은 데이터 또는 가장 낮은 데이터중 하나를 삭제하는 것이다.

두가지 연산이 사용된다
하나는 데이터를 삽입하는 연산, 하나는 데이터를 삭제하는 연산
삭제하는 연산은 우선순위가 높은 것을 삭제하는 연산, 우선순위가 가장 낮은 것을 삭제하는 연산 으로 구분된다

I n 은 정수 n을 q에 삽입
D 1 은 최댓값을 삭제
D -1 는 최솟값을 삭제

만약 q가 비어있는데 적용할 연산이 'd'라면 무시가능

"""
import sys
import heapq

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    
    # 연산의 개수
    k = int(input())
    
    q = []
    maxh, minh = [], []
    visited = [False] * k
    
    for i in range(k):
        # 연산과 숫자 
        op, num = map(str, input().split())
        num = int(num)
        
        
        if op == 'I':
            heapq.heappush(maxh, (-num, i) )
            heapq.heappush(minh, (num, i))
            
        else:
            if num == 1:
                while maxh and visited[maxh[0][1]]:
                    heapq.heappop(maxh)
                
                if maxh:
                    visited[maxh[0][1]] = True
                    heapq.heappop(maxh)
                
            
            else:
                while minh and visited[minh[0][1]]:
                    heapq.heappop(minh)
                
                if minh:
                    visited[minh[0][1]] = True
                    heapq.heappop(minh)
    
    maxAnswer = float('inf')
    while maxh:
        tmp = heapq.heappop(maxh)
        if visited[tmp[1]] == False:
            maxAnswer = min(-tmp[0],maxAnswer)
            break
    
    minAnswer = float('inf')
    while minh:
        tmp = heapq.heappop(minh)
        if visited[tmp[1]] == False:
            minAnswer = min(tmp[0],minAnswer)
            break
        
    
    if maxAnswer == float('inf') or minAnswer == float('inf'):
        print("EMPTY")
    else:
        print(maxAnswer,minAnswer)