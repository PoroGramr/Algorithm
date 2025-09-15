def solution(board, skill):
    N = len(board)
    M = len(board[0])

    # 1) (N+1) x (M+1) 차분배열
    diff = [[0]*(M+1) for _ in range(N+1)]

    # 2) 네 꼭짓점 마킹 (공격: -degree, 회복: +degree)
    for t, r1, c1, r2, c2, degree in skill:
        if t == 1:
            v = -degree
        else:
            v = degree
        diff[r1][c1]       += v
        diff[r1][c2+1]     -= v
        diff[r2+1][c1]     -= v
        diff[r2+1][c2+1]   += v

    # 3) 행 누적 → 열 누적
    # 행 방향
    for r in range(N):
        run = 0
        for c in range(M):
            run += diff[r][c]
            diff[r][c] = run
    # 열 방향
    for c in range(M):
        run = 0
        for r in range(N):
            run += diff[r][c]
            diff[r][c] = run

    # 4) 양수 카운트
    answer = 0
    for r in range(N):
        for c in range(M):
            if board[r][c] + diff[r][c] > 0:
                answer += 1
    return answer
