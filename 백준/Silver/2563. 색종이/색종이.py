"""
아이디어

100 * 100 도화지 배열을 생성함
모두 0 으로 채운다

그 후 색종이의 좌표를 받음
1번 좌표 a는 왼쪽 틈, 2번 좌표 b는 아래 틈이다
이걸 바탕으로 색종이의 크기 만큼 도화지 배열을 1로 바꿈
색종이 크기만큼 도화지 채우기
가잔 왼쪽 상단 좌표를 찾아야한다.
a는 그대로 b+10하면 왼쪽 상단 좌표
for y in range(b+10, b, -1)
    for x in range(a, a + 10):
        data[y][x] = 1

for y in range(100):
    for x in range(100):
        if data[y][x] == 1:
            count += 1
"""
white = [[0] * 100 for _ in range(100)]
N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    
    # 색종이의 부분들을 1로 채움
    # -> 넓이를 구하기 위한 과정
    for y in range(b, b + 10):
        for x in range(a, a + 10):
            white[y][x] = 1

count = 0

# 1로 채워진 부분들을 구함 -> 넓이
for y in range(100):
    for x in range(100):
        if white[y][x] == 1:
            count += 1

print(count)