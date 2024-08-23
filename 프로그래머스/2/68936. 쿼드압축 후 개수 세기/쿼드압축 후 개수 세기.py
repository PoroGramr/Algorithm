"""
 - 영역에 있는 모든 수가 같으면, 하나로 압축
 - 다른 수가 있다면 4개로 나눠서 -> 압축 가능한지 확인
 
 - 결과: 압축한 결과 0과 1의 개수
 
 아이디어 array, size
 - 영역을 전체 검사해서 압축할 수 있는지 확인
    - 압축가능하면(모두 동일하면 압축)
    - 압축 불가능하면,
        - 영역을 넷으로 나누기
        - 각각 압축할 수 있는지 확인
"""
def quadComp(arr,x,y,size,answer):
    # 압축 가능한지 확인
    value = arr[x][y] # arr의 첫 칸의 값을 확인
    
    same = True
    for i in range(size):
        for j in range(size):
            if arr[x+i][y+j] != value:
                same = False
                break
        if not same:
            break
    
    if same:
        # 압축 가능
        answer[value] += 1
    
    else:
        quadComp(arr, x, y,size//2, answer)
        quadComp(arr, x+size//2, y,size//2, answer)
        quadComp(arr, x, y+size//2, size//2, answer)
        quadComp(arr, x+size//2, y+size//2, size//2, answer)
        
    return
        
    
        
        
    


def solution(arr):
    answer = [0 ,0]
    quadComp(arr, 0, 0, len(arr), answer)
    return answer