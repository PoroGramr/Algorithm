def dfs(index, current_score, current_calories):
    global max_score

    # 칼로리 제한을 넘으면 더 이상 진행하지 않음
    if current_calories > calorie_limit:
        return

    # 현재까지 얻은 점수로 최대 점수를 갱신
    max_score = max(max_score, current_score)

    # 모든 재료를 확인했으면 종료
    if index == n:
        return

    # 현재 재료를 선택하는 경우
    dfs(index + 1, current_score + ingredients[index][0], current_calories + ingredients[index][1])

    # 현재 재료를 선택하지 않는 경우
    dfs(index + 1, current_score, current_calories)

# 테스트 케이스 수
T = int(input())

for test_case in range(1, T + 1):
    # 재료 수와 칼로리 제한 입력
    n, calorie_limit = map(int, input().split())

    # 재료 정보 입력 (점수, 칼로리)
    ingredients = [tuple(map(int, input().split())) for _ in range(n)]

    # 최대 점수를 저장할 변수
    max_score = 0

    # 백트래킹을 통해 탐색 시작
    dfs(0, 0, 0)

    # 결과 출력
    print(f'#{test_case} {max_score}')
