def solution(gems):
    kind = len(set(gems))           # 전체 보석 종류 수
    counts = {}                     # 윈도우 안 보석별 개수 저장
    answer = [0, len(gems) - 1]     # 최악의 구간 (0-based)
    left = 0

    for right, gem in enumerate(gems):
        # ① counts.get 키 인자를 제대로 gems[right]로 수정
        counts[gem] = counts.get(gem, 0) + 1

        # ② 모든 종류가 포함되면
        while len(counts) == kind:
            # 더 짧은 구간인지 확인
            if right - left < answer[1] - answer[0]:
                answer = [left, right]

            # left 보석 하나 제거
            counts[gems[left]] -= 1
            if counts[gems[left]] == 0:
                del counts[gems[left]]
            left += 1

    # 1-based 인덱스로 변환하여 반환
    return [answer[0] + 1, answer[1] + 1]
