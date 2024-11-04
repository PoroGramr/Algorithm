"""
- 입력
    - 덤프횟수 
    - 높이 리스트
- 출력
    최고점과 최저점의 높이 차이
- 아이디어
값이 큰 요소의 인덱스를 찾는다
가장 낮은 요소의 인덱스를 찾는다.
반복

마지막 계산
"""
for t in range(1, 11):
    # 덤프 횟수
    dump = int(input()) 
    
    # 세로 길이 정보 리스트
    data = list(map(int, input().split()))
    for _ in range(dump):
        minValue = min(data)
        maxValue = max(data)
        
        minIdx = 0
        maxIdx = 0
        for i in range(100):
            if data[i] == minValue:
                minIdx = i
            elif data[i] == maxValue:
                maxIdx = i
        
        data[minIdx] += 1
        data[maxIdx] -= 1
    
    ans = max(data) - min(data)
    
    print(f"#{t} {ans}")
            
    
    