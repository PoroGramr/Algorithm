n = int(input())

for k in range(n):
    count = 0
    s = int(input())  # 돌아가야 하는 학생수
    move = [list(map(int, input().split())) for _ in range(s)]
    
    # 각 이동 경로를 복도 구간으로 변환
    corridor = [0] * 201  # 복도는 1번부터 200번까지
    
    for i in range(len(move)):
        move[i].sort()
        start = (move[i][0] + 1) // 2  # 출발하는 방의 복도 구간
        end = (move[i][1] + 1) // 2    # 도착하는 방의 복도 구간
        
        # 이동 구간에서 모든 복도 구간의 겹침을 기록
        for j in range(start, end + 1):
            corridor[j] += 1
    
    # 가장 많이 겹친 복도 구간을 찾음
    count = max(corridor)
    
    print(f"#{k+1} {count}")
