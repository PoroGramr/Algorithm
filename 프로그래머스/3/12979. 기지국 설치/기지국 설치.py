def solution(n, stations, w):
    cover = 2*w + 1
    ans = 0
    prev = 1  # 아직 커버되지 않은 구간의 시작 후보

    for s in sorted(stations):
        left = max(1, s - w)
        right = min(n, s + w)

        # prev ~ left-1 까지가 빈 구간
        if prev < left:
            length = left - prev
            ans += (length + cover - 1) // cover  # 정수 올림
        prev = right + 1  # 다음 빈 구간 시작 후보

    # 마지막 기지국 이후의 꼬리 구간
    if prev <= n:
        length = n - prev + 1
        ans += (length + cover - 1) // cover

    return ans
