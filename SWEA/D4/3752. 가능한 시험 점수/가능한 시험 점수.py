def possible_scores(scores):
    possible = {0}  # 0점은 항상 가능하므로 초기화
    for score in scores:
        new_scores = set()
        for s in possible:
            new_scores.add(s + score)
        possible.update(new_scores)  # 기존 가능한 점수들과 새로운 점수를 합침
    return len(possible)


# 테스트 케이스 입력 받기
T = int(input())  # 테스트 케이스 수

for tc in range(1, T + 1):
    N = int(input())  # 문제 수
    scores = list(map(int, input().split()))  # 각 문제의 점수
    result = possible_scores(scores)
    print(f"#{tc} {result}")
