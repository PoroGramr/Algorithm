def dfs(i,sm,cnt):
    global sums
    if i == 7:
        if cnt == 3:
            sums.add(sm)
        return

    # 해당 인덱스 숫자 고름
    dfs(i+1, sm + nums[i], cnt + 1)

    # 해당 인덱스 숫자 고르지 않음
    dfs(i+1, sm, cnt)


T = int(input())

for t in range(1, T + 1):
    nums = list(map(int, input().split()))

    # 중복값을 생기지 않게함
    sums = set()

    dfs(0,0,0) # 인덱스, 합, 선택한 숫자의 개수

    # 리스트로 바꿔 정렬함
    sums = list(sums)
    sums.sort(reverse=True)
    print(f"#{t} {sums[4]}")