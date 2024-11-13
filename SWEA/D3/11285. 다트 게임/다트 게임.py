import  math
T = int(input())
ans = []

for t in range(T):
    N = int(input())
    score= 0  # 라운드 마다의 총점
    for n in range(N):
        x, y = map(int, input().split())
        r = math.ceil(math.sqrt(x * x + y * y) / 20)
        if r <= 0:
            score += 10
        elif r <= 11:
            score += 11 - r
    ans.append(f"#{t + 1} {score}")

for x in ans:
    print(x)