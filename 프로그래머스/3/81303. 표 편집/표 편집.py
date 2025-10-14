def solution(n, k, cmds):
    # 양방향 연결(인덱스 기반 링크드 리스트)
    prev = [i - 1 for i in range(n)]
    next = [i + 1 for i in range(n)]
    next[-1] = -1  # 마지막의 next는 없음

    stack = []  # (삭제행, prev, next)

    for cmd in cmds:
        parts = cmd.split()
        c = parts[0]

        if c == "U":
            x = int(parts[1])
            for _ in range(x):
                k = prev[k]
        elif c == "D":
            x = int(parts[1])
            for _ in range(x):
                k = next[k]
        elif c == "C":
            stack.append((k, prev[k], next[k]))
            # 이웃 링크 재연결
            if prev[k] != -1:
                next[prev[k]] = next[k]
            if next[k] != -1:
                prev[next[k]] = prev[k]
            # 커서 이동 규칙
            k = prev[k] if next[k] == -1 else next[k]
        elif c == "Z":
            idx, p, nx = stack.pop()   # 변수 충돌 방지
            # 이웃에서 나를 다시 가리키게
            if p != -1:
                next[p] = idx
            if nx != -1:
                prev[nx] = idx
            # 내 prev/next도 복원
            prev[idx] = p
            next[idx] = nx

    # 결과 문자열 생성
    answer = ['O'] * n
    for idx, _, _ in stack:  # 남아있는 건 복구되지 않은 삭제행
        answer[idx] = 'X'
    return ''.join(answer)
