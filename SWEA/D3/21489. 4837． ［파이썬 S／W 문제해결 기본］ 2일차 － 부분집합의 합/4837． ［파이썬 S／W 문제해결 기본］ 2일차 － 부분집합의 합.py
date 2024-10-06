
def dfs(n ,sm, cnt):
    global ans

    # 종료 조건: n에 관련된 수식
    if n == N:
        if sm == K and cnt == CNT:
            ans += 1
        return

    # 숫자를 사용하는 경우
    dfs(n+1, sm + data[n], cnt + 1)
    # 사용하지 않는 경우
    dfs(n+1, sm, cnt)
    
T = int(input())



for i in range(1, T + 1):
    CNT , K = map(int, input().split())
    data = [n for n in range(1,13)]
    N = 12

    ans = 0
    dfs(0, 0, 0)

    print(f"#{i} {ans}")