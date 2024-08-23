"""
문제이해
- 최소 필요 피로도 : 던전에 입장하기 위해 최소한 필요한 피로도 / 입장 조건
- 소모 피로도 : 던전을 탐험한 후에 소모되는 피로도 / 실제 소모되는 피로도
- 던전은 한 번씩만 탐험할 수 있음

- 입력:
    - k : 현재 피로도
    - dungeons : (최소, 소모) [리스트]
- 출력:
    - 최대로 들어갈 수 있는 던전 수



아이디어
- 던전이 최대 8개임
- 8개짜리 순열!
- 순열을 반복
    - 최소 피로도를 넘는지
    - 넘으면 피로도 깎고
- 최대 탐험 던전 수

제한조건
-dungeons: n max -> 8 
- 8! 1억보단 작음
"""

from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    
    for perm in permutations(dungeons):
        tired = k # 피로도
        count = 0
        
        for minimum, consumtion in perm:
            if tired >= minimum:
                tired -= consumtion
                count += 1
            else:
                break
                
        answer = max(answer, count)
    return answer