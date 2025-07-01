'''
이 앨범에는 총 노래가 N곡이 들어있고. 모든 노래의 길이는 L초이다. 그리고 노래와 노래 사이에는 5초 동안 아무 노래도 들리지 않는 조용한 구간이 있다.

강토가 앨범의 첫 곡을 듣는 순간이 0초이다. 그리고 그 0초부터 강토의 전화벨이 울리기 시작한다. 전화벨은 D초에 1번씩 울리며, 한 번 울릴때 1초동안 울린다.

강토가 모든 앨범 수록곡을 듣고 나서 전화벨을 들을 수 있는 시간은?

'''
# 총 N곡, 노래의 길이 L초, 전화벨은 D초의 한번
N, L, D = map(int, input().split())
check = [False] * 5000

index = 0

for _ in range(N):
    for _ in range(L):
        check[index] = True
        index += 1
    
    for _ in range(5):
        index += 1


time = 0
while True:
    if check[time] == False:
        print(time)
        break
    else:
        time += D

    

