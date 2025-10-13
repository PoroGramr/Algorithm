"""
# 2차원 배열 만들기
    arr = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            y = i + 1
            x = j + 1
            big = max(y,x)
            arr[i][j] = big        

    # 1차원 배열로 변경
    
    arrOne = []
    
    for col in arr:
        for num in col:
            arrOne.append(num)
    
"""


def solution(n, left, right):
    
    """
    1,2,3,2,2,3,3,3,3
    1234
    2234
    3334
    4444
    """
    
    # 1차원 배열 생성
    arr = []
    
    # 요구사항에 맞게 1차원 배열에 값 삽입
    
    for i in range(left, right + 1):
        col = i // n
        
        num = i % n
        
        if num < col:
            num = col
        
        arr.append(num + 1)
        
    
    return arr