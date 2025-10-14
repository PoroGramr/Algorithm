"""
가로가 Wcm 세로가 Hcm인 종이가 있음
1x1 의 격자칸이 존재
누군가 이 종이를 대각선으로 잚

이 직각 삼각형종이에서 1x1로 잘라 사용할 수 있는 만큼 사용하기로 하였음

W,H가 주어질 떄 사용할 수 있는 정사각형의 개수를 구하시오

의사코드
기존 사이즈가 정사각형, 직사각형이냐에 따라 달라질듯?


"""
import math
def solution(w,h):
    answer = 1
    
    if w==h:
        answer = w*h - w
        if answer <= 0:
            answer = 0
    else:
        answer = (w*h) - (w + h - math.gcd(w,h))
    return answer