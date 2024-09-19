"""
문제이해
- 입력
    T : 정수 (테스트 케이스)
    N, M : 정수, 정수 (다음 입력으로 주어질 리스트 2개의 길이)
    list1 : 정수 리스트, 길이 N
    list2 : 정수 리스트, 길이 M
- 출력
    answer : 정수


아이디어
케이스는 3가지 이다
1. list1이 list2보다 짧은 경우
2. list1과 list2의 길이가 같은 경우
3. list1이 list2보다 긴 경우

3가지의 경우를 바탕으로 문제를 해결해야 한다. 
"""

n = int(input())


for i in range(n):
  N, M = map(int, input().split())
  listA = list(map(int, input().split()))
  listB = list(map(int, input().split()))
  maxNum = -999999999
  # case1의 경우
  if N < M:
    
    # 긴 리스트의 길이 - 짧은 리스트의 길이 를 이용하여 긴 리스트의 인덱스에 접근한다.
    for k in range(M - N + 1): 
      cal = 0
      for j in range(N):
        cal += listA[j] * listB[j + k]
      maxNum = max(maxNum,cal)

  # case2의 경우
  elif N == M:
    for K in range(M):
      maxNum += listA[k] * listB[k]

  # case3의 경우
  elif N > M:
    # 긴 리스트의 길이 - 짧은 리스트의 길이 를 이용하여 긴 리스트의 인덱스에 접근한다.
    for k in range(N - M + 1):
      cal = 0
      for j in range(M):
        cal += listA[j+k] * listB[j]
      maxNum = max(maxNum,cal)
  print(f"#{i+1} {maxNum}")
    