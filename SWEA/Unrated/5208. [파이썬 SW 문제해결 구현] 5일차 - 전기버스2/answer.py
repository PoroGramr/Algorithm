def dfs(n, cnt, sm):
    global ans
    if ans<=cnt:
        return
 
    if n==N:
        ans = min(ans, cnt)
        return
 
    # 가지치기를 고려하는 겨우: 유망한 답이 먼저 나오는 방향으로 호출
    if sm>0:                    # 교체하지 않는 경우
        dfs(n+1, cnt, sm-1)
    dfs(n+1, cnt+1, lst[n]-1)   # 교체하는 경우
 
T = int(input())
for test_case in range(1, T + 1):
    lst = list(map(int, input().split()))
    N = lst[0]
    ans = N     # 모든 정류장에서 교체할경우 N
 
    dfs(2, 0, lst[1]-1) # 1번 정류장에서는 교체회수X, 2번부터 진행
    print(f'#{test_case} {ans}')
