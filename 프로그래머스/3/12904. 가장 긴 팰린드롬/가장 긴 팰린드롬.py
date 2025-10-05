def solution(s):
    n = len(s)
    if n <= 1:
        return n
    
    def expand(l, r):
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1  # 마지막 실패 한 번 전 길이
    
    ans = 1
    for i in range(n):
        # 홀수 중심
        ans = max(ans, expand(i, i))
        # 짝수 중심
        ans = max(ans, expand(i, i+1))
        
    return ans
