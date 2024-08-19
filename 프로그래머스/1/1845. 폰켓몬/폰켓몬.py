def solution(nums):
    # 문제 이해
    # - N개의 요소가 있는 리스트가 한 개 주어진다.
    # - 주어진 리스트에서 N/2 개를 선택할 수 있는 경우의 수의 합을 구한다.
    # - 이 때 중복된 숫자를 선택한 경우는 제외한다.
    # 아이디어
    # !! 중복을 제거함
    # !! 중복되지 않은 상태에선 어떻게든 골라도 가능
    # - 중복되지 않은 리스트 만들기(unique)
    # - unique랑 n/2랑 비교
    # -- unique > n/2 : n/2
    # -- unique < n/2 : unique
    
    
    # 제한사항
    answer = 0
    unique = []
    for n in nums:
        if n not in unique:
            unique.append(n)
    
    selection = len(nums)//2
    uniqCnt = len(unique)
    
    if selection > uniqCnt:
        return uniqCnt
    return selection