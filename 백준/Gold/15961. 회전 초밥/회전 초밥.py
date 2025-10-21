"""
1. 벨트의 임의의 한 위치부터 K개의 접시를 연속해서 먹을 경우 할이낙격
2. 각 고객에게 초밥의 종류 하나가 쓰인 쿠폰을 발행, 1번 행사에 참여했을 경우 초밥 하나를 무료로 제공,
만약 해당 초밥이 벨트에 없다면 새로 만들어 제공


"""
#  접시의 수 N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
n, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(n)]

count = [0] * (d + 1)
unique = 0

count[c] += 1
unique += 1

for i in range(k):
    if count[belt[i]] == 0:
        unique += 1
    count[belt[i]] += 1

answer = unique

for i in range(1, n):
    left = belt[i - 1]
    count[left] -= 1
    if count[left] == 0:
        unique -= 1
    
    right = belt[(i +k - 1) % n]
    if count[right] == 0:
        unique += 1
    count[right] += 1
    
    if unique > answer:
        answer = unique
    
    
print(answer)



