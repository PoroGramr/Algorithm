"""

1번 : 2초 걸림 가장위 블록을 없애 인벤토리에
2번 : 1초 걸림 인벤토리에서 블록 하나 꺼내 채움 


최대한 빨리 땅 고르기 작업에 걸리는 최소 시간과 그 경우 땅의 높이



입력 n 세로 m 가로 b 인벤토리 블럭 수

"""



N,M,B = map(int, input().split())

data = []

daSet = set()

for i in range(N):
    data.append(list(map(int, input().split())))

for y in range(N):
    for x in range(M):
        daSet.add(data[y][x])


daSet = list(daSet)
answer = []
for d in range(257): 
    time = 0
    block = B
    for y in range(N):
        for x in range(M):
            if data[y][x] != d:
                
                if data[y][x] > d:
                    tmp = data[y][x] - d
                    time += 2 * tmp
                    block += tmp
                else:
                    tmp = d - data[y][x]
                    time += tmp 
                    block -= tmp
    
    
    if block >= 0:
        answer.append((time, d))

answer.sort(key = lambda x : (x[0], -x[1]))
print(*answer[0])


