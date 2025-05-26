def solution(elements):
    n = len(elements)
    # 1) 원형 수열 처리를 위해 두 번 붙이기
    circular = elements * 2

    # 2) 누적합(prefix sum) 계산 (길이 2n+1)
    prefix = [0] * (2*n + 1)
    for i in range(2*n):
        prefix[i+1] = prefix[i] + circular[i]

    # 3) 모든 길이 1~n, 모든 시작점 0~n-1에 대해 부분합 구하기
    sums = set()
    for length in range(1, n+1):          # 길이
        for start in range(0, n):         # 원본 위치에서만 시작
            end = start + length
            sums.add(prefix[end] - prefix[start])

    # 4) 서로 다른 합의 개수 반환
    return len(sums)
