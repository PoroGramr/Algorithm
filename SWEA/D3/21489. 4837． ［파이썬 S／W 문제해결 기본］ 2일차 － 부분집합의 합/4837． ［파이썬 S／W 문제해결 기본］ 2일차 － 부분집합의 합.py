def dfs(ind, n,sm): # ind : 리스트 인덱스 , n : 원소의 수, k : 합
    global answer
    if ind == 12:
        if n == N and sm == K:
            answer += 1
        return
    
    # 더하는 경유
    dfs(ind+1, n + 1, sm + data[ind])

    # 더하지 않는 경우
    dfs(ind+1, n, sm)


T = int(input())

for i in range(1,T+1):
    N, K = map(int, input().split()) # N : 원소의 수 , K : 부분 집합의 합
    data = [n for n in range(1,13)]

    answer = 0
    dfs(0,0,0)

    print(f"#{i} {answer}")
