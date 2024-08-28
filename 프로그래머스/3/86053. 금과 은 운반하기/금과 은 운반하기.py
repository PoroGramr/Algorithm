"""
필요한 자원 : a,b
도시별 자원 : g,s
트럭 1대 : t,w

주어진 시간 동안 최대한 옮길 수 있는 자원의 수를 찾는 문제
- 주어진 시간 동안 옮길 수 있는 자원의 수
    - 주어진 시간동안 트럭은 몇번 왔다갔다 할 수 있나 -> 횟수 * w
    - move = total time // 2*t but 남은 시간이 t이상이면 한 번 더 움직일 수 있음 
    - move * (g+s)

- 주어진 시간 동안 a, b에 해당하는 자원을 옮길 수 있는 최소 시간을 구하면 됨
    - 더 많은 자원을 옮김 -> right = mid - 1
    - 더 적은 자원을 옮김 -> left = mid - 1
    
"""

def solution(a, b, g, s, w, t):
    left, right = 0, 4*10**15 # 4*10^15 # 충분히 큰 어떤 값
    answer = right # 최악의 경우로 초기화
    
    
    while left <= right:
        mid = (left + right) // 2
        
        total_gold = 0
        total_silver = 0
        total_res = 0
        
        # mid라는 시간 동안 옮길 수 있는 자원의 양
        for i in range(len(g)):
            move = mid // (2*t[i]) # 주어진 시간 동안 트럭이 왕복할 수 있는 수
            if mid % (2*t[i]) >= t[i]: # 한 번 더 움직일 수 있는 시간이 남았으면
                move += 1
                
            max_gold = min(g[i], move * w[i]) # 금만 옮겼을 때
            max_silver = min(s[i], move * w[i]) # 은만 옮겼을 때
            max_res = min(g[i] + s[i], move * w[i]) # 함께 옮겼을 때
        
            total_gold += max_gold
            total_silver += max_silver
            total_res += max_res
        
        # 옮긴 자원이 필요한 자원보다 많은 경우
        if total_gold >= a and total_silver >= b and total_res >= a + b:
            answer = mid # 최소값을 찾는 경우이므로 가능한 왼쪽 범위
            right = mid - 1
        # 옮긴 자원이 필요한 자원보다 적은 경우
        else:
            left = mid + 1
    
    return answer