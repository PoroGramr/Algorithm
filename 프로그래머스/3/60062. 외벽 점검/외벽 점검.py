from itertools import permutations

def solution(n, weak, dist):
    W = len(weak)
    # 원형을 선형으로 만들기 (두 번 이어붙임)
    extended = weak + [w + n for w in weak]

    answer = float('inf')

    # 시작 지점을 weak의 각 인덱스로 잡아본다
    for start in range(W):
        # 친구들 투입 순서의 모든 순열
        for friends in permutations(dist):
            used = 1  # 첫 번째 친구 사용
            # 첫 번째 친구가 커버할 수 있는 끝 지점
            cover_end = extended[start] + friends[used - 1]

            # start부터 start+W-1 까지의 취약 지점을 모두 살펴본다
            for idx in range(start, start + W):
                if extended[idx] > cover_end:
                    # 현재 친구로는 커버 불가 -> 다음 친구 투입
                    used += 1
                    if used > len(friends):  # 친구 다 썼으면 실패
                        break
                    cover_end = extended[idx] + friends[used - 1]

            else:
                # 모든 취약지점 커버 성공(브레이크 없이 완주)
                answer = min(answer, used)

    return -1 if answer == float('inf') else answer
