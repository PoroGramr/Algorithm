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
for i in range(1,11):
    d = int(input())
    data  = list(map(int, input().split()))
    m = len(data)
    for k in range(d):
        bigV = max(data)
        smallV = min(data)
        
        bigIndex = 0
        smallIndex = 0
        for fb in range(m):
            if data[fb] == bigV:
                bigIndex = fb
        for fs in range(m):
            if data[fs] == smallV:
                smallIndex = fs
        data[smallIndex] += 1
        data[bigIndex] -= 1
    answer = max(data) - min(data)
    print(f"#{i} {answer}")
            
        
       