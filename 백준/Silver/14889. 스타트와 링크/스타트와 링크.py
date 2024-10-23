def dfs(i, alst, blst):
    global ans
    if i == N:
        if len(alst) == M:
            asum = bsum = 0
            for i in range(M):
                for j in range(M):
                    asum += data[alst[i]][alst[j]]
                    bsum += data[blst[i]][blst[j]]
            ans = min(ans, abs(asum - bsum))

        return
    # 스타트 팀에 팀원이 합류하는 경우
    dfs(i+1, alst+[i], blst)

    # 링크 팀에 팀원이 합류하는 경우
    dfs(i+1, alst, blst+[i])    


N = int(input())

# 절반으로 나눠지기 떄문에 추후 계산의 편의를 위해 정의
M = N // 2

# 능력치 데이터
data = []

for _ in range(N):
    data.append(list(map(int, input().split())))

# 최대값으로 설정
ans = float("inf")

dfs(0,[],[]) # index, 스타트팀 팀원, 링크팀 팀원

print(ans)
