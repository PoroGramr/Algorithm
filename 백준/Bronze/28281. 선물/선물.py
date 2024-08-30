"""
아이디어
- 입력 : N일 뒤 생일인 정수 N , 사려는 양말의 개수 2X 의 X
      : N 일간 양말의 가격 리스트 [ 1, 2, 3, ...]
남은 N 일 가운데 연속한 2일에 걸쳐 양말 2X개를 사는 데 드는 최소 비용은?

data = [] 리스트를 선언한 뒤
1~ 2, 2 ~ 3, 3~ 4 이런식으로 각각 2일마다 드는 비용을 data에 append한다.
그후 min()을 이용해 최소 값을 출력
"""


n , x = map(int, input().split())
socks = list(map(int, input().split()))

data = []

for i in range(len((socks)) - 1):
    data.append(socks[i] * x + socks[i+1] * x)

answer = min(data)

print(answer)
