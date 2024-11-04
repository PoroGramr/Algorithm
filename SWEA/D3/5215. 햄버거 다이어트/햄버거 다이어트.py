# import sys
# sys.setrecursionlimit(10**6)  # 재귀 제한을 1,000,000으로 설정

def dfs(i, score, cal): # 인덱스, 점수, 칼로리
    global ans
    
    # 모든 요소를 다 탐색했을 때
    if i == M:
        
        # 제한 칼로리를 넘지 않았다면
        if cal <= L:
            ans = max(ans, score)
        return

    # 해당 인덱스의 재료를 추가하는 경우
    dfs(i+1, score+data[i][0], cal + data[i][1])
    
    # 해당 인덱스의 재료를 추가하지 않는 경우
    dfs(i+1, score, cal)

    return


T = int(input())

for t in range(1, T+1):
    N, L = map(int, input().split()) # 재료의 수, 제한 칼로리
    data = []


    for _ in range(N):
        score, cal  = map(int, input().split()) # 점수, 칼로리를 리스트에 삽입
        data.append([score, cal])
    
    # 데이터의 길이를 변수로 저장
    M = len(data)

    ans = 0
    
    # 탐색
    dfs(0,0,0) # 인덱스, 점수, 칼로리

    print(f"#{t} {ans}")