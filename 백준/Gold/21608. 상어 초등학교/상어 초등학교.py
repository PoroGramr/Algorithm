N = int(input())
# 자리를 정하게 될 번호 순서
students = []
# 자리 정하는 번호순서대로 해당 학생이 좋아하는 학생 리스트
loves = []

# 번호에 맞는 자리를 저장할 리스트
# 인덱스 계산을 편하게 하기 위해 N + 1로 리스트를 생성
M = N + 1
sits = [[0] * (M) for _ in range(M)]

# 입력에 따른 리스트 업데이트
for _ in range(N ** 2):
    lst = list(map(int, input().split()))
    stu = lst[0]
    lov = lst[1::]

    students.append(stu)
    loves.append(lov)

# 1. 자리 배치
for i in range(len(students)):
    # 1-1. 비어있는 칸 중 좋아하는 학생이 인접한 칸에 가장 많은 칸
    cond1 = []

    # 근처에 좋아하는 학생이 몇명 있는지
    lovecount = 0
    for y in range(1,M):
        for x in range(1,M):
            if sits[y][x] == 0:
                # 해당 자리 근처 좋아하는 친구 수 가운트
                currentLove = 0
                for py, px in ((-1,0), (1,0),(0,-1),(0,1)):
                    ny, nx = y + py, x + px
                    if 1 <= ny < M and 1<= nx < M:
                        if sits[ny][nx] in loves[i]:
                            currentLove += 1

                # 주위에 좋아하는 친구 명수가 같다면 그 좌표를 추가
                if currentLove == lovecount:
                    cond1.append((y,x))

                # 주위에 좋아하는 친구 명수가 더 많다면 기존의 리스트를 초기화하고
                # 새로 업데이트
                elif currentLove > lovecount:
                    lovecount = currentLove
                    cond1 = [[y,x]]
    # 1번 조건에 해당하는 자리가 1개 라면
    if len(cond1) == 1:
        cy, cx = cond1[0]
        sits[cy][cx] = students[i]
        continue

    # 1-2 : 1-1 조건 결과가 여러개일떼, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸
    else:
        # 비어있는 칸이 가장 많은 칸 저장 리스트
        cond2 = []

        # 지금까지의 주위에 빈칸이 가장 많은 경우의 주위 빈칸의수
        emptyCount = 0
        for cy, cx in cond1:
            # 현재 반복문에서의 주위 빈칸의 수
            curEmpty = 0

            # 인접한칸 빈자리 수 카운트
            for py, px in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ny, nx = cy + py, cx + px
                if 1 <= ny < M and 1 <= nx < M:
                    if sits[ny][nx] == 0:
                        curEmpty += 1

            # 주위 빈 자리의 수가 현재 최대 빈자리 수와 같다면
            if emptyCount == curEmpty:
                cond2.append([cy,cx])

            # 주위 빈자리수가 최대치라면
            elif emptyCount < curEmpty:
                emptyCount = curEmpty
                cond2 = [[cy,cx]]

        # 1-2 조건 만족시
        if len(cond2) == 1:
            cy, cx = cond2[0]
            sits[cy][cx] = students[i]
            continue

        # 1-3 : 1-2결과가 여러개일 경우, 행의 번호가 가장 작은칸
        # -> 열의 번호가 가장 작은칸
        else:
            cond2.sort(key = lambda x :(x[0], x[1]))
            cy, cx = cond2[0]
            sits[cy][cx] = students[i]
            continue


# 2. 점수 계산
score = 0
for j in range(len(students)):
    for ly in range(1, M):
        for lx in range(1, M):

            if sits[ly][lx] == students[j]:
                near = 0
                for py, px in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ny, nx = ly + py, lx + px
                    if 1 <= ny < M and 1 <= nx < M:
                        if sits[ny][nx] in loves[j]:
                            near +=1

                if near == 1:
                    score += 1
                elif near == 2:
                    score += 10
                elif near == 3:
                    score += 100
                elif near == 4:
                    score += 1000

print(score)


















