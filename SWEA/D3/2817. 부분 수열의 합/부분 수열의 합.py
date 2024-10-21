def check(i,n):
    global ans
    # 더 이상 체크할 인덱스가 없으면 종료
    if i == len(data):
        # 부분수열의 합이 K와 같은지 확인
        if n == K:
            ans += 1
        return

    if i + 1 <= len(data):
        check(i+1, n+data[i])

        check(i + 1, n)
    



T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    data = list(map(int, input().split()))

    ans = 0 
    check(0,0)  # index, sum
    print(f"#{t} {ans}")