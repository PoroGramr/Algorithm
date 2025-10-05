def solution(name):
    # 1. 상하 이동 계산
    answer = 0
    for ch in name:
        diff = ord(ch) - ord('A')
        answer += min(diff, 26 - diff)

    # 2. 좌우 이동 계산
    move = len(name) - 1  # 기본: 끝까지 오른쪽 이동
    for i in range(len(name)):
        next_idx = i + 1
        # 연속된 A 건너뛰기
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1
        # 이동 최소화: i에서 돌아가거나 건너뛰는 경우 고려
        move = min(move, 2 * i + len(name) - next_idx, i + 2 * (len(name) - next_idx))

    answer += move
    return answer
