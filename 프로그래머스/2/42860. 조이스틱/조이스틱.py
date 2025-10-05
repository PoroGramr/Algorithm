def solution(name):
    answer = 0
    n = len(name)
    
    # 1) 상하 이동 합
    for ch in name:
        up = ord(ch) - ord('A')
        down = ord('Z') - ord(ch) + 1
        answer += min(up, down)
    
    # 2) 좌우 이동 최솟값
    move = n - 1
    for i in range(n):
        j = i + 1
        # 연속된 'A' 구간 스킵
        while j < n and name[j] == 'A':
            j += 1
        # i까지 갔다가 뒤로 꺾는 경우 vs 끝까지 가는 경우 비교
        move = min(move, i + n - j + min(i, n - j))
    
    answer += move
    return answer
