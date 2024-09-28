from collections import deque

def bfs():
    q = deque()
    v = [[[0] * M for _ in range(N)] for _ in range(H)]
    
    cnt = 0                     # 안익은 토마토 수 카운트
    for h in range(H):
        for n in range(N):
            for m in range(M):
                
                # 안익은 토마토 라면
                if data[h][n][m] == 0:
                    cnt += 1
                
                # 익은 토마토 라면
                elif data[h][n][m] == 1:
                    q.append((h,n,m))
                    v[h][n][m] = 1
    
    while q:
        (ch,cn,cm) = q.popleft()
        for (ph,pn,pm) in ((-1,0,0),(1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)):
            nh, nn, nm = ch + ph, cn + pn, cm +pm
            if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M and data[nh][nn][nm] == 0 and v[nh][nn][nm] == 0:
                q.append((nh,nn,nm))
                v[nh][nn][nm] = v[ch][cn][cm] + 1
                cnt -= 1
    if cnt == 0:
        return v[ch][cn][cm] - 1
    else:
        return -1


M,N,H = map(int, input().split()) # 가로, 세로, 높이
data = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
ans = bfs()
print(ans)
