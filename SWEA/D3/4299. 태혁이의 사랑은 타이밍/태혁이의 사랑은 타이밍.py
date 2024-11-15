T = int(input())

for t in range(1, T + 1):
    D, H, M = map(int, input().split())

    # 11일 11시 11분
    bDays = 11*24*60 + 11*60 + 11

    sadDays = D * 24*60 + H * 60 + M

    ans = sadDays - bDays

    if ans >=0:
        print(f"#{t} {ans}")
    else:
        print(f"#{t} -1")

