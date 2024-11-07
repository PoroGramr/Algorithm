"""
문제 이해
    덩치는 (x,y) 로 표현 된다. x는 키 y는 몸무게 이다
    a 가 b 보다 둘 다 값이 크다면 a의 덩치가 b보다 더 크다고 한다.
    키와 몸무게 중 하나만 값이 크다면 덩치가 크다고 할 수없다.

    n명의 집단에서 각 사람의 덩치 등수는 자신보다 더 큰 덩치의 사람의 수로 정해진다.
    만일 자신보다 더 큰 덩치의 사람이 k 명이라면 그 사람의 덩치 등수는 k+1이 된다.
    이렇게 등수를 결정하면 같은 덩치 등수를 가진 사람은 여러명도 가능하다.
    - 입력
        전체 사람의 수 n
        몸무게와 키 x,y 가 n 번 반복되서 입력 된다.
    - 출력
    입력된 순서대로 각 사람의 덩치 등수를 공백문자로 분리해서 출력

아이디어
    일단 몸무게도 크고, 키도 커야 덩치가 크다고 할 수 있다.
    그냥 탐색?
    그러면 그냥
    자기보다 덩치 큰 사람의 수 ?

"""
N = int(input())
data = []

for _ in range(N):
    cm, kg = map(int, input().split())

    data.append([cm, kg])

ans = []

for i in range(N):
    count = 0
    for j in range(N):
        if i == j:
            continue
        elif data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            count += 1
    ans.append(count+1)
print(*ans)



