def dfs(n, sm, add, sub, mul, div):
    global mn, mx

    if sm < int(-1e9) or int(1e9)<sm:
        return
    
     # 종료 조건
    if n == N:
        mn = min(mn, sm)
        mx = max(mx, sm)
        return
    
    # 하부 호출
    if add > 0:
        dfs(n+1, sm + data[n], add -1, sub,mul, div)
    if sub > 0:
        dfs(n+1, sm - data[n], add, sub - 1,mul, div)
    if mul > 0:
        dfs(n+1, sm * data[n], add, sub,mul-1, div)
    if div > 0:
        dfs(n+1, int(sm/data[n]), add, sub,mul, div-1)


N = int(input())

data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

mn, mx = int(1e9), int(-1e9)
# 연산은 a * b 이런식으로 진행되므로 인덱스가 1부터 시작
# 그래야 a 값을 바탕으로 다음 사칙연산을 할 수 있기 때문!
dfs(1,data[0],add, sub, mul, div)


print(mx)
print(mn)

