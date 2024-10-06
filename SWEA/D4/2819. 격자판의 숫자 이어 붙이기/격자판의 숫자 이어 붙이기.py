def dfs(n, num, y, x):

    # num이 정수이기에 7개의 숫자를 이용해 만들었어도 7자리가 아닌것처럼 보임
    # ex 0_111_111 -> 111_111이지만 실제로는 7개의 숫자를 이어붙인결과임
    # 따라서 n을 이용하여 숫자가 현재까지 몇개가 붙여진건지 표현
    if n == CNT:
        sset.add(num)
        return

    for py, px in ((0,1), (0,-1), (1,0), (-1,0)):
        ny , nx = y + py, x + px

        # 문자열로 치면 숫자는 계속해서 1의 자리 부분에 붙으므로 (기존 숫자 * 10 + 다음숫자) => 정수(문자열) 이런식으로 진행됌
        if 0 <= ny < N and 0 <=nx < N:
            dfs(n+1, num*10 + data[ny][nx], ny, nx)


T = int(input())

for i in range(1, T+1):
    N , CNT = 4, 7
    data = [list(map(int, input().split())) for _ in range(N)]

    sset  = set()

    # 가능한 모든 위치 순회

    for y in range(N):
        for x in range(N):
            dfs(1, data[y][x], y, x)
    print(f"#{i} {len(sset)}")

