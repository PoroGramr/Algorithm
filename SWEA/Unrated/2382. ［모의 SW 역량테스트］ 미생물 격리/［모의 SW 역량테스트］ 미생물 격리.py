T = int(input())

for t in range(1, T + 1):
    N, M, K = map(int, input().split())  # 정사각형 셀의 가로세로 N, M시간 후 남아있는 미생물의 수, K개의 군집
    
    # 미생물들의 정보 리스트
    microbes = [] 
    for _ in range(K):
        microbes.append(list(map(int, input().split())))  # 세로위치, 가로위치, 미생물 수, 이동방향
    
    # 약품이 칠해진 구역 좌표 리스트
    medic = set()
    for a in range(N):
        medic.add((0, a))
        medic.add((N - 1, a))
    for b in range(1, N - 1):
        medic.add((b, 0))
        medic.add((b, N - 1))
    
    # M 시간동안 미생물들의 변화 계산
    for _ in range(M):
        count = [[0] * N for _ in range(N)]
        check = [[[] for _ in range(N)] for _ in range(N)]

        # 각 미생물 군집의 이동 처리
        for i in range(len(microbes)):
            microbe = microbes[i]
            y, x, amount, direction = microbe

            # 이동방향에 따라 다음 위치 계산
            if direction == 1:  # 상
                ny, nx = y - 1, x
            elif direction == 2:  # 하
                ny, nx = y + 1, x
            elif direction == 3:  # 좌
                ny, nx = y, x - 1
            elif direction == 4:  # 우
                ny, nx = y, x + 1

            # 다음 위치로 업데이트
            microbes[i][0], microbes[i][1] = ny, nx
            check[ny][nx].append(i)

            # 약품 구역인 경우 미생물 수 절반 감소 및 방향 반전
            if (ny, nx) in medic:
                microbes[i][2] //= 2
                if microbes[i][2] == 0:
                    microbes[i] = None  # 미생물이 0이 되면 제거 표시
                else:
                    # 방향 반전
                    if direction == 1:
                        microbes[i][3] = 2
                    elif direction == 2:
                        microbes[i][3] = 1
                    elif direction == 3:
                        microbes[i][3] = 4
                    elif direction == 4:
                        microbes[i][3] = 3

        # 미생물 군집 병합 처리
        for y in range(N):
            for x in range(N):
                if len(check[y][x]) > 1:  # 같은 위치에 2개 이상의 군집이 있는 경우
                    total_microbes = sum(microbes[i][2] for i in check[y][x] if microbes[i])
                    max_microbe = max(check[y][x], key=lambda i: microbes[i][2])
                    new_direction = microbes[max_microbe][3]

                    # 최대 미생물 수 군집을 유지하면서 나머지 군집을 병합
                    microbes[max_microbe][2] = total_microbes
                    microbes[max_microbe][3] = new_direction
                    for i in check[y][x]:
                        if i != max_microbe:
                            microbes[i] = None  # 병합된 군집은 제거 표시

        # 제거 표시된 미생물 군집 삭제
        microbes = [microbe for microbe in microbes if microbe]

    # 남은 미생물 수 합산
    ans = sum(microbe[2] for microbe in microbes)
    print(f"#{t} {ans}")
