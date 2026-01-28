"""
다솜이는 기타를 많이 가지고 있다

각각의 기타는 모두 다른 시리얼 번호를 가지고 있다.

기타를 빨리 찾아서 빨리 연주하기 위해 기타를 시리얼 번호 순서대로 정렬하고자 한다.

시리얼번호는 알파벳 대문자와 숫자로 이루어져 있다.

시리얼 번호 a가 B앞에 오는 경우
1. A와 B의 길이가 다르면, 짧은 것이 먼저
2. 만얀 서로 길이가 같다면, A의 모든 자리수의 합과 B의 모든 자리수의 합을 비교해서 작은 합을 가지는 것이 먼저(숫자만 더함)
3. 1,2 로 비교 불가 시 사전 순으로 비교 숫자가 알파벳보다 사전순으로 작음
"""



n = int(input())

guitars = []

for _ in range(n):
    guitars.append(input())
    
def digitSum(s):
    total = 0
    for c in s:
        if c.isdigit():
            total += int(c)
    
    return total
    
guitars.sort(key = lambda x : (len(x), digitSum(x),x ))
for g in guitars:
    print(g)