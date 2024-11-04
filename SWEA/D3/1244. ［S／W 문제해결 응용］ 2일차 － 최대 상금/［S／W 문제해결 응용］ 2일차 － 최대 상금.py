"""
제시된 횟수만큼 숫자들을 변경한 뒤
최댓값을 출력

"""

def dfs(n):
    global ans
    if n == c:

        # 문자열을 정수로 변환해 최대값을 찾아냄
        snum = ""
        for s in num:
            snum += s
        snum = int(snum)

        ans = max(ans, snum)
        return

    for i in range(0,len(num) - 1):
        for j in range(i+1, len(num)):

            # 2개의 숫자의 위치를 교환
            num[i], num[j] = num[j],num[i]

            # 방문 처리 검사흘 위해선 리스트로 검사가 불가하기에 리스트를 문자열로 변환 후 검사
            state = "".join(num)
            if (n, state) not in v:
                dfs(n+1)
                v.append((n, state))

            # 위치 교환한 2개의 숫자를 다시 원래 위치로 변환
            num[i],num[j] = num[j],num[i]



T  = int(input())
for t in range(1, T+1):
    num, c = map(int, input().split())
    # 입력된 정수를 문자 리스트로 변환
    num  = list(str(num))

    ans = 0

    # 방문 처리를 위한 리스트
    v = []

    # dfs를 활용한 탐색
    dfs(0)

    print(f"#{t} {ans}")